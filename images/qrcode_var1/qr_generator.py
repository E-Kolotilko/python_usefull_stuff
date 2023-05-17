import qrcode

def save_qr(text, save_path):
    img = qrcode.make(text)
    img.save(save_path)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('No text input. Making a run as a demo that it works')
        text = 'https://www.google.com'
    else:
        text = sys.argv[1]
    save_qr(text, 'myQrCode.png')
