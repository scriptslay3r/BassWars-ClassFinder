print("Welcome to Bass Wars")
print("Let's See What Class You're in!")

speakerArea = input("What is the surface area of your subwoofers? ")
if speakerArea == "?":

	speakerSize = input("What size are your speakers? ")
	
	speakerAmount = input("How many " + speakerSize + " inch speakers do you have? ")
	
	speakerShape = input("Are they (R)ound or (S)quare ")
	if speakerShape == "R": 
	
		totalSize = int(speakerSize) * int(speakerAmount)
	
		speakerArea = totalSize * 3.14
	

		"""
		## 4inch = 12 in^2 
		## 6 inch = 28 in^2
		## 8 inch = 50 in^2
		## 10 inch = 78 in^2
		## 12 inch = 113 in^2
		## 15 inch = 176 in^2
		## 18 inch = 254 in^2
		
		"""
		print(" You're speaker area is " + str(speakerArea) + "in\u00b2")
	elif speakerShape == "S" :
		totalSize = speakerSize * speakerAmount 
	
		speakerArea = totalSize * totalSize
	
		"""
		## 4 inch = 16 in^2 
		## 6 inch = 36 in^2
		## 8 inch = 64 in^2
		## 10 inch = 100 in^2
		## 12 inch = 144 in^2
		## 15 inch = 225 in^2
		## 18 inch = 324 in^2
		
		"""
		print(" You're speaker area is " + str(speakerArea) + "in\u00b2")
	else: 
		print("Please type 'R' for Round speakers or 'S' for Square speakers ")

#else:
	##speakerArea = int(speakerArea)
	
portArea = input("What is the port area of the enclosure? ")

bassValue = int(speakerArea) + int(portArea)


power = input("How many watts push your Subwoofer(s)? ")

print("The Bass Value is " + str(bassValue) + "in\u00b2 and is powered with " + str(power) + " Watts")

if int(bassValue) < 351 and int(power) < 5001:
	bassClass = "Stealth"

	print("Your class is " + str(bassClass))
elif int(bassValue) < 351 and int(power) > 5000:
	##upgrade due to power
	bassClass = "Monster"
	print("Your class is " + str(bassClass))

elif  351 < int(bassValue) < 750 and 5000 < int(power) < 10000:
	bassClass = "Monster"
	print("Your class is " + str(bassClass))

elif  351 < int(bassValue) < 750 and int(power) > 10000:
	#Upgrade due to power
	bassClass = "Chaos"
	print("Your class is " + str(bassClass))

elif 751 < int(bassValue) < 1300 and 10000 <  int(power) < 20000:
	bassClass = "Chaos"
	print("Your class is " + str(bassClass))

elif 751 < int(bassValue) < 1300 and int(power) > 20000:
	#upgrade due to power
	bassClass = "Beast"
	print("Your class is " + str(bassClass))

elif 1301 < int(bassValue) < 2000 and  20001 < int(power) < 40000:
	bassClass = "Beast"
	print("Your class is " + str(bassClass))

elif 1301 < int(bassValue) < 2000 and int(power) > 40000:
	#Upgrade due to power
	bassClass = "Legendary"
	print("Your class is " + str(bassClass))

elif 2000 < int(bassValue) and int(power) > 40000:
	bassClass = "Legendary"
	print("Your class is " + str(bassClass))
else:
	print("Whoops maybe its a weird set up, we need a person to take a look!")
""" if bass value = 0 - 350 AND power = 0 - 5000 class = Stealth
	if bass value = 0= 350 AND power > 5000 Class = Monster
	if bass value = 351-750 AND power = 5001 - 10000 watts class = Monster
	if bass value = 351-750 AND power > 10000 Class = Chaos
	if bass value = 751-1300 AND power = 10001 - 20000 class = Chaos
	if bass value = 751-1300 AND power > 20001 class = Beast 
	if bass value = 1301-2000 AND power = 20001 - 40000 class = Beast
	if bass value = 2000+ AND power = 40001 + Class = Legendary 
"""
