from pyfiglet import Figlet
import time
from datetime import datetime as dt
import os

from screen import screen_t
from snow import snow_t
from city import city_t

lastUpdateTime = 0
updateIntervalMillis = 500
goalDate = dt(2024, 1, 1)

width = 100
height = 25

if __name__ == "__main__":
    
    mainScreen = screen_t(width, height)
    snow = snow_t(width, height, 1)
    city = city_t()

    
    while True:
        if lastUpdateTime + updateIntervalMillis < time.time() * 1000:
            lastUpdateTime = time.time() * 1000
            # This if will execute every 10th of a second
            mainScreen.clear()

            
            mainScreen.copy(city.drawCity(), (0,3))

            car = [
                "                                  ______",
                "                                 /|_||_\`.__",
                "------------------------------- (   _    _ _\\ ---------------------------",
                "-  -  -  -  -  -  -  -  -  -  - =`-(_)--(_)-'  -  -  -  -  -  -  -  -  -  ",
                "--------------------------------------------------------------------------"
            ]
            mainScreen.copy(car, (5, 11))


            timeDifference = goalDate - dt.now()
            dateString = str(timeDifference).split(".")[0]
            string = Figlet(font='slant', width=width, ).renderText(dateString).split("\n")
            # Remove last index
            string.pop()
            mainScreen.copy(string, (0, 16))

        

            string = Figlet(font='slant', width=width, ).renderText("Happy New Years").split("\n")
            # Remove last index
            string.pop()
            mainScreen.copy(string, (0, 0))

            mainScreen.copy(snow.drawSnow(), (0,0))

            sign =["                   ",
                                    "  ______________   ",
                                    " |.------------.|  ",
                                    " ||            ||  ",
                                    " ||  Codedéx   ||  ",
                                    " || Hackathon  ||  ",
                                    " ||            ||  ",
                                    " ||____________||  ",
                                    " '------..------'  ",
                                    "        ||         ",
                                    "        ||         ",
                                    "      .-||-. _     ",
                                    "     '..---.- '    ",]
                           
            mainScreen.copy(sign, (80,4))
        
            mainScreen.output()






































            
    # print("Hello world losers")
    # ascii_banner = pyfiglet.figlet_format("Hello!!")
    # print(type(ascii_banner))

    # print(ascii_banner)
    # print(datetime.now().strftime('%H:%M:%S'))