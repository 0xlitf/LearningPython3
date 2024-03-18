import asyncio
import time

from mqttwrapper.hbmqtt_backend import run_script


async def setup_db():
    return {
        "query_db": query_db
    }


async def query_db(value):
    # pretend this is some slow DB query, for example.
    print(f"value: {value}")
    await asyncio.sleep(3)
    return f'{value}'


async def callback(topic, payload, query_db):
    db_result = await query_db(payload)
    print("Received payload {} on topic {}, db result: {}".format(payload, topic, db_result))


def main():
    run_script(callback, broker="mqtt://10.10.5.138",
               topics=["sys/device/zc_control", "sys/device/zc_control_result", "sys/device/zc_config",
                       "sys/device/zc_robot_status"], context_callback=setup_db)
    i = 0
    while True:
        print(f"{i}")
        i += 1
        time.sleep(1)


if __name__ == "__main__":
    main()
