import qrcode


def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


# Example usage:
if __name__ == '__main__':
    data = 'https://arshadalism.github.io/Portfolio-website/'
    filename = "example_qr_code.png"
    generate_qr_code(data, filename)
    print(f"QR code generated and saved as {filename}")
