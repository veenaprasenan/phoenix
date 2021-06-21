from time import sleep
import sys
import RPi.GPIO as GPIO
import smtplib
import time
import re
import json
from urllib.request import urlopen
#for location
url='http://ipinfo.io/json'
response=urlopen(url)
data=json.load(response)
IP=data['ip']
city=data['city']
country=data['country']
region=data['region']
IPa='IP:{3}\nRegion:{0}\ncountry:{1}\ncity:{2}'.format(region,country,city,IP)
#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = 'phoenixproject000@gmail.com' #change this to match your gmail account
GMAIL_PASSWORD = 'phoenix#123'  #change this to match your gmail password

init =  "Initializing the Phoenix \n"
for x in init:
    print(x.upper(), end='')
    sys.stdout.flush()
    sleep(0.05)
def buzzer():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    buzzer=23
    GPIO.setup(buzzer,GPIO.OUT)
    while True:
        GPIO.output(buzzer,GPIO.HIGH)
        sleep(4)
        GPIO.output(buzzer,GPIO.LOW)
        sleep(1)
        break
def pr_check() :
    if pr in range(20,25) :
        print("LEVEL 1 ACCIDENT")
        sendTo = 'veenavellappally@gmail.com'
        emailSubject = "level1 Accident Detected!"
        emailContent = "Location::"+IPa
        emailContent = emailContent+ "....Aciident detected- Name: Micheal ,Address: Tarson Villa,MNC, Cochin,Kerala "
        sender.sendmail(sendTo, emailSubject, emailContent)
    elif pr in range(25,30) :
        print("LEVEL 2 ACCIDENT")
        sendTo = 'veenavellappally@gmail.com'
        emailSubject = "level2 Accident Detected!"
        emailContent = "Location::"+IPa
        emailContent = emailContent+ "....Aciident detected- Name: Micheal ,Address: Tarson Villa,MNC, Cochin,Kerala"
        sender.sendmail(sendTo, emailSubject, emailContent)
    elif pr in range(30,35) :
        print("LEVEL 3 ACCIDENT")
        sendTo = 'veenavellappally@gmail.com'
        emailSubject = "level 3 Accident Detected!"
        emailContent = "Location::"+IPa
        emailContent = emailContent+ "....Aciident detected- Name: Micheal  ,Address: Tarson Villa,MNC, Cochin,Kerala "
        sender.sendmail(sendTo, emailSubject, emailContent)
    elif pr in range(35,40) :
        print("LEVEL 4 ACCIDENT")
        sendTo = 'veenavellappally@gmail.com'
        emailSubject = "level 4 Accident Detected!"
        emailContent = "Location::"+IPa
        emailContent = emailContent+  "....Aciident detected- Name: Micheal  ,Address: Tarson Villa,MNC, Cochin,Kerala"
        sender.sendmail(sendTo, emailSubject, emailContent)
    else :
        print("LEVEL 5 ACCIDENT")
        sendTo = 'veenavellappally@gmail.com'
        emailSubject = "level 5 Accident Detected!"
        emailContent = "Location::"+IPa
        emailContent = emailContent+  "....Aciident detected- Name: Micheal  ,Address: Tarson Villa,MNC, Cochin,Kerala"
        sender.sendmail(sendTo, emailSubject, emailContent)

def sp_check() :
    if sp in range(50,75) :
        print("LEVEL 3 ACCIDENT")
        sendTo = 'veenavellappally@gmail.com'
        emailSubject = "level3 Accident Detected!"
        emailContent = "Location::"+IPa
        emailContent = emailContent+ "....Aciident detected- Name: Micheal  ,Address: Tarson Villa,MNC, Cochin,Kerala"
        sender.sendmail(sendTo, emailSubject, emailContent)
    elif sp in range(75,100) :
        print("LEVEL 4 ACCIDENT")
        sendTo = 'veenavellappally@gmail.com'
        emailSubject = "level4 Accident Detected!"
        emailContent = "Location::"+IPa
        emailContent = emailContent+ "....Aciident detected- Name: Micheal  ,Address: Tarson Villa,MNC, Cochin,Kerala"
        sender.sendmail(sendTo, emailSubject, emailContent)
    else :
        print ("LEVEL 5 ACCIDENT")
        sendTo = 'veenavellappally@gmail.com'
        emailSubject = "level5 Accident Detected!"
        emailContent = "Location::"+IPa
        emailContent = emailContent+  "....Aciident detected- Name: Micheal  ,Address: Tarson Villa,MNC, Cochin,Kerala"
        sender.sendmail(sendTo, emailSubject, emailContent)

def rate() :
    if sp >=50 :
        sp_check()
    else :
        pr_check()
def detect():
    print ("Accident detected")
    buzzer()
    rate()
    print("Email Sent")
    time.sleep(0.1)

class Emailer:
    def sendmail(self, recipient, subject, content):
        #Create Headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit
sender = Emailer()
while True:
    sp =int(input("Enter speed :"))
    pr =int(input("Enter pressure :"))
    if pr >= 20 :
        detect()
        break
