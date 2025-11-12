from AlphaBot import AlphaBot
import time

Ab = AlphaBot()
Ab.setMotor(35,35)

try:
        while True:
                left, right = Ab.read_sensors()
                if left == 0 or right == 0:
                        Ab.stop()
                        Ab.backward()
                        time.sleep(1)
                        Ab.stop()
                        if left == 0:
                                Ab.right()
                                time.sleep(0.7)
                        if right == 0:
                                Ab.right()
                                time.sleep(0.7)


                else:
                        Ab.forward()

except KeyboardInterrupt:
        GPIO.cleanup()