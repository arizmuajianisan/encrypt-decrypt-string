from cryptography.fernet import Fernet

message = str(input("Input encoded message: "))

#key = Fernet.generate_key()

#fernet = Fernet(key)

decryptMessage = message.decrypt(message).decode()

print("Decrypted result: ", decryptMessage)