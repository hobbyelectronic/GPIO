#!/user/bi/env python
from Tkinter import *
from time import time
import RPi.GPIO as GPIO
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

Outputs=[18,16,15,13,12,11,23,22,19,21,24,26,7,3,5]
#initialise IO states
io0=0
io4=0
io1=0
io17=0
io21=0
io22=0
io10=0
io9=0
io11=0
io7=0
io8=0
io25=0
io24=0
io23=0
io18=0


R=0
for Port in Outputs:
	GPIO.setup(Port, GPIO.OUT)
	GPIO.output(Port, False)
	R=R + 1

GPIO.setup(7, GPIO.OUT)

def GPIO0() :
	global io0
	if io0==0:
		GPIO.output(3, True)
		B2 = Button(root, fg="Red",text="1",command=GPIO0).grid(row=1, column=6)
		io0=1
	else:
		GPIO.output(3, False)
		io0=0
		B2 = Button(root, fg="Black",text="0",command=GPIO0).grid(row=1, column=6)

	
def GPIO1() :
	global io1
	if io1==0:
		GPIO.output(5, True)
		B3 = Button(root, fg="Red", text="1",command=GPIO1).grid(row=2, column=6)
		io1=1
	else:
		GPIO.output(5, False)
		io1=0
		B3 = Button(root, fg="Black", text="0",command=GPIO1).grid(row=2, column=6)
	
	
	 
	
def GPIO4():
	global io4
	if io4==0:
		GPIO.output(7, True)
		B4 = Button(root, fg="Red",text="1",command=GPIO4).grid(row=3, column=6)
		io4=1
	else:
		GPIO.output(7, False)
		io4=0
		B4 = Button(root, fg="Black", text="0",command=GPIO4).grid(row=3, column=6)
		
	
def GPIO17() :
	global io17
	if io17==0:
		GPIO.output(11, True)
		B6 = Button(root, fg="Red", text="1",command=GPIO17).grid(row=5, column=6)
		io17=1
	else:
		GPIO.output(11, False)
		io17=0
		B6 = Button(root, fg="Black", text="0",command=GPIO17).grid(row=5, column=6)
	

	
def GPIO21() :
	global io21
	if io21==0:
		GPIO.output(13, True)
		B7 = Button(root, fg="Red", text="1",command=GPIO21).grid(row=6, column=6)
		io21=1
	else:
		GPIO.output(13, False)
		io21=0
		B7 = Button(root, fg="Black", text="0",command=GPIO21).grid(row=6, column=6)

	
def GPIO22() :
	global io22
	if io22==0:
		GPIO.output(15, True)
		B8 = Button(root, fg="Red", text="1",command=GPIO22).grid(row=7, column=6)
		io22=1
	else:
		GPIO.output(15, False)
		io22=0
		B8 = Button(root, fg="Black", text="0",command=GPIO22).grid(row=7, column=6)
	
	
def GPIO10() :
	global io10
	if io10==0:
		GPIO.output(19, True)
		B10 = Button(root, fg="Red", text="1",command=GPIO10).grid(row=9, column=6)
		io10=1
	else:
		GPIO.output(19, False)
		io10=0
		B10 = Button(root, fg="Black", text="0",command=GPIO10).grid(row=9, column=6)
	
def GPIO9() :
	global io9
	if io9==0:
		GPIO.output(21, True)
		B11 = Button(root, fg="Red", text="1",command=GPIO9).grid(row=10, column=6)
		io9=1
	else:
		GPIO.output(21, False)
		io9=0
		B11 = Button(root, fg="Black", text="0",command=GPIO9).grid(row=10, column=6)
	
	
def GPIO11() :
	global io11
	if io11==0:
		GPIO.output(23, True)
		B12 = Button(root, fg="Red", text="1",command=GPIO11).grid(row=11, column=6)
		io11=1
	else:
		GPIO.output(23, False)
		io11=0
		B12 = Button(root, fg="Black", text="0",command=GPIO11).grid(row=11, column=6)

def GPIO7() :
	global io7
	if io7==0:
		GPIO.output(26, True)
		B26 = Button(root, fg="Red", text="1",command=GPIO7).grid(row=12, column=7)
		io7=1
	else:
		GPIO.output(26, False)
		io7=0
		B26 = Button(root, fg="Black", text="0",command=GPIO7).grid(row=12, column=7)
	
def GPIO8() :
	global io8
	if io8==0:
		GPIO.output(24, True)
		B25 = Button(root, fg="Red", text="1",command=GPIO8).grid(row=11, column=7)
		io8=1
	else:
		GPIO.output(24, False)
		io8=0
		B25 = Button(root, fg="Black", text="0",command=GPIO8).grid(row=11, column=7)
	
	
