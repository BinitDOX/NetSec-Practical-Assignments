from gui import GUI
from crypter import Crypter

if __name__ == '__main__':
    crypter = Crypter()  # Create crypter object
    app = GUI(crypter)  # Pass it to GUI object
    print('(+) Running')
