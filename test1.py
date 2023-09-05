from gpiozero import MotionSensor

def motion_sensor_update(PIN):
    pir = MotionSensor(PIN)
    while True:
        pir.wait_for_motion()
        print("Motion detected")
        pir.wait_for_no_motion()
        print("Motion Stopped")

