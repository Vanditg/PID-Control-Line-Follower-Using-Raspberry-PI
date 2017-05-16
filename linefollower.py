# IR line follower for 2 base

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

#IR SENSOR INPUTS

GPIO.setup(3, GPIO.IN)	#i                            
GPIO.setup(16,GPIO.IN)	#j
GPIO.setup(29,GPIO.IN)	#k
GPIO.setup(31,GPIO.IN)	#l
GPIO.setup(33,GPIO.IN)	#m

#MOTORS

#MOTOR	left
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

#MOTOR Right
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

#MOTOR OUTPUTS
GPIO.output(5,0)
GPIO.output(7,0)
GPIO.output(11,0)
GPIO.output(13,0)

#CONDITIONS
while True:
          i=GPIO.input(3)                         
          j=GPIO.input(16)
	  k=GPIO.input(29)
	  l=GPIO.input(31)
	  m=GPIO.input(33)

          if i==1 and j==1 and k==1 and l==1 and m==1:
                               
                print "backward",i,j,k,l,m
                GPIO.output(5,0)
                GPIO.output(7,1)
                GPIO.output(11,1)
                GPIO.output(13,1)

          elif i==1 and j==1 and k==0 and l==1 and m==1:

                print " forward  1 ",i,j,k,l,m
                GPIO.output(5,0)
                GPIO.output(7,1)
                GPIO.output(11,1)
                GPIO.output(13,0)

	  elif i==1 and j==0 and k==1 and l==1 and m==1:

                print " left ",i,j,k,l,m
                GPIO.output(5,1)
                GPIO.output(7,1)
                GPIO.output(11,1)
                GPIO.output(13,0)	

	  
	  elif i==0 and j==1 and k==1 and l==1 and m==1:

                print "sharp left",i,j,k,l,m
                GPIO.output(5,1)
                GPIO.output(7,0)
                GPIO.output(11,1)
                GPIO.output(13,0)

          elif i==0 and j==0 and k==0 and l==0 and m==1:
		
		print " sharpest left  turn ",i,j,k,l,m
                GPIO.output(5,1)
                GPIO.output(7,0)
                GPIO.output(11,1)
                GPIO.output(13,0)


	  elif i==1 and j==1 and k==1 and l==0 and m==1:

                print " right  turn ",i,j,k,l,m
                GPIO.output(5,0)
                GPIO.output(7,1)
                GPIO.output(11,1)
                GPIO.output(13,1)

	  elif i==1 and j==1 and k==1 and l==1 and m==0:

                print " sharp right",i,j,k,l,m
                GPIO.output(5,0)
                GPIO.output(7,1)
                GPIO.output(11,0)
                GPIO.output(13,1)

	  elif i==1 and j==0 and k==0 and l==0 and m==0:

                print " sharpest right turn",i,j,k,l,m
                GPIO.output(5,0)
                GPIO.output(7,1)
                GPIO.output(11,0)
                GPIO.output(13,1)

	  elif i==1 and j==0 and k==0 and l==1 and m==1:

                print " forward",i,j,k,l,m
                GPIO.output(5,0)
                GPIO.output(7,1)
                GPIO.output(11,1)
                GPIO.output(13,0)
	 
	  elif i==1 and j==0 and k==0 and l==0 and m==1:

	        print "forward",i,j,k,l,m
	 	GPIO.output(5,0)
                GPIO.output(7,1)
                GPIO.output(11,1)
                GPIO.output(13,0)

	  elif i==1 and j==1 and k==0 and l==0 and m==1:

	        print "forward",i,j,k,l,m
                GPIO.output(5,0)
                GPIO.output(7,1)
                GPIO.output(11,1)
                GPIO.output(13,0)

	  elif i==0 and j==0 and k==1 and l==1 and m==1:

                print " sharp left",i,j,k,l,m
                GPIO.output(5,1)
                GPIO.output(7,0)
                GPIO.output(11,1)
                GPIO.output(13,0)

	  elif i==1 and j==1 and k==1 and l==0 and m==0:

                print " sharp right",i,j,k,l,m
                GPIO.output(5,0)
                GPIO.output(7,1)
                GPIO.output(11,0)
                GPIO.output(13,1)

	  elif i==0 and j==0 and k==0 and l==0 and m==0: 

               print "backward ",i,j,k,l,m
               GPIO.output(5,1)
               GPIO.output(7,0)
               GPIO.output(11,0)
               GPIO.output(13,1)
          
	  elif i==0 and j==0 and k==0 and l==1 and m==1:

	       print "left side turn",i,j,k,l,m
               GPIO.output(5,1)
               GPIO.output(7,1)
               GPIO.output(11,1)
               GPIO.output(13,0)
#	       time.sleep(0.5)
#	       GPIO.output(5,0)
 #              GPIO.output(7,1)
  #             GPIO.output(11,0)
   #            GPIO.output(13,1)		
  
	  elif i==1 and j==1 and k==1 and l==0 and m==0:
              
	       print "sharp  right",i,j,k,l,m
               GPIO.output(5,1)
               GPIO.output(7,0)
               GPIO.output(11,1)
               GPIO.output(13,0)
	      

	  elif i==1 and j==1 and k==0 and l==0 and m==0:

	       print "right ",i,j,k,l,m
	       GPIO.output(5,0)
               GPIO.output(7,1)
               GPIO.output(11,1)
               GPIO.output(13,1)
               	       
	  elif i==0 and j==1 and k==1 and l==1 and m==1:
	 
	       print "sharp left",i,j,k,l,m
 	       GPIO.output(5,0)
               GPIO.output(7,1)
               GPIO.output(11,0)
               GPIO.output(13,1)	      
