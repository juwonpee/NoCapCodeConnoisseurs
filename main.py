from pyfiglet import Figlet
import time
from datetime import datetime as dt
from character import character_t

lastUpdateTime = 0
updateIntervalMillis = 100
goalDate = dt(2024, 1, 1)

character_t mainScreen
if __name__ == "__main__":
    while True:
        if lastUpdateTime + updateIntervalMillis < time.time() * 1000:
            lastUpdateTime = time.time() * 1000
            # This if will execute every 10th of a second
            timeDifference = goalDate - dt.now()
            dateString = str(timeDifference).split(".")[0]
            # print (dateString)

            figletRenderer = Figlet(font='slant', width=150)
            temp = figletRenderer.renderText(dateString)
            print(type(temp))
            print(figletRenderer.renderText(dateString))






































            
    # print("Hello world losers")
    # ascii_banner = pyfiglet.figlet_format("Hello!!")
    # print(type(ascii_banner))

    # print(ascii_banner)
    # print(datetime.now().strftime('%H:%M:%S'))