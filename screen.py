import os

class screen_t:
    def __init__(self, width: int, height: int):
        self.screen = [[" "] * width for i in range(height)]
        self.width = width
        self.height = height

    def clear(self):
        self.screen = [[" "] * self.width for i in range(self.height)]
        os.system('cls' if os.name == 'nt' else 'clear')

    def copy(self, array: [], location:(int, int)):
        # make every string same size
        for i in range(len(array)):
            array[i] = array[i].ljust(self.width, " ")

        for y in range(0, len(array)):
            for x in range(0, len(array[0])):
                # Check if out of bounds
                currentCopyPosition = (x + location[0], y + location[1])
                if (currentCopyPosition[0] >= self.width or currentCopyPosition[1] >= self.height):
                    continue
                
                # If within bounds, check if empty space
                if (array[y][x] == " "):
                    continue
                
                # else copy over
                self.screen[currentCopyPosition[1]][currentCopyPosition[0]] = array[y][x]


    def output(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if (self.screen[y][x] == ""):
                    print(" ")
                else:
                    print(self.screen[y][x], end="")
            
            # newline
            print("")