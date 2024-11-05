class XorMe:
    
    def __init__(self, what, xor_num):
        self.__crypto(what, xor_num)
        self.__s = self.__crypto(what, xor_num)
    
    def __crypto(self, what, xor_num):
        return ''.join(chr(ord(char) ^ xor_num) for char in what)
    
    def __str__(self):
        return self.__s

open_text = "You look like hell!"
xor_num = 3

encrypted_text = XorMe(open_text, xor_num)
print(str(encrypted_text))

decrypted_text = XorMe(str(encrypted_text), xor_num)
print(decrypted_text)