from pprint import pprint
import sys
import random
import time
import pyautogui


#import win32gui	
#whatTodo



def main_loop():

	pyautogui.PAUSE = 0
	#vars
	status 	= 0
	i 		= 0
	swap	= ''
	mode 	= ''
	list0	= ["Aatrox","Ahri","Akali","Alister","Amumu","Anivia","Annie","Ashe","Aurelion Sol","Azir","Bard","blitzcrank","Brand","Braum","Caitlyn","Camille","Cassiopeia","Cho'Gath","Corki","Darius","Diana","Dr. Mundo","Draven","Ekko","Elise","Evelynn","Ezreal","Fiddlesticks","Fiora","Fizz","Galio","Gankplank","Garen","Graves","Hecarim","Heimerdinger","Illaoi","Irelia","Ivern","Janna","Jarvan IV.","Jax","Jayce","Jhin","Jinx","Kalista","Karma","Khartus","Kassadin","Katarina","Kayle","Kennen","kha'Zix","Kai'Sa","Kindred","Kled","Kog'Maw","LeBlanc","Lee Sin","Leona","Lissandra","Lucian","Lulu","Lux","Malphite","Malzhar","Maokai","Master Yi","Kayn","Miss Fortune","Mordekaiser","Morgana","Name","Nasus","Nautilus","Nidalee","Nocturne","Nunu","Olaf","Orianna","Ornn","Pantheon","Poppy","Rakan","Rek'Sai","Renekton","Rengar","Riven","Rumble","Ryze","Sejuani","Shaco","Shen","Shyvana","Singed","Sion","Sivir","Sona","Soraka","Swain","Syndra","Tahm'kench","Taric","Teemo","Thresh","Tristana","Trundle","Tryndamere","Twisted Fate","Twitch","Udyr","Urgot","Varus","Vayne","Vi","Viktor","Vladimir","Volibear","Warwick","Wukong","Xerath","Xin Zhao","Yasou","Yorick","Zac","Zed","Ziggs","Zilean","Zyra","Zoe"]
	
	global mouseposX
	global mouseposY

	if 'mouseposX' in vars() or 'mouseposX' in globals():
		lol = 1
	else:
		mouseposX = 200

	if 'mouseposY' in vars() or 'mouseposY' in globals():
		lol = 2		
	else:
		mouseposY = 100

	mouseposX = int(mouseposX)
	mouseposY = int(mouseposY)

	screenWidth, screenHeight = pyautogui.size()

	mode = input("What schould I do?\n\nWrite 'help' to show every possible command! \n")
	time.sleep(1)


	#normal operation -> no need to swap things
	if mode == "normal":
		#win32gui.ShowWindow(HWND, win32con.SW_RESTORE)
		#win32gui.SetWindowPos(HWND,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
		#win32gui.SetWindowPos(HWND,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
		#win32gui.SetWindowPos(HWND,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE

		list1 = list0
		length= len(list0)
		pyautogui.moveTo(mouseposX, mouseposY)

		for cname in list1:
			pyautogui.click()
			pyautogui.typewrite(cname, interval=0)
			pyautogui.press('enter')
			print(cname)

		#reset vars
		status  = 0
		list1   = []
		mode    = ''

	elif mode == "random":
		list2 = list0

		#win32gui.ShowWindow(HWND, win32con.SW_RESTORE)
		#win32gui.SetWindowPos(HWND,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
		#win32gui.SetWindowPos(HWND,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
		#win32gui.SetWindowPos(HWND,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE
		pyautogui.moveTo(mouseposX, mouseposY)

		while len(list2) != 0:
			status = 1
			i = random.randint(0,len(list2))
			i = i-1
			swap = list2.pop(i)
			pyautogui.click()
			pyautogui.typewrite(swap, interval=0)
			pyautogui.press('enter')

		#reset vars
		status	=0
		mode	=''

	elif mode == "help":
		print("\nFunctions:\n")
		print("normal    	 -> writing lol names from a to z\n")
		print("random    	 -> writing the names in random order\n")
		print("setpos		 -> save the actual mousepostion as new coodinates for the chatbox\n")
		print("setpos manually   -> enter new X and Y Coordinates to locate the chatbox\n")
		print("testcursor	 -> test the saved coordinates onscreen\n")
		print("To close the programm just use [Strg + C]\n")

		#reset vars
		status	=0
		mode	=''

	elif mode == "testcursor":
		print("Cursor gesetzt!\n")
		pyautogui.moveTo(mouseposX, mouseposY)
		print(mouseposX)
		print(mouseposY)
		print(mouseposY)

		mousestat = 1
		status	=0
		mode	=''

	elif mode == "setpos manually":
		mouseposX = input("Set mouse X in pixel !\n")
		mouseposY = input("Set mouse Y in pixel !\n")

		#reset vars
		status	=0
		mode	=''

	elif mode == "setpos":
		x, y = pyautogui.position()
		mouseposX = x
		mouseposY = y
	
		print("new x position = "+str(x))
		print("new y position = "+str(y))

		#reset vars
		status	=0
		mode	=''

	else:
		print("I'm just a random error occuring because my dev sucks :-)")

if __name__ == '__main__':
	while 1:
		try:
			main_loop()

		except KeyboardInterrupt:

			print >> sys.stderr, 'Exiting by user request.'

			sys.exit(0)