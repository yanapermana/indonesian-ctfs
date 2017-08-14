import socket
import sys
import string

libs = {}
charset = string.ascii_letters + string.digits + '{_}'

for char in charset:
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_address = ('tenkai.compfest.web.id', 10086)
		print >>sys.stderr, 'connecting to %s port %s' % server_address
		sock.connect(server_address)
		sock.recv(4096)
		sock.send('{}\n'.format(char))
		recv = sock.recv(4096)
		key = recv.rstrip()
		libs[key] = char
	except:
		pass

ctx = 'hahahaCHIM!hahahahahahahahahahahahahahahaCHIM!hahahahahahahahahahahahahaCHIM!hahahahahahahahahahahahahahahahaCHIM!hahahahahahaCHIM!hahahahahaCHIM!hahahahahahahahahahahahahahahahahahahaCHIM!hahahahahahahahahahahahahahahahahahahahaCHIM!hahahahahahahahahahaduhmehhahaCHIM!hahahahahahahahahahahahahahahahahahahahahahahahahaCHIM!hahahahaduhmehhahaCHIM!hahahahahahahahahahahahahahahahahahahahahahahahahaCHIM!hahahahaduhmehhahahahahahaCHIM!hahahahahahahahahahahahahahahahahahaCHIM!hahahahahahahahahahahahahahahaCHIM!hahahahahahahahahahahahahaCHIM!mehhahahahahahahahahahahahahahahahahahahaCHIM!hahahahahahahahahahahahahahahahaCHIM!hahahahahahahahahahahahahahahahahahaCHIM!hahahahahahahahahahahahahahahaCHIM!hahahahahahahahahahahahahahahahahahahahahaCHIM!hahahahahahahahahahahahahahahahahahahahaCHIM!meh'
ctx = ctx.replace('!','! ')
ctx = ctx.replace('duh','duh ')
ctx = ctx.replace('meh','meh ')
ctx = ctx.split(' ')

for c in ctx:
	try:
		sys.stdout.write(libs[c])
	except:
		sys.stdout.write(' ')

# flag := 'COMPFEST9{BY3_BY3_FROM_SPROUT}'