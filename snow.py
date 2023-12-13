from random import random

class snow_t:

    def __init__(self, width: int, height: int, snow_probability: int):
        self.screen = [[" "] * width for i in range(height)]
        self.width = width
        self.height = height
        self.snow_probability = snow_probability

    def clear(self):
        self.screen = [[" "] * self.width for i in range(self.height)]
    
    def drawSnow(self) -> []:
        # Loop for any snow characters
        for y in range(self.height-1, -1, -1):
            for x in range(self.width-1, -1, -1):
                if (self.screen[y][x] == "✻"):
                    self.screen[y][x] = " "
                    if (y+1 == self.height):    # If at bottom
                        self.screen[y][x] = "✻"
                    else:   # If not at bottom, check if below is snow
                        if (self.screen[y+1][x] == "✻"):
                            self.screen[y][x] = "✻"
                        else:
                            self.screen[y+1][x] = "✻"

        # Spawn snow randomly                
        probability = random()
        if (probability < self.snow_probability) :
            location = int(random() * self.width)
            self.screen[0][location] = "✻"

        returnArray = []
        for y in range(self.height):
            string = ""
            for x in range(self.width):
                string += self.screen[y][x]
            returnArray.append(string)
        return returnArray
