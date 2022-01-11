from gui import GUI
from crypter import Crypter

if __name__ == '__main__':
    crypter = Crypter()
    app = GUI(crypter)
    print('(+) Running')
