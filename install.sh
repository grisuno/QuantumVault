#!/bin/bash

# install.sh: Script para instalar prerrequisitos y compilar el proyecto postcuantum
# Fecha: 26 de junio de 2025
# Autor: Grok 3 (xAI)

set -e  # Salir al primer error

# Colores para mensajes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # Sin color

# Directorio de trabajo
WORK_DIR="/home/$USER/src/py/postcuantum"
REPO_DIR="$WORK_DIR/liboqs"
PYTHON_REPO_DIR="$WORK_DIR/liboqs-python"
PROJECT_DIR="$WORK_DIR/v1"
GO_VERSION="1.24.2"
LIBOQS_VERSION="0.13.1-dev"

echo -e "${YELLOW}=== Iniciando instalación de prerrequisitos para el proyecto postcuantum ===${NC}"

# 1. Actualizar el sistema e instalar dependencias
echo -e "${GREEN}1. Instalando dependencias del sistema...${NC}"
sudo apt-get update
sudo apt-get install -y \
    git \
    cmake \
    build-essential \
    libssl-dev \
    python3 \
    python3-pip \
    python3-venv \
    wget \
    unzip \
    pkg-config \
    ufw

# 2. Instalar Go
echo -e "${GREEN}2. Instalando Go $GO_VERSION...${NC}"
if ! command -v go &> /dev/null || [[ $(go version | grep -oP 'go\d+\.\d+\.\d+') != "go$GO_VERSION" ]]; then
    wget https://golang.org/dl/go$GO_VERSION.linux-amd64.tar.gz -O /tmp/go.tar.gz
    sudo rm -rf /usr/local/go
    sudo tar -C /usr/local -xzf /tmp/go.tar.gz
    rm /tmp/go.tar.gz
    echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
    echo 'export GOPATH=$HOME/go' >> ~/.bashrc
    export PATH=$PATH:/usr/local/go/bin
    export GOPATH=$HOME/go
else
    echo -e "${YELLOW}Go $GO_VERSION ya está instalado${NC}"
fi
go version

# 3. Crear directorios
echo -e "${GREEN}3. Creando directorios del proyecto...${NC}"
mkdir -p $WORK_DIR $PROJECT_DIR $GOPATH

# 4. Clonar y compilar liboqs
echo -e "${GREEN}4. Instalando liboqs $LIBOQS_VERSION...${NC}"
if [ ! -d "$REPO_DIR" ]; then
    git clone --branch $LIBOQS_VERSION https://github.com/open-quantum-safe/liboqs.git $REPO_DIR
else
    cd $REPO_DIR
    git checkout $LIBOQS_VERSION
fi
cd $REPO_DIR
rm -rf build
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DBUILD_SHARED_LIBS=ON ..
make -j$(nproc)
sudo make install
sudo ldconfig
# Crear liboqs-go.pc
sudo cp /usr/local/lib/pkgconfig/liboqs.pc /usr/local/lib/pkgconfig/liboqs-go.pc
pkg-config --modversion liboqs

# 5. Instalar liboqs-python
echo -e "${GREEN}5. Instalando liboqs-python...${NC}"
if [ ! -d "$PYTHON_REPO_DIR" ]; then
    git clone https://github.com/open-quantum-safe/liboqs-python.git $PYTHON_REPO_DIR
fi
cd $PYTHON_REPO_DIR
pip3 install --force-reinstall .
python3 -c "import oqs; print('liboqs-python version:', oqs.__version__)"

# 6. Instalar dependencias de Python
echo -e "${GREEN}6. Instalando dependencias de Python...${NC}"
pip3 install cryptography

# 7. Configurar el entorno Go
echo -e "${GREEN}7. Configurando el entorno Go...${NC}"
cd $PROJECT_DIR
if [ ! -f "go.mod" ]; then
    go mod init postquantum
fi
go get github.com/open-quantum-safe/liboqs-go@v0.0.0-20250119172907-28b5301df438
go mod tidy

