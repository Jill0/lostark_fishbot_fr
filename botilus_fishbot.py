import os
import win32com.client
import pyautogui
import cv2
import time
import random
import numpy as np

shell = win32com.client.Dispatch("WScript.Shell")
os.chdir(os.getcwd())

# GLOBAL VAR
GLOBAL_TIMEOUT = 25
GLOBAL_FISH_CAUGHT = 0
GLOBAL_FISH_KEY = "e"
GLOBAL_BAIT_KEY = "f"
GLOBAL_NASSE_KEY = "g"
GLOBAL_MINIGAME_KEY = "z"
#

print("Début de la pêche dans 5 secondes ! (Botilus#0001)")
print("Un facteur d'échec est intégré pour éviter que des réussites et un ban assuré.")
time.sleep(5)
print("et zeeeeeeeeeeeeeeee parti !!!")
time.sleep(5)
for i in range(1000):
	# LOCAL VAR
	LOCATE_FISH_BAIT = None
	LOCATE_FISH_EXCLAMATION = None
	LOCATE_FISH_FOOD = None
	LOCATE_FISH_NASSPUT = None
	LOCATE_FISH_NASSOPEN = None
	LOCATE_MINIGAME_READY = None
	LOCATE_VITAL_EMPTY = None
	timeout = GLOBAL_TIMEOUT
	#
	shell.SendKeys(GLOBAL_FISH_KEY)
	time.sleep(2)
	LOCATE_VITAL_EMPTY = pyautogui.locateOnScreen('vitalempty.png', confidence=0.9)
	if (LOCATE_VITAL_EMPTY != None):
		print("VOUS N'AVEZ PLUS D'ENERGIE VITALE !")
		time.sleep(30)
		continue
	time.sleep(3)

	LOCATE_FISH_BAIT = pyautogui.locateOnScreen('bait.png', confidence=0.6)
	if (LOCATE_FISH_BAIT != None):
		while (LOCATE_FISH_EXCLAMATION == None) and (timeout > 0):
			LOCATE_FISH_EXCLAMATION = pyautogui.locateOnScreen('fishcaught.png', confidence=0.6)
			timeout -= 0.1

		if (LOCATE_FISH_EXCLAMATION != None):
			time.sleep(random.randint(5,10)/10)
			shell.SendKeys(GLOBAL_FISH_KEY)
			time.sleep(7)
			LOCATE_FISH_EXP = pyautogui.locateOnScreen('fishexp.png', confidence=0.6)
			if (LOCATE_FISH_EXP != None):
				GLOBAL_FISH_CAUGHT += 1
				print("Nombre de poissons attrapés : {}".format(GLOBAL_FISH_CAUGHT))
				LOCATE_MINIGAME_READY = pyautogui.locateOnScreen('minigame_ready.png', confidence=0.5)
			time.sleep(1)

		if(LOCATE_MINIGAME_READY == None):
			LOCATE_MINIGAME_READY = pyautogui.locateOnScreen('minigame_ready.png', confidence=0.5)
		if(LOCATE_MINIGAME_READY != None):
			time.sleep(5)
			shell.SendKeys(GLOBAL_MINIGAME_KEY)
			time.sleep(3)
			MINIGAME_TIMEOUT = 20
			while (MINIGAME_TIMEOUT > 0):
				MINIGAME_TIMEOUT -= 0.1
				MINIGAME_EXCELLENT = pyautogui.locateOnScreen('minigame_excellent.png', confidence=0.3)
				if (MINIGAME_EXCELLENT == None):
					for i in range(10):
						shell.SendKeys(" ")

		LOCATE_FISH_EXCLAMATION = pyautogui.locateOnScreen('fishcomp.png', confidence=0.9)
		if (LOCATE_FISH_EXCLAMATION != None):
			print("Utilisation de la compétence Appât")
			shell.SendKeys(GLOBAL_BAIT_KEY)
			time.sleep(7)

		LOCATE_FISH_NASSPUT = pyautogui.locateOnScreen('nassput.png', confidence=0.8)
		if (LOCATE_FISH_NASSPUT != None):
			print("Pose de la nasse")
			shell.SendKeys(GLOBAL_NASSE_KEY)
			time.sleep(7)

		LOCATE_FISH_NASSOPEN = pyautogui.locateOnScreen('nassopen.png', confidence=0.8)
		if (LOCATE_FISH_NASSOPEN != None):
			print("Récupération de la nasse")
			shell.SendKeys(GLOBAL_NASSE_KEY)
			time.sleep(7)
	else:
		print("Hameçon non détecté, je recommence dans 10s...")
	time.sleep(10)
        

