# Requires the initio.py library that can be found here: http://4tronix.co.uk/initio/

import initio, time

speed = 75

# Define pins for Pan/Tilt
pan = 0
tilt = 1
tVal = 0 # 0 degrees is centre
pVal = 0 # 0 degrees is centre

initio.init()

# Moving tilt servo to simulate Yes (not used yet)
# @pVal - passing the tilt value
def doYes(tPan):
    # @tilt - passing the pan pin
    # @tVal - passing the pan value
    initio.setServo(pan, pVal)
    time.sleep(0.2)

# Moving pan servo to simulate No  
# @tVal - passing the tilt value
def doNo(tVal):
    # @tilt - passing the tilt pin
    # @tVal - passing the tilt value
    initio.setServo(tilt, tVal)
    time.sleep(0.2)

# main loop
try:
    # Sets values of infrared sensors
    lastIRleft = initio.irLeft()
    lastIRright = initio.irRight()
    lastIRall = initio.irAll()
    while True:
        # Sets motors forward with speed value
        initio.forward(speed)
        # Gets and prints distance from ultrasonic sensor
        distSonar = initio.getDistance()
        print "Sonar: ", int(distSonar)
        time.sleep(0.05)
        
        # If ultrasonic sensor is triggered or both infrared sensors are triggered...
        if (distSonar < 30) or (lastIRall):
            newIRleft = initio.irLeft()
            newIRright = initio.irRight()
            
            # If both infrared sensors are triggered, will backup creating an arc
            if (newIRleft != lastIRleft) and (newIRright != lastIRright):
                initio.stop()
                time.sleep(1.5)
                doNo(-20)
                doNo(20)
                doNo(-20)
                doNo(20)
                doNo(0)
                initio.turnReverse(100, 25)
                print "IR Both: "
                print "Backup"
                time.sleep(6)
                initio.stop()
                time.sleep(1.5)
                       
            # If right sensor is triggered, will turn left
            elif (newIRleft == lastIRleft) and (newIRright != lastIRright):
                initio.stop()
                time.sleep(1.5)
                doNo(-20)
                doNo(20)
                doNo(-20)
                doNo(20)
                doNo(0)
                initio.spinLeft(speed)
                print "IR Right: "
                print "Turn left"
                time.sleep(1.6)
                initio.stop()
                time.sleep(1.5)
                
            # If left sensor is triggered, will turn right
            elif (newIRleft != lastIRleft) and (newIRright == lastIRright):
                initio.stop()
                doNo(-20)
                doNo(20)
                doNo(-20)
                doNo(20)
                doNo(0)
                initio.spinRight(speed)
                print "IR Left: "
                print "Turn righ"
                time.sleep(1.6)
                initio.stop()
                time.sleep(1.5)
            
except KeyboardInterrupt:
    initio.cleanup()
    
