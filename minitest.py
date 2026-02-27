import pywhatkit as kit
import time
import pyautogui
import webbrowser
import keyboard
from datetime import datetime, timedelta

start_date = datetime(2004, 7, 1)
end_date = datetime(2006, 12, 31)
current_date = start_date
while current_date <= end_date:
    pyautogui.sleep(2)
    # pyautogui.click(x=1508, y=410)
    # username = "231SLS09020049"

    # keyboard.write(username)

    pyautogui.click(x=27, y=53)

    pyautogui.sleep(3)
    pyautogui.click(x=1142, y=765)
    pyautogui.click(x=1142, y=765)
    pyautogui.click(x=1142, y=765)
    pyautogui.sleep(1)

    password = current_date.strftime("%m/%d/%Y")
    keyboard.write(password)

    print(f"Trying with password: {password}")
    current_date += timedelta(days=1)

    pyautogui.sleep(1)
    pyautogui.click(x=1589, y=846)
    # pyautogui.click(x=1482, y=555)
    # pyautogui.click(x=1482, y=555)
    # pyautogui.sleep(1)

    # keyboard.press('ctrl+c')
    # pyautogui.sleep(1)
    # pyautogui.click(x=1689, y=559)
    # pyautogui.sleep(1)

    # keyboard.press('ctrl+v')

    
    # pyautogui.click(x=1578, y=631)


    # pyautogui.sleep(5)

    # pyautogui.click(x=1197, y=202)


    pyautogui.sleep(2)






