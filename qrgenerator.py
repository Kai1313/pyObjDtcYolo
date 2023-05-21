import qrcode
from qrcode.util import best_fit

# Define the public data and private data
public_data = "Public QR Code Data"
private_data = "Private QR Code Data"

# Calculate the appropriate QR code version based on the length of the private data
version = best_fit(private_data, error_correction=qrcode.constants.ERROR_CORRECT_H)

# Create the QR code for the public data
public_qr = qrcode.QRCode(version=version, error_correction=qrcode.constants.ERROR_CORRECT_H)
public_qr.add_data(public_data)
public_qr.make()

# Convert the private data into binary format
binary_data = ''.join(format(ord(char), '08b') for char in private_data)

# Embed the binary data into the public QR code
qr_img = public_qr.make_image(fill_color="black", back_color="white")
qr_pixels = qr_img.get_image().convert('RGB')

for i in range(len(binary_data)):
    row = i // qr_img.size[0]
    col = i % qr_img.size[0]
    pixel = qr_pixels.getpixel((col, row))
    if binary_data[i] == '1':
        qr_pixels.putpixel((col, row), (pixel[0], pixel[1], pixel[2] ^ 1))

# Save the masked QR code as an image file
masked_qr_file = "masked_qr_code.png"
qr_img.save(masked_qr_file)
