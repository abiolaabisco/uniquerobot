#!/usr/bin/python
import time

import RPi.GPIO as GPIO

import smtplib

import time
import logging

from time import strftime
LOG = "/var/log/main_cod.log"
logging.basicConfig(filename=LOG, filemode="w", level=logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
logging.getLogger("").addHandler(console)
logger = logging.getLogger(__name__)


from email.mime.text import MIMEText

USERNAME = "antivandals.alerts@gmail.com"

PASSWORD = "W***************************"

MAILTO  = "anti.vandals@abujaelectricity.com"

 
GPIO.setmode(GPIO.BOARD)
SENSOR1 = 16    
SENSOR2= 18
BUZZER = 15
SENSOR3= 31
SENSOR4= 29
 

logger.info ( "PIR Module Holding Time Test (CTRL-C to exit)")
GPIO.setup(SENSOR1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(SENSOR2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(SENSOR3, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(SENSOR4, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(BUZZER, GPIO.OUT)
 
Previous_State =0
Current_State = 0


try:

 

  logger.info  ("Waiting for PIR to settle ...")

 

  # Loop until PIR output is 0

  while GPIO.input(SENSOR1) or GPIO.input(SENSOR2) or GPIO.input(SENSOR3) or GPIO.input(SENSOR4)==1:

    Current_State  = 0

 

  print "  Ready"

  while True :
      
      # Read PIR state
      Current_State = GPIO.input(SENSOR1)or GPIO.input(SENSOR2) or  GPIO.input(SENSOR3) or GPIO.input(SENSOR4)
      if Current_State==1 and Previous_State==0:
         GPIO.output(BUZZER, False)
          
           # PIR is triggered
         start_time=time.time()
         logger.info  ("  Motion detected at mpape location! \n\n what else do u need to be applied'")
         while  GPIO.input(SENSOR1)or GPIO.input(SENSOR2) or GPIO.input(SENSOR3) or GPIO.input(SENSOR4):
           #GPIO.output(BUZZER, True)
           time.sleep(1)
          
         detect= strftime("%Y-%m-%d %H:%M:%S")
         msg = MIMEText('Motin was detected at detect')
         msg = MIMEText('Local decetion time was: '+detect)
         msg['Subject'] = 'Motion Has been Detected at mpape location /t what else do u need to be applied'
         #GPIO.output(BUZZER, True)
         msg['From'] = USERNAME
         msg['To'] = MAILTO
         
         server = smtplib.SMTP('smtp.gmail.com:587')
         server.ehlo_or_helo_if_needed()
         server.starttls()
         server.ehlo_or_helo_if_needed()
         server.login(USERNAME,PASSWORD)
         server.sendmail(USERNAME, MAILTO, msg.as_string())
         
         server.quit()
         # Record previous state
         Previous_State==1
       
      elif Current_State==0 and Previous_State==1:
           GPIO.output(15, False)
          # PIR has returned to ready state
           stop_time=time.time()
           logger.info  ("  Ready ",)
           elapsed_time=int(stop_time-start_time)
           logger.info ( " (Elapsed time : " + str(elapsed_time) + " secs)")
           Previous_State==0
      else:
         GPIO.output(15, False)

      

 

except KeyboardInterrupt:

  print "  Quit"

  # Reset GPIO settings

  GPIO.cleanup()



##    while True: 
##        time.sleep(0.1)
##        Previous_state = Current_state
##        Current_state =GPIO.input(SENSOR1)#and  (SENSOR2) or  (SENSOR3) and  (SENSOR4)
##    if Current_state != Previous_state:
##        new_state = "HIGH" if Current_state else "LOW"
##        print("GPIO pin %s is %s" % (SENSOR1, new_state))# and (SENSOR2, new_state)or(SENSOR3, new_state) and(SENSOR4, new_state))
##        
##        server  = smtplib.SMTP('smtp.gmail.com' , 578)
##        server.starttls()
##        server.login("abiolaabisco37@gmail.com", "adamawa14")
##
##        msg= 'intruder'
##        server.sendmail("abiolaabisco37@gmail.com", "abiolaabisco37@gmail.com", msg)
##        server.quit()
##        
              
