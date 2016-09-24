
import initio, time

speed = 75

# Define pins for Pan/Tilt
pan = 0
tilt = 1
tVal = 0 # 0 degrees is centre
pVal = 0 # 0 degrees is centre

initio.init()

def doYes(tPan):
    initio.setServo(pan, pVal)
    time.sleep(0.2)

def doNo(tVal):
    initio.setServo(tilt, tVal)
    time.sleep(0.2)

# main loop
try:
    lastIRleft = initio.irLeft()
    lastIRright = initio.irRight()
    lastIRall = initio.irAll()
    while True:
        initio.forward(speed)
        distSonar = initio.getDistance()
        print "Sonar: ", int(distSonar)
        time.sleep(0.05)
        
        if (distSonar < 30) or (lastIRall):
            newIRleft = initio.irLeft()
            newIRright = initio.irRight()
            
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
    
