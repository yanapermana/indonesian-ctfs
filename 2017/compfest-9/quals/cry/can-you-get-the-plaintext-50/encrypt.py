plain_text_file = open('plain_text', 'r')
key_file = open('key', 'r')

plain_text = plain_text_file.read()
key = key_file.read()
panjang = len(plain_text)

if panjang % len(key) != 0:
    for i in range(len(key) - (panjang % len(key))):
        plain_text = plain_text + " "

for i in range(len(plain_text) / len(key)):
    cipher_text_file = open('cipher_text_' + str(i + 1), 'w')
    for j in range(i * len(key), (i + 1) * len(key)):
        cipher_text_file.write(chr(ord(plain_text[j]) ^ ord(key[j - i * len(key)])))
    cipher_text_file.close()

plain_text_file.close()
key_file.close()