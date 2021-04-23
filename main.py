import os
import requests
import ctypes
import threading
import time
from colorama import Fore, init
import random

init()

errorCodes = [100, 101, 103, 201, 202, 203, 204, 205, 206, 300, 301, 302, 303, 304, 307, 308, 400, 401, 402, 403, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 422, 425, 426, 428, 431, 451, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]

def main():
	with open("usernames.txt", "r") as f:
		global line
		lines = f.read().splitlines()
		for line in lines:
			thread = threading.Thread(target=checkUsername, daemon=True)
			thread.start()
			time.sleep(0.3)
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
	username = line
	tiktokRequest = requests.get("https://tiktok.com/@" + username)
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
	print(Fore.YELLOW + "[!] Some usernames may show has available but are actually banned.\nIf you are having issues with the checker try using a VPN.")
	main()