import time
import threading
import lgpio
from constants.config import DIR_PIN, PWM_PIN, ACTUATOR_FULL_TRAVEL_TIME, PWM_FREQUENCY, PWM_PERIOD

gpio_handle = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(gpio_handle, DIR_PIN)
lgpio.gpio_claim_output(gpio_handle, PWM_PIN)

pwm_running = False
actuator_state = None
lock = threading.Lock()

def motor_pwm(speed):
    global pwm_running
    pwm_running = True
    duty = speed / 100.0

    def loop():
        while pwm_running:
            lgpio.gpio_write(gpio_handle, PWM_PIN, 1)
            time.sleep(PWM_PERIOD * duty)
            lgpio.gpio_write(gpio_handle, PWM_PIN, 0)
            time.sleep(PWM_PERIOD * (1 - duty))

    threading.Thread(target=loop, daemon=True).start()


def motor_off():
    global pwm_running
    pwm_running = False
    lgpio.gpio_write(gpio_handle, PWM_PIN, 0)


def extend_actuator():
    global actuator_state
    with lock:
        if actuator_state == "extending":
            return
        actuator_state = "extending"

    print("ACTUATOR: EXTENDING")

    def run():
        lgpio.gpio_write(gpio_handle, DIR_PIN, 1)
        motor_pwm(100)
        time.sleep(ACTUATOR_FULL_TRAVEL_TIME)
        motor_off()
        global actuator_state
        with lock:
            actuator_state = None

    threading.Thread(target=run, daemon=True).start()


def retract_actuator():
    global actuator_state
    with lock:
        if actuator_state == "retracting":
            return
        actuator_state = "retracting"

    print("ACTUATOR: RETRACTING")

    def run():
        lgpio.gpio_write(gpio_handle, DIR_PIN, 0)
        motor_pwm(100)
        time.sleep(ACTUATOR_FULL_TRAVEL_TIME)
        motor_off()
        lgpio.gpio_write(gpio_handle, DIR_PIN, 1)
        global actuator_state
        with lock:
            actuator_state = None

    threading.Thread(target=run, daemon=True).start()
