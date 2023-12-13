class city_t:
    def __init__(self):
        self.background = ["                        .|.                                                        ",
                           "                        | |                                               --       ",
                           "                        |'|            ._____            *        __*..* |  |      ",
                           "                ___    |  |            |.   |' .----.     _*   .-'   '-. |  |      ",
                           "        _    .-'   '-. |  |     .--'|  ||   | _|    |  .-'|  _.|  |    ||   '-__   ",
                           "     .-'|  _.|  |    ||   '-__  |   |  |    ||      |  |' | |.    |    ||       |  ",
                           "     |' | |.    |    ||       | |   |  |    ||      |  |  | |     |    ||       |  ",
                           "  ___|  '-'     '    ||       '-'   '-.'    '`      |__|  | |     |    ||       |  "]
        
        self.width = len(self.background[0])
        self.height = len(self.background)
        self.screen = [[" "] * self.width for i in range(self.height)]
        self.index = 0
    
    def drawCity(self) -> []:
        for y in range(self.height):
            for x in range(self.width):
                # make sure x+self.index is not out of bounds
                tempX = x+self.index
                while(tempX >= self.width):
                    tempX -= self.width
                self.screen[y][x] = self.background[y][tempX]
                if (self.index == self.width):
                    self.index = 0
        
        self.index += 1
        
        returnArray = []
        for y in range(self.height):
            string = ""
            for x in range(self.width):
                string += self.screen[y][x]
            returnArray.append(string)
        return returnArray