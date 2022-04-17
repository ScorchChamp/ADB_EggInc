from ScorchScrc import *
import ScorchScrc
import time

        
def slideScreen(x1, y1, x2, y2, time):  device.shell(f'input touchscreen swipe {x1} {y1} {x2} {y2} {time}')
def tapScreen(x, y):                    device.shell(f'input touchscreen tap {x} {y}')

def holdSpawnButton(time = 1000):
    x, y = getLocationOfButton('spawn_button')
    slideScreen(x, y, x, y, time)

def isHatcheryAvailable():
    refreshScreenshot(device)
    x, y = getLocationOfButton('hatchery_start')
    print(x,y)
    if x:
        pxl_array = np.array(Image.open('screen.png'), dtype=np.uint8)[int(y)][int(x):int(x)+10]
        print(pxl_array)
        return not colorInPixelArray([240,13,13,255], pxl_array)
    return False
     
def holdSpawnButtonWhileHatcheryWorking():
    print("Spawning chickens!")
    while isHatcheryAvailable():
        ScorchScrc.hold_button_time = ScorchScrc.hold_button_time + 1
        holdSpawnButton(ScorchScrc.hold_button_time*1000)
    ScorchScrc.hold_button_time = ScorchScrc.hold_button_basis

def clickButton(button_name):
    x,y = getButton(button_name)
    if x:
        tapScreen(x,y)
    else:
        raise Exception ("Button not found!")

def getButton(button_name):
    refreshScreenshot(device)
    return getLocationOfButton(button_name)

def getNextAdvertisement():         return getButton('advertisement_button')
def getWatchButton():               return getButton('watch_button')
def getCollectButton():             return getButton('collect_button')
def getBoxButton():                 return getButton('box_button')
def getAvailableResearchButton():   return getButton('research_available_button')
def getUnavailableResearchButton(): return getButton('research_unavailable_button')
def getResearchButton():            return getButton('research_button')

def openBoxes():
    print("Checking for boxes!")
    x,y = getBoxButton()
    if x:
        print("Opening box!")
        tapScreen(x, y)
        time.sleep(1)
        x, y = getCollectButton()
        tapScreen(x, y)

def watchAdvertisements():
    print("Checking for videos!")
    while getNextAdvertisement():
        x, y = getNextAdvertisement()
        if x:
            print("Watching video!")
            tapScreen(x, y)
            time.sleep(2)
            x, y = getWatchButton()
            tapScreen(x, y)
            time.sleep(60)
            closeVideo()
            time.sleep(5)
            closeVideo()

def closeVideo():
    tapScreen(1030, 80)

def research():
    print("Starting research!")
    x,y = getResearchButton()
    if x:
        tapScreen(x, y)
        time.sleep(2)
        available_x, available_y = getAvailableResearchButton()
        unavailable_x, unavailable_y = getUnavailableResearchButton()
        if not available_x and not unavailable_x:
            slideScreen(500,500,500,1600,200)
        for y in range(1,10):
            available_x, available_y = getAvailableResearchButton()
            unavailable_x, unavailable_y = getUnavailableResearchButton()
            if available_x or unavailable_x:
                for i in range(0,5):
                    for y in range(400, 1800, 100):
                        tapScreen(available_x, y)
            slideScreen(500,1300,500,450,2000)
    tapScreen(x, y)
    