import time

from mqttwrapper import run_script


def callback(topic, payload):
    print("Received payload {} on topic {}".format(payload, topic))


def blocking():
    run_script(callback, broker="mqtt://10.10.5.138",
               topics=["sys/device/zc_control", "sys/device/zc_control_result", "sys/device/zc_config",
                       "sys/device/zc_robot_status"])


def non_blocking_callback(topic, payload):
    print("non blocking mode: Received payload {} on topic {}".format(payload, topic))


def non_blocking():
    run_script(non_blocking_callback, broker="mqtt://10.10.5.138",
               topics=["sys/device/zc_control", "sys/device/zc_control_result", "sys/device/zc_config",
                       "sys/device/zc_robot_status"], blocking=False)
    while True:
        print("Alive and kicking")
        time.sleep(1)


if __name__ == "__main__":
    # blocking()
    non_blocking()
