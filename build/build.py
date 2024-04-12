import os

path = os.getcwd()

print("Compilation du code... [1/2]")
os.system(f'pyinstaller --noconfirm --onefile --console --icon "{path}/assets/images/logo.ico"  "{path}/fastqr.py"')
# print("Compilation du code... [2/2]")
# os.system(f'pyinstaller --noconfirm --onefile --windowed --icon "{path}/assets/images/logo.ico"  "{path}/gui.py"')