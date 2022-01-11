class States:  # Class used as enum type
    Decrypted, Encrypted = range(0, 2) # Decrypted = 0, Encrypted = 1

class Crypter:
    def __init__(self):
        self.states = States()  # Decrypted = 0, Encrypted = 1
        self.c_state = self.states.Decrypted  # Current state
        self.error = ''  # For error state

    def check_validity(self, m):
        if len(m) == 0:  # Check for empty input
            self.error = '(-) ERR: Empty input'
            return False
        if not m.isalpha():  # Check for non-alpha input
            self.error = '(-) ERR: Non-alphabetic input'
            return False
        return True  # Return true if all checks pass

    # Main encrypter / decrypter
    def __crypt(self, m):  # Algo: Just like for 10 numbers 2 is invert of 8, here, ascii(A) is invert of [26 - ascii(A)] = ascii(Z) (ord = ascii)
        return ''.join([chr(ord('a') + abs(ord(x) - ord('a') - 25)) if ord(x) >= ord('a') else chr(ord('A') + abs(ord(x) - ord('A') - 25)) for x in m])
    # Let's take dry run for a character say 'B' in string m:
    # ascii('B') is less than ascii('a') so segment after else is exec -> chr(ord('A') + abs(ord(x) - ord('A') - 25))
    # -> chr(65 + abs(66 - 65) - 25)
    # -> chr(65 + abs(-24))
    # -> chr(65 + 24) = chr(89) = 'Y'

    def encrypt(self, m):
        self.error = ''  # Reset error state
        if not self.check_validity(m):
            return None
        self.c_state = self.states.Encrypted  # Change state to Encrypted = 1
        return self.__crypt(m)  # Toggle cryption

    def decrypt(self, c):
        self.error = ''  # Reset error state
        if not self.check_validity(c):
            return None
        self.c_state = self.states.Decrypted  # Change state to Decrypted = 0
        return self. __crypt(c)  # Toggle cryption





