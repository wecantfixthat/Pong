import pygame
import pygame_menu
from pygame_menu.baseimage import BaseImage
import pygame_menu.font
from PONG import init_game
from Gamemode import create_gamemode_window
from SettingsMenu import createSettingsMenu


pygame.init()
surface = pygame.display.set_mode((1080, 720))
font = pygame_menu.font.FONT_NEVIS
globalName = ""
class menu():
        pygame.init()
        myimage = pygame_menu.baseimage.BaseImage(
        './assets/new.jpg',
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
        )
        mytheme = pygame_menu.themes.THEME_DARK
        mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
        mytheme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
        mytheme.title_font = pygame_menu.font.FONT_NEVIS
        mytheme.background_color=(myimage)

        def TextVal(name): 
                globalName= name
                file1 = open("name.txt","w")
                file1.write(name + " \n")
        def getName():
                return globalName
        mainmenu = pygame_menu.Menu("Welcome to PONG!", 1080, 720,theme=mytheme)
        mainmenu.add.text_input("Enter name: ", default= "Player", onchange=TextVal)
        mainmenu.add.button('Play',  init_game)
        mainmenu.add.button('Game Options', create_gamemode_window)
        mainmenu.add.button('Settings', createSettingsMenu)
        mainmenu.add.button("Leaderboard")
        mainmenu.add.button("Quit", pygame_menu.events.EXIT)

        mainmenu.mainloop(surface)

