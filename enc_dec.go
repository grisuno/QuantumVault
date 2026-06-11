package main

import (
    "archive/tar"
    "compress/gzip"
    "crypto/aes"
    "crypto/cipher"
    "crypto/rand"
    "flag"
    "fmt"
    "io"
    "os"
    "path/filepath"
    "strings"
    "github.com/open-quantum-safe/liboqs-go/oqs"
    "golang.org/x/crypto/pbkdf2"
    "crypto/sha256"
)

func deriveAESKey(sharedSecret []byte) []byte {
    return pbkdf2.Key(sharedSecret, []byte(""), 100000, 32, sha256.New)
}

func encryptFile(inputPath, outputPath string, aesKey []byte) error {
    data, err := os.ReadFile(inputPath)
    if err != nil {
        return fmt.Errorf("error al leer %s: %v", inputPath, err)
    }
    nonce := make([]byte, 12)
    if _, err := rand.Read(nonce); err != nil {
        return fmt.Errorf("error al generar nonce: %v", err)
    }
    block, err := aes.NewCipher(aesKey)
    if err != nil {
        return fmt.Errorf("error al crear cifrador AES: %v", err)
    }
    aesgcm, err := cipher.NewGCM(block)
    if err != nil {
        return fmt.Errorf("error al crear GCM: %v", err)
    }
    ciphertext := aesgcm.Seal(nil, nonce, data, nil)
    return os.WriteFile(outputPath, append(nonce, ciphertext...), 0644)
}

func decryptFile(inputPath, outputPath string, aesKey []byte) error {
    data, err := os.ReadFile(inputPath)
    if err != nil {
        return fmt.Errorf("error al leer %s: %v", inputPath, err)
    }
    if len(data) < 12 {
        return fmt.Errorf("archivo cifrado inválido: %s", inputPath)
    }
    nonce, ciphertext := data[:12], data[12:]
    block, err := aes.NewCipher(aesKey)
    if err != nil {
        return fmt.Errorf("error al crear cifrador AES: %v", err)
    }
    aesgcm, err := cipher.NewGCM(block)
    if err != nil {
        return fmt.Errorf("error al crear GCM: %v", err)
    }
    plaintext, err := aesgcm.Open(nil, nonce, ciphertext, nil)
    if err != nil {
        return fmt.Errorf("error al descifrar %s: %v", inputPath, err)
    }
    return os.WriteFile(outputPath, plaintext, 0644)
}

