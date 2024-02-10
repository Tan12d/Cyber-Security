import rsa

def file_open(file):
    key_file = open(file,'rb')
    key_data = key_file.read()
    key_file.close()

    return key_data

privkey = rsa.PrivateKey.load_pkcs1(file_open('privatekey.key'))

message = file_open('dict1.py')
hash_value = rsa.compute_hash(message,'SHA-512')
signature = rsa.sign(message,privkey,'SHA-512')
s = open('signature_file','wb')
s.write(signature)
print(signature)
print(len(signature))
print(len(hash_value)*8)