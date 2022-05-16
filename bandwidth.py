from pywinauto.application import Application
from pywinauto.keyboard import SendKeys
import pywinauto
import time
import schedule
import datetime


def limitOn():
    app = Application().connect(process=5828)
    win = app.window(title='OBS 23.2.1 (64-bit, windows) - Profile: Untitled - Scenes: Untitled')

    win.SetFocus()
    win.TypeKeys('{VK_F12}')
    print(datetime.datetime.now())
    print('***ENABLED AND BROADCASTING***')
def limitOff():
    app = Application().connect(process=5828)
    win = app.window(title='OBS 23.2.1 (64-bit, windows) - Profile: Untitled - Scenes: Untitled')

    win.SetFocus()
    win.TypeKeys('{VK_F12}')
    print(datetime.datetime.now())
    print('***DISABLED AND NOT BROADCASTING***')



schedule.every().monday.at("01:00").do(limitOff)
schedule.every().monday.at("17:00").do(limitOn)
schedule.every().tuesday.at("01:00").do(limitOff)
schedule.every().tuesday.at("17:00").do(limitOn)
schedule.every().wednesday.at("01:00").do(limitOff)
schedule.every().wednesday.at("17:00").do(limitOn)
schedule.every().thursday.at("01:00").do(limitOff)
schedule.every().thursday.at("17:00").do(limitOn)
schedule.every().friday.at("01:00").do(limitOff)
schedule.every().friday.at("12:00").do(limitOn)


isRunning = True

while True:
    schedule.run_pending()
    time.sleep(1)