func main() {
    mode := flag.String("mode", "", "Modo: encrypt o decrypt")
    typ := flag.String("type", "", "Tipo: inplace o targz")
    dir := flag.String("dir", "", "Directorio a cifrar/descifrar")
    pubkey := flag.String("pubkey", "", "Archivo con clave pública (para cifrado)")
    seckey := flag.String("seckey", "", "Archivo con clave secreta (para descifrado)")
    flag.Parse()

    if *mode != "encrypt" && *mode != "decrypt" {
        fmt.Println("Error: --mode debe ser 'encrypt' o 'decrypt'")
        os.Exit(1)
    }
    if *typ != "inplace" && *typ != "targz" {
        fmt.Println("Error: --type debe ser 'inplace' o 'targz'")
        os.Exit(1)
    }
    if *dir == "" {
        fmt.Println("Error: --dir es requerido")
        os.Exit(1)
    }

    kem := &oqs.KeyEncapsulation{}
    defer kem.Clean()
    if err := kem.Init("ML-KEM-512", nil); err != nil {
        fmt.Printf("Error al inicializar KEM: %v\n", err)
        os.Exit(1)
    }

    if *mode == "encrypt" {
        if *pubkey == "" {
            fmt.Println("Error: se requiere --pubkey para cifrado")
            os.Exit(1)
        }
        if _, err := os.Stat(*dir); os.IsNotExist(err) {
            fmt.Printf("Error: el directorio '%s' no existe\n", *dir)
            os.Exit(1)
        }
        publicKey, err := os.ReadFile(*pubkey)
        if err != nil {
            fmt.Printf("Error al leer clave pública: %v\n", err)
            os.Exit(1)
        }
        ciphertext, sharedSecret, err := kem.EncapSecret(publicKey)
        if err != nil {
            fmt.Printf("Error al encapsular: %v\n", err)
            os.Exit(1)
        }
        aesKey := deriveAESKey(sharedSecret)

        if *typ == "inplace" {
            outputDir := filepath.Join(*dir, "encrypted")
            if err := os.MkdirAll(outputDir, 0755); err != nil {
                fmt.Printf("Error al crear directorio %s: %v\n", outputDir, err)
                os.Exit(1)
            }
            err = filepath.Walk(*dir, func(path string, info os.FileInfo, err error) error {
                if err != nil {
                    return err
                }
                if !info.IsDir() && !strings.HasPrefix(filepath.Dir(path), outputDir) {
                    relPath, err := filepath.Rel(*dir, path)
                    if err != nil {
                        return fmt.Errorf("error al calcular path relativo para %s: %v", path, err)
                    }
                    outputPath := filepath.Join(outputDir, relPath)
                    if err := os.MkdirAll(filepath.Dir(outputPath), 0755); err != nil {
                        return err
                    }
                    if err := encryptFile(path, outputPath, aesKey); err != nil {
                        return err
                    }
                    fmt.Printf("Cifrado: %s -> %s\n", path, outputPath)
                }
                return nil
            })
            if err != nil {
                fmt.Printf("Error al cifrar archivos: %v\n", err)
                os.Exit(1)
            }
            if err := os.WriteFile("ciphertext.bin", ciphertext, 0644); err != nil {
                fmt.Printf("Error al guardar ciphertext: %v\n", err)
                os.Exit(1)
            }
            fmt.Printf("Clave secreta compartida: %x\n", sharedSecret)
            fmt.Println("Ciphertext guardado en ciphertext.bin")

        } else if *typ == "targz" {
            tarFile, err := os.Create("test.tar.gz")
            if err != nil {
                fmt.Printf("Error al crear test.tar.gz: %v\n", err)
                os.Exit(1)
            }
            gw := gzip.NewWriter(tarFile)
            tw := tar.NewWriter(gw)
            err = filepath.Walk(*dir, func(path string, info os.FileInfo, err error) error {
                if err != nil {
                    return err
                }
                if !info.IsDir() && !strings.HasPrefix(filepath.Dir(path), filepath.Join(*dir, "encrypted")) {
                    header, err := tar.FileInfoHeader(info, "")
                    if err != nil {
                        return err
                    }
                    relPath, err := filepath.Rel(*dir, path)
                    if err != nil {
                        return fmt.Errorf("error al calcular path relativo para %s: %v", path, err)
                    }
                    header.Name = filepath.Join(filepath.Base(*dir), filepath.ToSlash(relPath))
                    if err := tw.WriteHeader(header); err != nil {
                        return err
                    }
                    file, err := os.Open(path)
                    if err != nil {
                        return err
                    }
                    defer file.Close()
                    _, err = io.Copy(tw, file)
                    return err
                }
                return nil
            })
            if err != nil {
                fmt.Printf("Error al crear tar: %v\n", err)
                os.Exit(1)
            }
            tw.Close()
            gw.Close()
            tarFile.Close()
            if err := encryptFile("test.tar.gz", "test.tar.gz.encrypted", aesKey); err != nil {
                fmt.Printf("Error al cifrar tar: %v\n", err)
                os.Exit(1)
            }
            os.Remove("test.tar.gz")
            if err := os.WriteFile("ciphertext.bin", ciphertext, 0644); err != nil {
                fmt.Printf("Error al guardar ciphertext: %v\n", err)
                os.Exit(1)
            }
            fmt.Println("Directorio comprimido y cifrado en test.tar.gz.encrypted")
            fmt.Printf("Clave secreta compartida: %x\n", sharedSecret)
            fmt.Println("Ciphertext guardado en ciphertext.bin")
        }

    } else if *mode == "decrypt" {
        if *seckey == "" {
            fmt.Println("Error: se requiere --seckey para descifrado")
            os.Exit(1)
        }
        secretKey, err := os.ReadFile(*seckey)
        if err != nil {
            fmt.Printf("Error al leer clave secreta: %v\n", err)
            os.Exit(1)
        }
        if err := kem.Init("ML-KEM-512", secretKey); err != nil {
            fmt.Printf("Error al inicializar KEM con clave secreta: %v\n", err)
            os.Exit(1)
        }
        ciphertext, err := os.ReadFile("ciphertext.bin")
        if err != nil {
            fmt.Printf("Error al leer ciphertext: %v\n", err)
            os.Exit(1)
        }
        sharedSecret, err := kem.DecapSecret(ciphertext)
        if err != nil {
            fmt.Printf("Error al desencapsular: %v\n", err)
            os.Exit(1)
        }
        aesKey := deriveAESKey(sharedSecret)

        if *typ == "inplace" {
            encryptedDir := filepath.Join(*dir, "encrypted")
            outputDir := filepath.Join(*dir, "decrypted")
            if _, err := os.Stat(encryptedDir); os.IsNotExist(err) {
                fmt.Printf("Error: el directorio %s no existe\n", encryptedDir)
                os.Exit(1)
            }
            if err := os.MkdirAll(outputDir, 0755); err != nil {
                fmt.Printf("Error al crear directorio %s: %v\n", outputDir, err)
                os.Exit(1)
            }
            err = filepath.Walk(encryptedDir, func(path string, info os.FileInfo, err error) error {
                if err != nil {
                    return err
                }
                if !info.IsDir() {
                    relPath, err := filepath.Rel(encryptedDir, path)
                    if err != nil {
                        return fmt.Errorf("error al calcular path relativo para %s: %v", path, err)
                    }
                    outputPath := filepath.Join(outputDir, relPath)
                    if err := os.MkdirAll(filepath.Dir(outputPath), 0755); err != nil {
                        return err
                    }
                    if err := decryptFile(path, outputPath, aesKey); err != nil {
                        return err
                    }
                    fmt.Printf("Descifrado: %s -> %s\n", path, outputPath)
                }
                return nil
            })
            if err != nil {
                fmt.Printf("Error al descifrar archivos: %v\n", err)
                os.Exit(1)
            }
            fmt.Printf("Clave secreta compartida: %x\n", sharedSecret)

        } else if *typ == "targz" {
            if _, err := os.Stat("test.tar.gz.encrypted"); os.IsNotExist(err) {
                fmt.Printf("Error: el archivo test.tar.gz.encrypted no existe\n")
                os.Exit(1)
            }
            if err := decryptFile("test.tar.gz.encrypted", "test.tar.gz", aesKey); err != nil {
                fmt.Printf("Error al descifrar tar: %v\n", err)
                os.Exit(1)
            }
            outputDir := fmt.Sprintf("%s_decrypted", filepath.Base(*dir))
            if err := os.MkdirAll(outputDir, 0755); err != nil {
                fmt.Printf("Error al crear directorio %s: %v\n", outputDir, err)
                os.Exit(1)
            }
            tarFile, err := os.Open("test.tar.gz")
            if err != nil {
                fmt.Printf("Error al abrir test.tar.gz: %v\n", err)
                os.Exit(1)
            }
            defer tarFile.Close()
            gr, err := gzip.NewReader(tarFile)
            if err != nil {
                fmt.Printf("Error al crear lector gzip: %v\n", err)
                os.Exit(1)
            }
            defer gr.Close()
            tr := tar.NewReader(gr)
            for {
                header, err := tr.Next()
                if err == io.EOF {
                    break
                }
                if err != nil {
                    fmt.Printf("Error al leer tar: %v\n", err)
                    os.Exit(1)
                }
                if header.Typeflag == tar.TypeReg {
                    outputPath := filepath.Join(outputDir, header.Name)
                    if err := os.MkdirAll(filepath.Dir(outputPath), 0755); err != nil {
                        fmt.Printf("Error al crear directorio %s: %v\n", filepath.Dir(outputPath), err)
                        os.Exit(1)
                    }
                    f, err := os.Create(outputPath)
                    if err != nil {
                        fmt.Printf("Error al crear archivo %s: %v\n", outputPath, err)
                        os.Exit(1)
                    }
                    if _, err := io.Copy(f, tr); err != nil {
                        f.Close()
                        fmt.Printf("Error al escribir archivo %s: %v\n", outputPath, err)
                        os.Exit(1)
                    }
                    f.Close()
                    fmt.Printf("Descifrado y descomprimido: %s\n", outputPath)
                }
            }
            os.Remove("test.tar.gz")
            fmt.Printf("Archivo descifrado y descomprimido en %s\n", outputDir)
            fmt.Printf("Clave secreta compartida: %x\n", sharedSecret)
        }
    }
}