import argparse
import io
import qrcode
import os
from colorama import init, Fore, Back

version = 1.0


def main():
    parser = argparse.ArgumentParser(
        description='FastQR: Créez des codes QR facilement et rapidement sur votre terminal. Dépôt Github: https://github.com/Luckyluka17/FastQR'
    )

    parser.add_argument(
        '-g', '--generate',
        help='Génère un code QR (exemple: fastqr --generate https://google.com)',
        dest='generate',
        required=True,
        type=str,
    )
    parser.add_argument(
        '-o', '--out',
        help='Exporter le code QR dans un fichier de sortie (exemple: fastqr --generate https://google.com --out test.txt)',
        dest='out',
        type=str,
    )
    parser.add_argument(
        '-c', '--color',
        help='Couleur de sortie du code QR dans le terminal (voir les couleurs prises en charge sur cette page : )',
        dest='color',
        type=str,
        default="WHITE"
    )


    args = parser.parse_args()

    if args.generate:

        qr = qrcode.QRCode()

        qr.add_data(str(args.generate))

        if args.out:
            if not os.path.exists(f"{args.out}"):
                with open(f"{args.out}", "w", encoding="utf-8") as f:
                    qr.print_ascii(out=f)
                    f.seek(0)
                    f.close()
                if os.path.exists(f"{args.out}"):
                    print(Fore.GREEN + f"Le code QR a été exporté dans le fichier {args.out}.")
                else:
                    print(Fore.RED + f"Une erreur s'est produite.")
            else:
                print(Fore.RED + f"Un fichier nommé {args.out} existe déjà dans le répertoire sélectionné.")

        else:
            f = io.StringIO()
            qr.print_ascii(out=f)
            f.seek(0)

            if args.color == "CLASSIC":
                print(Back.WHITE + Fore.BLACK + f.read())
            elif args.color == "BLUE":
                print(Fore.BLUE + f.read())
            elif args.color == "CYAN":
                print(Fore.CYAN + f.read())
            elif args.color == "GREEN":
                print(Fore.GREEN + f.read())
            elif args.color == "RED":
                print(Fore.RED + f.read())
            elif args.color == "MAGENTA":
                print(Fore.MAGENTA + f.read())
            elif args.color == "WHITE":
                print(Fore.WHITE + f.read())
            elif args.color == "YELLOW":
                print(Fore.YELLOW + f.read())
            else:
                print(Fore.RED + f"La couleur \"{args.color}\" est invalide.") 

if __name__ == "__main__":
    init(autoreset=True)
    main()