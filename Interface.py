import os
import time
os.system('clear')
Mo = 0
Tu = 0
We = 0
Th = 0
Fr = 0
Sa = 0
Su = 0
print("---------------------------------")
print("------ AutoFlush Interface ------")
print("---------------------------------")
print
print
Days = raw_input("Please input what days the toilet should flush: ") #Gets user choice
Days = Days.lower() #Converts string typed by user to all lowercase
i = 0
while i < len(Days):  #This While loop find out what days the user has typed and then manipulates boolean variables accordingly
	First_Letter = Days[i]
	Second_Letter = Days[i+1]
	Day = First_Letter + Second_Letter
	if(Day == "mo"):
		Mo = 1
	elif(Day == "tu"):
		Tu = 1
	elif(Day == "we"):
		We = 1
	elif(Day == "th"):
		Th = 1
	elif(Day == "fr"):
		Fr = 1
	elif(Day == "sa"):
		Sa = 1
	elif(Day == "su"):
		Su = 1
	i = i+2
Start_Hour = input("When should the Toilet start flushing? (You must type the answer in 24 hour format)  ")
End_Hour = input("When should the Toilet Stop Flushing? (You must type the answer in 24 hour format)  ")
Interval = input("How much time should there be between flushes (Please answer in minutes)  ")
print
print("All Done! This program will now kill the current instance of Schedule.py, Overwrite the old values with new ones, then Restart Schedule.py")
time.sleep(5)
#Kill current instance of Schedule.py
os.system("ps -ef | grep 'python Schedule.py' | grep -v grep | awk '{print $2}' | xargs kill")
#Check to see if Variables.txt is a file. If yes, Delete and Replace. If not, create new.
exists = os.path.isfile('/home/pi/variables.py')
if exists:
	os.remove('variables.py')
	print("Variables.py already exists. Replacing...")
else:
	print("variables.py does not already exist. Creating new one...")
#Write new variables file
file = open("variables.py","w")
file.write("Mo = "+str(Mo)+"\n")
file.write("Tu = "+str(Tu)+"\n")
file.write("We = "+str(We)+"\n")
file.write("Th = "+str(Th)+"\n")
file.write("Fr = "+str(Fr)+"\n")
file.write("Sa = "+str(Sa)+"\n")
file.write("Su = "+str(Su)+"\n")
file.write("Start_Hour = "+str(Start_Hour)+"\n")
file.write("End_Hour = "+str(End_Hour)+"\n")
file.write("Interval = "+str(Interval)+"\n")
file.close()

#start new instance of Schedule.py
os.system("python Schedule.py &") #Starts Schedule.py in the background
