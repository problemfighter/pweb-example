from time import sleep

from ppy_file_text import FileUtil

print("Test Run")


for i in range(10):
    response = FileUtil.is_started("test_one", 5)
    print(f"response: {response}")
    sleep(1)
