from sys import stdout
from Crypto.Util.strxor import strxor
ctx = [False for i in range(12)]
for i in range(12):
	fname = 'cipher_text_{}'.format(i+1)
	with open(fname) as f:
		ctx[i] = f.read().rstrip()

key = 'inikeynya!'
for c in ctx:
	stdout.write(strxor(key,c))


"""
flag := COMPFEST9{r3u51n9_th3_0n3_t1m3_p4d}
"""
