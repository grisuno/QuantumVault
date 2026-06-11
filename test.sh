#!/bin/bash
set -e
rm -rf test/encrypted test/decrypted test_decrypted test.tar.gz test.tar.gz.encrypted ciphertext.bin users instance
mkdir -p test/lol
echo "This is a secret text file" > test/secret.txt
dd if=/dev/urandom of=test/binary.bin bs=1024 count=10
echo "Another text file" > test/lol/lolll
./genkey.sh
./enc_dec --mode encrypt --type inplace --pubkey public.key --dir test
python3 enc_dec.py --mode decrypt --type inplace --seckey secret.key --dir test
diff -r test test/decrypted
./enc_dec --mode encrypt --type targz --pubkey public.key --dir test
python3 enc_dec.py --mode decrypt --type targz --seckey secret.key --dir test
diff -r test test_decrypted/test
echo "Testing Flask app..."
redis-server &
python3 app.py &
sleep 5
curl -X POST -d "username=user1&password=test123&_csrf_token=" http://localhost:5000/register
curl -X POST -d "username=admin1&password=test123&_csrf_token=" http://localhost:5000/register
curl -X POST -d "username=superadmin1&password=test123&_csrf_token=" http://localhost:5000/register
curl -X POST -d "username=superadmin1&password=test123&_csrf_token=" http://localhost:5000/login
sqlite3 instance/users.db "UPDATE users SET role='admin' WHERE username='admin1'"
sqlite3 instance/users.db "UPDATE users SET role='superadmin' WHERE username='superadmin1'"
kill %1
kill %2
