import hashlib

pass_found = 0
i_hash = input("Enter the hashed password: ")
p_doc = input("\nEnter password file name including path: ")
p_file = open(p_doc,"r")

for word in p_file:
    encode_word = word.encode('utf-8')
    hash_word = hashlib.md5(encode_word.strip())
    digest = hash_word.hexdigest()
    # print(digest)
    if digest == i_hash: # md5hashgenerator.com
    # if digest == hashlib.md5(i_hash.encode('utf-8').strip()).hexdigest():
        print("password found:",word)
        pass_found=1
        break

if not pass_found:
    print("password not found") 
