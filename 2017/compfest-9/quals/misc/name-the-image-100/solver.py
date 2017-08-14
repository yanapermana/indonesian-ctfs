import socket
import re
import requests
import json

api_key = 'acc_72808f4febc0105'
api_secret = 'c0964bf33ce723cdda020f9f129c14cf'

def get_middle_string(s, b, e):
	r = r"%s(.*?)%s" % (b,e)
	return re.findall(r,s)

while 1:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('tenkai.compfest.web.id', 43575)
	sock.connect(server_address)
	recv = sock.recv(512)
	sock.send('\n')

	for i in xrange(1000):
		recv = sock.recv(512)
		if 'COMPFEST9' in recv:
			print recv
			5/0
		try:
			imageUrl = get_middle_string(recv, 'image_url: ', '\nAnswer')[0]
			url = "https://api.imagga.com/v1/tagging?url={}".format(imageUrl)
			resp = requests.get(url, auth=(api_key, api_secret), verify=False)
			resp = json.loads(resp.text)
			tag = resp['results'][0]["tags"][0]["tag"]
			sock.send(tag+'\n')
		except:
			break

# flag := COMPFEST9{T4ke_th3_p1ctur3_anD_t4gs_W0l0lool0l0l0}