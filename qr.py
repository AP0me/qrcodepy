import qrcode
import os

def generate_qr_code(link, file_name):
  # Create a QR code instance
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
  )
  
  # Add the link to the QR code
  qr.add_data(link)
  qr.make(fit=True)
  
  # Create an image from the QR code
  img = qr.make_image(fill_color="black", back_color="white")
  
  # Save the image to a file
  img.save(file_name)

def generate_qr_codes(base_url, start_id, end_id, output_dir):
  # Create the output directory if it doesn't exist
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  for i in range(start_id, end_id + 1):
    link = f"{base_url}?id={i}"
    file_name = os.path.join(output_dir, f"qr_code_{i}.png")
    generate_qr_code(link, file_name)
    print(f"Generated QR code for {link} and saved as {file_name}")

# Example usage
base_url = "http://62.212.239.42:7777/adaqrchecker.com/qrcode.php"
start_id = 239
end_id = 240
output_dir = "qr_codes"

generate_qr_codes(base_url, start_id, end_id, output_dir)
