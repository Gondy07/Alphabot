from AlphaBot import AlphaBot
import time

Ab = AlphaBot()
Ab.setMotor(59,53.3)

try:
        # primo track
        for i in range(7):
                Ab.forward()
                time.sleep(1.3)
                Ab.left()
                time.sleep(0.11)

        Ab.left()
        time.sleep(0.4)
        Ab.forward()
        time.sleep(1)
        Ab.left()
        time.sleep(0.125)


        # secondo track
        for i in range(10):
                Ab.forward()
                time.sleep(1.3)
                Ab.left()
                time.sleep(0.11)


except KeyboardInterrupt:
        GPIO.cleanup()
