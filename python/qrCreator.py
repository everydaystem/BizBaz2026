import qrcode
from colorama import Fore, init

init(autoreset=True)

print("Combine your name and a custom message into a single terminal QR code.\n")

name = input("Enter your name: ").strip()
message = input("Enter your message: ").strip()

if not name or not message:
    print(f"{Fore.RED}Both name and message are required! Exiting program.")
else:
    combined_data = f"Name: {name}\nMessage: {message}"

    print(f"\n{Fore.YELLOW}Generating your custom terminal QR code...\n")

    qr = qrcode.QRCode(version=1, box_size=1, border=1)
    qr.add_data(combined_data)
    qr.make(fit=True)

    qr.print_tty()