def GPIO25() :
	global io25
	if io25==0:
		GPIO.output(22, True)
		B24 = Button(root, fg="Red", text="1",command=GPIO25).grid(row=10, column=7)			
		io25=1
	else:
		GPIO.output(22, False)
		io25=0
		B24 = Button(root, fg="Black", text="0",command=GPIO25).grid(row=10, column=7)
	
def GPIO24() :
	global io24
	if io24==0:
		GPIO.output(18, True)
		B22 = Button(root, fg="Red", text="1",command=GPIO24).grid(row=8, column=7)		
		io24=1
	else:
		GPIO.output(18, False)
		io24=0
		B22 = Button(root, fg="Black", text="0",command=GPIO24).grid(row=8, column=7)
	
	
def GPIO23() :
	global io23
	if io23==0:
		GPIO.output(16, True)
		B21 = Button(root, fg="Red", text="1",command=GPIO23).grid(row=7, column=7)		
		io23=1
	else:
		GPIO.output(16, False)
		io23=0
		B21 = Button(root, fg="Black", text="0",command=GPIO23).grid(row=7, column=7)
	

def GPIO18() :
	
	global io18
	if io18==0:
		GPIO.output(12, True)
		B19 = Button(root, fg="Red", text="1",command=GPIO18).grid(row=5, column=7)	
		io18=1
	else:
		GPIO.output(12, False)
		io18=0
		B19 = Button(root, fg="Black", text="0",command=GPIO18).grid(row=5, column=7)
		

root = Tk()
root.title("I/O Control")
root.geometry('200x375+200+200')

ioleft= ['3.3V','GPIO 0','GPIO 1','GPIO 4','-','GPIO 17','GPIO 21','GPIO 22','-','GPIO 10','GPIO 9', 'GPIO 11', '-']
ioright= ['5V','-','GND','TX','RX','GPIO 18','-','GPIO 23','GPIO 24','-','GPIO 25', 'GPIO 8', 'GPIO 7']

R=0
for label in ioleft:
	Label(text=label).grid(row=R,column=5)
	R=R + 1
	
R=0
for label in ioright:
	Label(text=label).grid(row=R,column=8)
	R=R + 1


B1 = Button(root, fg="Grey",text=" ").grid(row=0, column=6)
B2 = Button(root, fg="Black",text="0",command=GPIO0).grid(row=1, column=6)
B3 = Button(root, fg="Black", text="0",command=GPIO1).grid(row=2, column=6)
B4 = Button(root, fg="Black", text="0",command=GPIO4).grid(row=3, column=6)
B5 = Button(root, fg="Grey",text=" ").grid(row=4, column=6)
B6 = Button(root, fg="Black", text="0",command=GPIO17).grid(row=5, column=6)
B7 = Button(root, fg="Black", text="0",command=GPIO21).grid(row=6, column=6)
B8 = Button(root, fg="Black", text="0",command=GPIO22).grid(row=7, column=6)
B9 = Button(root, fg="Grey", text=" ").grid(row=8, column=6)
B10 = Button(root, fg="Black", text="0",command=GPIO10).grid(row=9, column=6)
B11 = Button(root, fg="Black", text="0",command=GPIO9).grid(row=10, column=6)
B12 = Button(root, fg="Black", text="0",command=GPIO11).grid(row=11, column=6)
B13 = Button(root, fg="Grey", text=" ").grid(row=12, column=6)
B14 = Button(root, fg="Grey", text=" ").grid(row=0, column=7)
B15 = Button(root, fg="Grey", text=" ").grid(row=1, column=7)
B16 = Button(root, fg="Grey", text=" ").grid(row=2, column=7)
B17 = Button(root, fg="Grey", text=" ").grid(row=3, column=7)
B18 = Button(root, fg="Grey", text=" ").grid(row=4, column=7)
B19 = Button(root, fg="Black", text="0",command=GPIO18).grid(row=5, column=7)
B20 = Button(root, fg="Grey", text=" ").grid(row=6, column=7)
B21 = Button(root, fg="Black", text="0",command=GPIO23).grid(row=7, column=7)
B22 = Button(root, fg="Black", text="0",command=GPIO24).grid(row=8, column=7)
B23 = Button(root, fg="grey", text=" ").grid(row=9, column=7)
B24 = Button(root, fg="Black", text="0",command=GPIO25).grid(row=10, column=7)
B25 = Button(root, fg="Black", text="0",command=GPIO8).grid(row=11, column=7)
B26 = Button(root, fg="Black", text="0",command=GPIO7).grid(row=12, column=7)


root.mainloop()