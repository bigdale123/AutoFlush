
from variables import *  #This line imports variable values from variables.py
import RPi.GPIO as GPIO	#These are just importing libraries I used
import time
import datetime

GPIO.setwarnings(False) #Sets GPIO Warnings to False

GPIO.setmode(GPIO.BOARD) #Sets GPIO mode to board

GPIO.setup(11, GPIO.OUT) #Tells the computer to set pin 11 to output mode

p = GPIO.PWM(11,50) #Sets up the PWM signal for operating the servo

p.start(0) #Starts the PWM on pin 11

Currently_Activated = 0 #Tells the program if the servo is currently able to flush
seconds = (60*Interval)-10 #Converts the interval variable to seconds variable, to be used for waiting between flushes

# So, i don't fully understand this function, but it's the backbone of making the servo work, so i'll explain the best I can
#	Servos use Pulse Width Modulation to know how much to turn, and that PWM is/can be measured in duty cycles,
#	So this function takes a user specified angle in degrees and converts it to a duty cycle.
#	Then, whenever we want to make to servo rotate, we just call this function rather than have all this for one rotation
def SetAngle(angle):
        duty = angle/18+.5
        GPIO.output(11, True)
        p.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(11, False)
        p.ChangeDutyCycle(0)

#This is the function called to flush the toilet. If a longer period between each rotation, change the 8 in the time.sleep function to however many seconds you want
#	NOTE: time.sleep here is not the time inbetween flushes. It is the time between each servo rotation, so it will rotate to 0 degrees, then wait 5 seconds to the toilet
#		To flush, then rotate back to the resting position.
def Flush():
        SetAngle(0)  # turn towards 0 degree
        time.sleep(8) # sleep 8 seconds
        SetAngle(180) # turn towards 180 degree

#The function that handles the hour checking
def HourStuff():
	global Currently_Activated
	if (currentDT.hour == Start_Hour):	#Tells the program that the servo is "Clocking In"
		Currently_Activated = 1
		Flush()
		time.sleep(seconds)
	elif (currentDT.hour > Start_Hour) and (currentDT.hour < End_Hour):  #The equivalent of being "On the Job"
		Currently_Activated = 1
		Flush()
	        time.sleep(seconds)
	elif (currentDT.hour == End_Hour) and (Currently_Activated == 1):	#The equivalent of "Clocking Out"
		Currently_Activated = 0
		Flush()
		time.sleep(seconds)

#This part loops forever, but no worries. It can be stopped by using "ps -ef | grep python" in the terminal, and then killing the Schedule.py Process.
while 1 != 0:
        currentDT = datetime.datetime.now() #Get the current DateTime variable structure
	if ((Mo == 1) and (currentDT.weekday() == 0)) or (Currently_Activated == 1): #If today is Monday (And toilet is set to flush that day) or Servo still on the job
		HourStuff()
	elif ((Tu == 1) and (currentDT.weekday() == 1)) or (Currently_Activated == 1): #If today is Tuesday (And toilet is set to flush that day) or Servo still on the job
		HourStuff()
	elif ((We == 1) and (currentDT.weekday() == 2)) or (Currently_Activated == 1): #If today is Wednesday (And toilet is set to flush that day) or Servo still on the job
                HourStuff()
	elif ((Th == 1) and (currentDT.weekday() == 3)) or (Currently_Activated == 1): #If today is Thursday (And toilet is set to flush that day) or Servo still on the job
                HourStuff()
	elif ((Fr == 1) and (currentDT.weekday() == 4)) or (Currently_Activated == 1): #If today is Friday (And toilet is set to flush that day) or Servo still on the job
               	HourStuff()
	elif ((Sa == 1) and (currentDT.weekday() == 5)) or (Currently_Activated == 1): #If today is Saturday (And toilet is set to flush that day) or Servo still on the job
                HourStuff()
	elif ((Su == 1) and (currentDT.weekday() == 6)) or (Currently_Activated == 1): #If today is Sunday (And toilet is set to flush that day) or Servo still on the job
                HourStuff()
