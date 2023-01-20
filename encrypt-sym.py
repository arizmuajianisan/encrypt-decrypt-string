from cryptography.fernet import Fernet

message = str(input("Input message to encrypt: "))

key = Fernet.generate_key()
print("key is: ",key)

fernet = Fernet(key)
print("fernet is: ", fernet)

encryptMessage = fernet.encrypt(message.encode())

print("Original string: ", message)
print("Encrypted string :", encryptMessage)

decryptMessage = fernet.decrypt(encryptMessage).decode()

print("Decrypted message: ", decryptMessage)