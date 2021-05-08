import os
import requests
import ctypes
import threading
import time
from colorama import Fore, init
import random

init()

errorCodes = [100, 101, 103, 201, 202, 203, 204, 205, 206, 300, 301, 302, 303, 304, 307, 308, 400, 401, 402, 403, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 422, 425, 426, 428, 431, 451, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]

def getProxy():
	global proxList
	global proxList2
	prox = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=US&ssl=no&anonymity=all")
	if prox.text == "You have reached your hourly maximum API requests of 750.":
		print("Please wait an hour before running this script again.")
		os.system('PAUSE')
		exit()
	proxyTxt = prox.text.splitlines()
	proxList = []
	for line in proxyTxt:
		proxList.append(line)
	prox2 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=US&ssl=yes&anonymity=all")
	if prox2.text == "You have reached your hourly maximum API requests of 750.":
		print("Please wait an hour before running this script again.")
		os.system('PAUSE')
		exit()
	proxyTxt2 = prox2.text.splitlines()
	proxList2 = []
	for line in proxyTxt2:
		proxList2.append(line)

def main():
	getProxy()
	with open("usernames.txt", "r") as f:
		global line
		lines = f.read().splitlines()
		for line in lines:
			thread = threading.Thread(target=checkUsername, daemon=True)
			thread.start()
			time.sleep(0.1)
		os.system('PAUSE >nul 2>&1')
		f.close()
		try:
			a.close()
		except Exception:
			pass

def checkUsername():
	global taken
	global available
	global total
	global randProxy
	global randProxySSL
	randProxy = random.choice(proxList)
	randProxySSL = random.choice(proxList2)
	username = line
	try:
		tiktokRequest = requests.get("https://tiktok.com/@{username}", proxies={"http": randProxy,"https": randProxySSL})
	except Exception as e:
		#print(e)
		return;
	if tiktokRequest.status_code == 200:
		taken += 1
		total += 1
		ctypes.windll.kernel32.SetConsoleTitleW("TikTok Username Checker | arshan.xyz | Available: " + str(available) +  " Taken: " + str(taken) + " Total: " + str(total))
		print(Fore.RED + f"[-] Username '{username}' is taken.")
	elif tiktokRequest.status_code == 404:
		available += 1
		total += 1
		ctypes.windll.kernel32.SetConsoleTitleW("TikTok Username Checker | arshan.xyz | Available: " + str(available) +  " Taken: " + str(taken) + " Total: " + str(total))
		print(Fore.GREEN + f"[+] Username '{username}' is available.")
		with open("available.txt", "a") as a:
			a.writelines(username + "\n")
	elif tiktokRequest.status_code == 429:
		total += 1
		ctypes.windll.kernel32.SetConsoleTitleW("TikTok Username Checker | arshan.xyz | Available: " + str(available) +  " Taken: " + str(taken) + " Total: " + str(total))
		print(Fore.YELLOW + "[!] You are being ratelimited.")
	elif tiktokRequest.status_code in errorCodes:
		total += 1
		ctypes.windll.kernel32.SetConsoleTitleW("TikTok Username Checker | arshan.xyz | Available: " + str(available) +  " Taken: " + str(taken) + " Total: " + str(total))
		print(Fore.YELLOW + "[!] An unexpected error has occured. Error Code: " + str(tiktokRequest.status_code))

if __name__ == "__main__":
	available = 0
	taken = 0 
	total = 0
	ctypes.windll.kernel32.SetConsoleTitleW("TikTok Username Checker | arshan.xyz | Available: " + str(available) +  " Taken: " + str(taken) + " Total: " + str(total))
	print(Fore.YELLOW + "[!] Some usernames may show has available but are actually banned.\nIf you are having issues with the checker try using restarting the script to get new proxies.")
	main()