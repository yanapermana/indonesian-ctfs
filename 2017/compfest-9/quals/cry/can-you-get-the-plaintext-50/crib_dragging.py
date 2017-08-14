import string
from Crypto.Util.strxor import strxor

words = open('/asset/english-wordlist').read().rstrip()

ctx = [False for i in range(12)]
for i in range(12):
	fname = 'cipher_text_{}'.format(i+1)
	with open(fname) as f:
		ctx[i] = f.read().rstrip()


def pad(s, mix):
	while len(s) < len(mix):
		s+=s
	return s[0:len(mix)]

def rot(t):
	return t[1:]+t[0]

def nosym(t):
	s=''
	for c in t:
		if c in string.ascii_letters:
			s+=c
		else:
			s+=' '
	return s

def in_english(s):
	if s in words:
		return True
	return False

def noempty(L):
	Z = []
	for x in L:
		if x != '':
			Z.append(x)
	return Z

def cribdrag(t, mix):
	for i in xrange(len(t)):
		t = rot(t)
		t=pad(t, mix)
		s = strxor(t, mix)
		s = nosym(s)
		s = noempty(s.split(' '))
		for c in s:
			if len(c) > 4:
				if in_english(c):
					print c
				else:
					print c

if __name__ == '__main__':
	variant = [False for i in range(11)]
	for i in range(11):
		variant[i] = strxor(ctx[0], ctx[i+1])

	while 1:
		key = raw_input('Known: ')
		for i in range(11):
			print i
			cribdrag(key, variant[i])