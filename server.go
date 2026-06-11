package main

import (
    "crypto/aes"
    "crypto/cipher"
    "fmt"
    "net"
    "github.com/open-quantum-safe/liboqs-go/oqs"
)

func main() {
    listener, err := net.Listen("tcp", ":12345")
    if err != nil {
        fmt.Printf("Error al iniciar el servidor: %v\n", err)
        return
    }
    defer listener.Close()
    fmt.Println("Servidor escuchando en 0.0.0.0:12345...")

    kem := oqs.KeyEncapsulation{}
    defer kem.Clean()
    err = kem.Init("ML-KEM-512", nil)
    if err != nil {
        fmt.Printf("Error al inicializar KEM: %v\n", err)
        return
    }
    fmt.Printf("PublicKey size: %d, Ciphertext size: %d\n", kem.Details().LengthPublicKey, kem.Details().LengthCiphertext)

    for {
        conn, err := listener.Accept()
        if err != nil {
            fmt.Printf("Error al aceptar conexión: %v\n", err)
            continue
        }
        fmt.Printf("Conexión establecida desde %v\n", conn.RemoteAddr())
        go handleConnection(conn, &kem)
    }
}

func handleConnection(conn net.Conn, kem *oqs.KeyEncapsulation) {
    defer conn.Close()

    publicKey, err := kem.GenerateKeyPair()
    if err != nil {
        fmt.Printf("Error al generar keypair: %v\n", err)
        return
    }
    fmt.Printf("Enviando publicKey (%d bytes): %x\n", len(publicKey), publicKey)

    _, err = conn.Write(publicKey)
    if err != nil {
        fmt.Printf("Error al enviar publicKey: %v\n", err)
        return
    }

    ciphertext := make([]byte, kem.Details().LengthCiphertext)
    n, err := conn.Read(ciphertext)
    if err != nil {
        fmt.Printf("Error al recibir ciphertext: %v\n", err)
        return
    }
    fmt.Printf("Recibido ciphertext (%d bytes): %x\n", n, ciphertext)

    sharedSecret, err := kem.DecapSecret(ciphertext)
    if err != nil {
        fmt.Printf("Error al desencapsular: %v\n", err)
        return
    }
    fmt.Printf("Shared secret (target): %x\n", sharedSecret)

    nonce := make([]byte, 12)
    n, err = conn.Read(nonce)
    if err != nil {
        fmt.Printf("Error al recibir nonce: %v\n", err)
        return
    }
    encryptedMessage := make([]byte, 1024)
    n, err = conn.Read(encryptedMessage)
    if err != nil {
        fmt.Printf("Error al recibir mensaje cifrado: %v\n", err)
        return
    }
    encryptedMessage = encryptedMessage[:n]
    fmt.Printf("Recibido nonce (%d bytes): %x, encryptedMessage (%d bytes): %x\n", len(nonce), nonce, len(encryptedMessage), encryptedMessage)

    block, err := aes.NewCipher(sharedSecret)
    if err != nil {
        fmt.Printf("Error al crear cifrador AES: %v\n", err)
        return
    }
    aesgcm, err := cipher.NewGCM(block)
    if err != nil {
        fmt.Printf("Error al crear GCM: %v\n", err)
        return
    }
    decryptedMessage, err := aesgcm.Open(nil, nonce, encryptedMessage, nil)
    if err != nil {
        fmt.Printf("Error al descifrar mensaje: %v\n", err)
        return
    }
    fmt.Printf("Mensaje descifrado: %s\n", decryptedMessage)
}
