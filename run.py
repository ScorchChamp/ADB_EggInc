from EggInc import *
import time
import threading
from assets.Device import Device

device = Device()

location = device.getAllButtons("buttons/box_button")
print(location)

# while True:
#     try:
#         holdSpawnButtonWhileHatcheryWorking()
#         openBoxes()
#         # watchAdvertisements()
#         # research()
#         print("Cycle completed!")
#     except Exception as e:
#         print(e)
#         pass