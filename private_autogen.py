import os
import sys
from time import sleep
import threading
from private_data import *

exiting = False

def input_thread():
    global exiting
    input()
    exiting = True
    sys.exit(0)

threading.Thread(None, input_thread, daemon=True).start()

count: int = 0
last: dict[str, float] = {}

while True:
    while True:
        if exiting:
            sys.exit(0)
        current: dict[str, float] = {}
        for root, _, files in os.walk("Assets/"):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.exists(file_path):  # and file != "pack.mcmeta"
                    current[file_path] = os.path.getmtime(file_path)
        if current != last:
            break
        if count % 15 == 0:
            print(".", end="", flush=True)
        sleep(1)
        count += 1

    count = 0
    last = current.copy()

    data.run()
