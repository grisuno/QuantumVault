package main

import (
    "crypto/aes"
    "crypto/cipher"
    "crypto/rand"
    "flag"
    "fmt"
    "net"
    "github.com/open-quantum-safe/liboqs-go/oqs"
)

func main() {
    gateway := flag.String("g", "", "Dirección IP del gateway")
    target := flag.String("t", "", "Dirección IP del target")
    message := flag.String("m", "¡Hola, este es un mensaje secreto!", "Mensaje a cifrar")
    flag.Parse()

    fmt.Printf("Gateway: %s, Target: %s, Message: %s\n", *gateway, *target, *message)

    conn, err := net.Dial("tcp", *target+":12345")
    if err != nil {
        fmt.Printf("Error al conectar al target %s:12345: %v\n", *target, err)
        return
    }
    defer conn.Close()

    // Inicializa ML-KEM-512
    kem := oqs.KeyEncapsulation{}
    defer kem.Clean()
    err = kem.Init("ML-KEM-512", nil)
    if err != nil {
        fmt.Printf("Error al inicializar KEM: %v\n", err)
        return
    }

    // Recibe la clave pública (800 bytes)
    publicKey := make([]byte, kem.Details().LengthPublicKey)
    n, err := conn.Read(publicKey)
    if err != nil {
        fmt.Printf("Error al recibir publicKey: %v\n", err)
        return
    }
    fmt.Printf("Recibido publicKey (%d bytes): %x\n", n, publicKey)

    // Encapsula el secreto compartido
    ciphertext, sharedSecret, err := kem.EncapSecret(publicKey)
    if err != nil {
        fmt.Printf("Error al encapsular: %v\n", err)
        return
    }
    fmt.Printf("Enviando ciphertext (%d bytes): %x\n", len(ciphertext), ciphertext)

    // Envía el ciphertext (768 bytes)
    _, err = conn.Write(ciphertext)
    if err != nil {
        fmt.Printf("Error al enviar ciphertext: %v\n", err)
        return
    }
    fmt.Println("Enviado ciphertext al target")

    // Cifra el mensaje con AES-256-GCM
    messageBytes := []byte(*message)
    nonce := make([]byte, 12)
    _, err = rand.Read(nonce)
    if err != nil {
        fmt.Printf("Error al generar nonce: %v\n", err)
        return
    }
    // Usa sharedSecret directamente (sin PBKDF2)
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
    encryptedMessage := aesgcm.Seal(nil, nonce, messageBytes, nil)
    fmt.Printf("Enviando nonce (%d bytes): %x, encryptedMessage (%d bytes): %x\n", len(nonce), nonce, len(encryptedMessage), encryptedMessage)

    // Envía nonce + mensaje cifrado
    _, err = conn.Write(append(nonce, encryptedMessage...))
    if err != nil {
        fmt.Printf("Error al enviar mensaje cifrado: %v\n", err)
        return
    }
    fmt.Println("Enviado mensaje cifrado al target")

    fmt.Printf("Shared secret (gateway): %x\n", sharedSecret)
}