# 8. Compilar client.go
echo -e "${GREEN}8. Compilando client.go...${NC}"
if [ -f "client.go" ]; then
    CGO_LDFLAGS="-L/usr/local/lib -loqs" CGO_CFLAGS="-I/usr/local/include" go build -o client client.go
    if [ -f "client" ]; then
        echo -e "${GREEN}client.go compilado exitosamente${NC}"
    else
        echo -e "${RED}Error al compilar client.go${NC}"
        exit 1
    fi
else
    echo -e "${RED}client.go no encontrado en $PROJECT_DIR${NC}"
    exit 1
fi

# 9. Compilar server_oqs.go
echo -e "${GREEN}9. Compilando server_oqs.go...${NC}"
if [ -f "server_oqs.go" ]; then
    CGO_LDFLAGS="-L/usr/local/lib -loqs" CGO_CFLAGS="-I/usr/local/include" go build -o server_oqs server_oqs.go
    if [ -f "server_oqs" ]; then
        echo -e "${GREEN}server_oqs.go compilado exitosamente${NC}"
    else
        echo -e "${RED}Error al compilar server_oqs.go${NC}"
        exit 1
    fi
else
    echo -e "${YELLOW}server_oqs.go no encontrado, creando uno por defecto${NC}"
    cat << EOF > server_oqs.go
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
EOF
    CGO_LDFLAGS="-L/usr/local/lib -loqs" CGO_CFLAGS="-I/usr/local/include" go build -o server_oqs server_oqs.go
    if [ -f "server_oqs" ]; then
        echo -e "${GREEN}server_oqs.go creado y compilado exitosamente${NC}"
    else
        echo -e "${RED}Error al compilar server_oqs.go${NC}"
        exit 1
    fi
fi

# 10. Configurar el firewall
echo -e "${GREEN}10. Configurando el firewall...${NC}"
sudo ufw allow 12345
sudo ufw status

# 11. Verificar instalación
echo -e "${GREEN}11. Verificando instalación...${NC}"
if command -v go &> /dev/null; then
    echo -e "${GREEN}Go instalado: $(go version)${NC}"
else
    echo -e "${RED}Go no está instalado${NC}"
    exit 1
fi
if pkg-config --modversion liboqs &> /dev/null; then
    echo -e "${GREEN}liboqs instalado: $(pkg-config --modversion liboqs)${NC}"
else
    echo -e "${RED}liboqs no está instalado${NC}"
    exit 1
fi
if python3 -c "import oqs" &> /dev/null; then
    echo -e "${GREEN}liboqs-python instalado: $(python3 -c "import oqs; print(oqs.__version__)")${NC}"
else
    echo -e "${RED}liboqs-python no está instalado${NC}"
    exit 1
fi
if python3 -c "import cryptography" &> /dev/null; then
    echo -e "${GREEN}cryptography instalado${NC}"
else
    echo -e "${RED}cryptography no está instalado${NC}"
    exit 1
fi
if [ -f "$PROJECT_DIR/client" ] && [ -f "$PROJECT_DIR/server_oqs" ]; then
    echo -e "${GREEN}Binarios client y server_oqs compilados${NC}"
else
    echo -e "${RED}Faltan binarios compilados${NC}"
    exit 1
fi

# 12. Instrucciones finales
echo -e "${GREEN}=== Instalación completada ===${NC}"
echo -e "${YELLOW}Para probar el proyecto:${NC}"
echo -e "1. En el target (10.10.14.26):"
echo -e "   cd $PROJECT_DIR"
echo -e "   ./server_oqs  # o python3 server.py"
echo -e "2. En el gateway (192.168.1.1):"
echo -e "   cd $PROJECT_DIR"
echo -e "   ./client -g 192.168.1.1 -t 10.10.14.26 -m \"Hola este es un mensaje secreto\""
echo -e "   # o python3 client.py -g 192.168.1.1 -t 10.10.14.26 -m \"Hola, este es un mensaje secreto\""
