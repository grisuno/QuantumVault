CGO_LDFLAGS="-L/usr/local/lib -loqs" CGO_CFLAGS="-I/usr/local/include" go build -o enc_dec enc_dec.go
CGO_LDFLAGS="-L/usr/local/lib -loqs" CGO_CFLAGS="-I/usr/local/include" go build -o client client.go
CGO_LDFLAGS="-L/usr/local/lib -loqs" CGO_CFLAGS="-I/usr/local/include" go build -o server server.go
