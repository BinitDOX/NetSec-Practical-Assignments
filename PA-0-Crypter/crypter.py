class States:
    Decrypted, Encrypted = range(0, 2)

class Crypter:
    def __init__(self):
        self.states = States()
        self.c_state = self.states.Decrypted
        self.error = ''

    def check_validity(self, m):
        if len(m) == 0:
            self.error = '(-) ERR: Empty input'
            return False
        if not m.isalpha():
            self.error = '(-) ERR: Non-alphabetic input'
            return False
        return True

    def __crypt(self, m):  # Main encrypter / decrypter
        return ''.join([chr(ord('a') + abs(ord(x) - ord('a') - 25)) if ord(x) >= ord('a') else chr(ord('A') + abs(ord(x) - ord('A') - 25)) for x in m])

    def encrypt(self, m):
        self.error = ''
        if not self.check_validity(m):
            return None
        self.c_state = self.states.Encrypted
        return self.__crypt(m)

    def decrypt(self, c):
        self.error = ''
        if not self.check_validity(c):
            return None
        self.c_state = self.states.Decrypted
        return self. __crypt(c)





