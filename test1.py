from gpiozero import MotionSensor, LED, Buzzer

led = LED(14)
pir = MotionSensor(17)

led.off()

while True:
    pir.wait_for_motion()
    print("Motion detected")
    led.on()
    pir.wait_for_no_motion()
    led.off()
    print("Motion Stopped")

