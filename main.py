import hashlib

password = input("Enter Password: ")

encrypted = hashlib.sha256(password.encode()).hexdigest()

print("Encrypted Password:", encrypted)