from cryptography.fernet import Fernet
import pyqrcode

# Generate a key for encryption
key = Fernet.generate_key()

# Define the public data
public_data = "Public QR Code Data"

# Define the private data
private_data = "Private QR Code Data"

# Encrypt the private data using the key
cipher_suite = Fernet(key)
encrypted_private_data = cipher_suite.encrypt(private_data.encode())

# Generate the QR code with the public data
qr_code = pyqrcode.create(public_data)

# Save the QR code as an image
qr_code.png("qr_code.png", scale=5)

# Save the encrypted private data separately
with open("private_data.txt", "wb") as file:
    file.write(encrypted_private_data)
