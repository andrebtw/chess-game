#!/usr/bin python3

import pygame
import json

from main_menu import *

# Pygame configuration


pygame.init() # Initialising pygame library
    
main_clock = pygame.time.Clock() # main_clock library assigned to the pygame clock

# Loads the JSON file with all the settings
with open("files/data/settings.json") as jsonSettings:
    jsonSettingsObject = json.load(jsonSettings)
    jsonSettings.close()

# Settings
fps = jsonSettingsObject['fps'] # Int : frames per second
width = jsonSettingsObject['width'] # Int : width resolution
height = jsonSettingsObject['height'] # Int : height resolution
fullscreen = jsonSettingsObject['fullscreen'] # Boolean : fullscreen or not

# Sets fullscreen if the fullscreen variable is True and vise versa
if fullscreen == False:
    screen = pygame.display.set_mode((width, height))
else:
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    
menu()