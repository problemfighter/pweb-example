from time import sleep

from ppy_common import PyCommon

print("Test Run")


for i in range(10):
    response = PyCommon.is_started("test_one", 5)
    print(f"response: {response}")
    sleep(1)
