from multimethod import multimethod
import pygame

class NamedColor:
    @multimethod
    def __init__(self, color: pygame.Color, name: str):
        self.color = color
        self.name = name
    
    @multimethod
    def __init__(self, h: float, s: float, v: float, name: str):
        self.color = pygame.Color(0, 0, 0)
        self.color.hsva = (h * 360, s * 100, v * 100, 100)
        self.name = name
    
    @multimethod
    def __init__(self, code: str):
        params = code.split("\n")
        self.color = pygame.Color(0, 0, 0)
        self.color.hsva = (int(params[2]), int(params[3]), int(params[4]))
        self.name = params[1]

    
    def __str__(self):
        return "Begin Color\n" + self.name + "\n" + str(self.color.hsva[0]) + "\n" + str(self.color.hsva[1]) + "\n" + str(self.color.hsva[2]) + "\nEnd Color\n"
    

class Palette:
    @multimethod
    def __init__(self, name: str, colors: list):
        self.colors = colors
        self.name = name

    @multimethod
    def __init__(self, code: str):
        self.colors = list()
        params = code.split("\n")
        self.name = params[1]
        prev = 0
        for i in range(2, len(params) - 1):
            if params[i] == "Begin Color":
                prev = i
            elif params[i] == "End Color":
                self.colors.append(NamedColor('\n'.join(params[prev:i])))


    def __str__(self):
        toReturn = "Begin Palette\n" + self.name + "\n"
        for color in self.colors:
            toReturn += color.__str__()
        return toReturn + "End Palette\n"
    
    def __len__(self):
        return len(self.colors)

    def __getitem__(self, key):
        return self.colors[key]
    
    def __setitem__(self, key, value):
        self.colors[key] = value
    
    def __delitem__(self, key):
        del self.colors[key]
    
    def __iter__(self):
        return iter(self.colors)
    
    def __reversed__(self):
        return reversed(self.colors)
    
    def __contains__(self, item):
        return item in self.colors
    

