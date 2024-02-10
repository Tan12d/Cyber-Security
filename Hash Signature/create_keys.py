import rsa

(pubkey,privkey) = rsa.newkeys(2048)

with open('publickey.key','wb') as key_file:
    key_file.write(pubkey.save_pkcs1('PEM'))

with open('privatekey.key','wb') as key_file:
    key_file.write(privkey.save_pkcs1('PEM'))