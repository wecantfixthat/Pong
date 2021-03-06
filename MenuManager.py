import pygame
import pygame_menu
from pygame_menu.baseimage import BaseImage
import pygame_menu.font
from PONG import init_game
from pygame_menu import Theme

pygame.init()
surface = pygame.display.set_mode((1080, 720))
font = pygame_menu.font.FONT_NEVIS
globalName = ""
game_mode = "singleplayer"
game_diff_left = "easy"
game_diff_right = "medium"
LIGHT_BLUE = [17, 156, 216]
DARK_BLUE = [9, 78, 107]
WHITE = [255, 255, 255]
GRAY = [110, 110, 110]

class Menu():
    def draw_main_menu():
        myimage = pygame_menu.baseimage.BaseImage(
            './assets/new.jpg',
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
            )
        mytheme = pygame_menu.themes.THEME_DARK
        mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
        mytheme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
        mytheme.title_font = pygame_menu.font.FONT_NEVIS
        mytheme.background_color=(myimage)

                
        mainmenu = pygame_menu.Menu("Welcome to PONG!", 1080, 720,theme=mytheme)
        gamemode_sub_menu = Gamemode.create_gamemode_window()
        settings_sub_menu = SettingsMenu.createSettingsMenu()
        leaderboard_sub_menu = LeaderboardMenu.draw_leaderboard_menu()

        mainmenu.add.text_input("Enter name: ", default= "Player", onchange=Menu.TextVal)
        mainmenu.add.text_input("Enter name: ", default= "Player2", onchange=Menu.TextVal2)

        mainmenu.add.button('Play',  init_game)
        mainmenu.add.button('Game Options', gamemode_sub_menu)
        mainmenu.add.button('Settings', settings_sub_menu)
        mainmenu.add.button('Leaderboard', leaderboard_sub_menu)
        mainmenu.add.button("Quit", pygame_menu.events.EXIT)

        mainmenu.mainloop(surface)


    def TextVal(name): 
        print(name)
        file1 = open("name.txt","w")
        file1.write(name + " \n")

    def TextVal2(name2): 
        print(name2)
        file2 = open("name2.txt","w")
        file2.write(name2 + " \n")
class Gamemode():

    def __init__(self) -> None:
        pass
    def create_gamemode_window(gamemode_window_size=(1080,720)):
        surface = pygame.display.set_mode((gamemode_window_size))

        global gamememode_menu
        gamememode_menu = pygame_menu.Menu('Gamemode', gamemode_window_size[0], gamemode_window_size[1], theme=Gamemode.custom_theme())
        global choose_gamemode_label
        choose_gamemode_label = gamememode_menu.add.label('Choose Gamemode Below', 'choose_id', max_char=-1, font_size=45, background_color=DARK_BLUE, font_color=WHITE)
        global choose_gamemode_selector
        choose_gamemode_selector = gamememode_menu.add.selector('Gamemode:', [('SinglePlayer', 1), ('MultiPlayer', 2), ('Computer vs Computer', 3)], selector_id='select_id', onchange=Gamemode.set_gamemode, background_color=LIGHT_BLUE, font_color=WHITE, font_size=30)
        global next_screen_btn_gamemode
        next_screen_btn_gamemode = gamememode_menu.add.button('Next', Gamemode.update_display, button_id='next_id', background_color=LIGHT_BLUE, font_color=WHITE, font_size=35)
        global first_gamemode_quit_btn
        first_gamemode_quit_btn = gamememode_menu.add.button('Quit', pygame_menu.events.EXIT, button_id='quit_id', background_color=DARK_BLUE, font_color=WHITE, font_size=25)
        global first_gamemode_back_btn
        first_gamemode_back_btn = gamememode_menu.add.button('Back to Menu', pygame_menu.events.BACK,button_id='back_id',
                                            cursor=pygame_menu.locals.CURSOR_HAND)
        return gamememode_menu

    def set_gamemode(selected_item, pos):
        global game_mode
        game_mode = selected_item[0][0].lower()

    def choose_difficulty_left(selected_item, pos):
        global game_diff_left
        game_diff_left = selected_item[0][0].lower()

    def choose_difficulty_right(selected_item, pos):
        global game_diff_right
        game_diff_right = selected_item[0][0].lower()

    from pygame_menu import Theme

    def custom_theme():
        mytheme = Theme(background_color=(0, 0, 0, 0), # transparent background
                    title_background_color=(4, 47, 126),
                    title_font_shadow=True,
                    widget_padding=20,
                    widget_margin=(10,30))
        bg_img = pygame_menu.baseimage.BaseImage(
        image_path='assets/menu_background_1080x720.jpg',
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY
        )

        mytheme.background_color = bg_img
        return mytheme

    def start_game():
        Gamemode.reset_ui()
        init_game(game_mode, game_diff_left, game_diff_right, fps = 80)

    def update_display():
        if game_mode == 'singleplayer':
            global choose_diff_single_lbl
            choose_diff_single_lbl = gamememode_menu.add.label('Choose Difficulty Below', max_char=-1, font_size=45, background_color=DARK_BLUE, font_color=WHITE)
            global choose_diff_single_select
            choose_diff_single_select = gamememode_menu.add.selector('Computer Difficulty:', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=Gamemode.choose_difficulty_left, background_color=LIGHT_BLUE, font_color=WHITE, font_size=30)
            global choose_diff_single_start
            choose_diff_single_start = gamememode_menu.add.button('Start Game', Gamemode.start_game, background_color=DARK_BLUE, font_color=WHITE, font_size=30)
            global choose_diff_single_quit
            choose_diff_single_quit = gamememode_menu.add.button('Quit', pygame_menu.events.EXIT, background_color=GRAY, font_color=WHITE, font_size=25)
            global choose_diff_single_back
            choose_diff_single_back = gamememode_menu.add.button('Back to Menu', pygame_menu.events.BACK,
                                                cursor=pygame_menu.locals.CURSOR_HAND)
        elif game_mode == 'multiplayer':
            global multi_start
            multi_start = gamememode_menu.add.button('Start Game', Gamemode.start_game, background_color=DARK_BLUE, font_color=WHITE, font_size=30)
        else:
            global choose_diff_multi_lbl
            choose_diff_multi_lbl = gamememode_menu.add.label('Choose Difficulty Below', max_char=-1, font_size=45, background_color=DARK_BLUE, font_color=WHITE)
            global choose_diff_multi_select_left
            choose_diff_multi_select_left = gamememode_menu.add.selector('Left Paddle Difficulty:', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=Gamemode.choose_difficulty_left, background_color=LIGHT_BLUE, font_color=WHITE, font_size=30,align=pygame_menu.locals.ALIGN_LEFT)
            global choose_diff_multi_select_right
            choose_diff_multi_select_right = gamememode_menu.add.selector('Right Paddle Difficulty:',[('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=Gamemode.choose_difficulty_right, background_color=LIGHT_BLUE, font_color=WHITE, font_size=30,align=pygame_menu.locals.ALIGN_RIGHT)
            global choose_diff_multi_start
            choose_diff_multi_start = gamememode_menu.add.button('Start Game', Gamemode.start_game, background_color=DARK_BLUE, font_color=WHITE, font_size=30)
            global choose_diff_multi_quit
            choose_diff_multi_quit = gamememode_menu.add.button('Quit', pygame_menu.events.EXIT, background_color=GRAY, font_color=WHITE, font_size=25)
            global choose_diff_multi_back
            choose_diff_multi_back = gamememode_menu.add.button('Back to Menu', pygame_menu.events.BACK,
                                                cursor=pygame_menu.locals.CURSOR_HAND)

        if gamememode_menu.get_widget("choose_id") != None:
            gamememode_menu.remove_widget("choose_id")
            gamememode_menu.remove_widget("select_id")
            gamememode_menu.remove_widget("next_id")
            gamememode_menu.remove_widget("quit_id")
            gamememode_menu.remove_widget("back_id")

    def reset_ui():
        if game_mode == 'singleplayer':
            gamememode_menu.remove_widget(choose_diff_single_lbl)
            gamememode_menu.remove_widget(choose_diff_single_select)
            gamememode_menu.remove_widget(choose_diff_single_start)
            gamememode_menu.remove_widget(choose_diff_single_quit)
            gamememode_menu.remove_widget(choose_diff_single_back)

        elif game_mode == 'computer vs computer':
            gamememode_menu.remove_widget(choose_diff_multi_lbl)
            gamememode_menu.remove_widget(choose_diff_multi_select_left)
            gamememode_menu.remove_widget(choose_diff_multi_select_right)
            gamememode_menu.remove_widget(choose_diff_multi_start)
            gamememode_menu.remove_widget(choose_diff_multi_quit)
            gamememode_menu.remove_widget(choose_diff_multi_back)
        else:
            gamememode_menu.remove_widget(multi_start)


        if gamememode_menu.get_widget('choose_id') == None:
            global choose_gamemode_label
            choose_gamemode_label = gamememode_menu.add.label('Choose Gamemode Below', 'choose_id', max_char=-1, font_size=45, background_color=DARK_BLUE, font_color=WHITE)
            global choose_gamemode_selector
            choose_gamemode_selector = gamememode_menu.add.selector('Gamemode:', [('SinglePlayer', 1), ('MultiPlayer', 2), ('Computer vs Computer', 3)], selector_id='select_id', onchange=Gamemode.set_gamemode, background_color=LIGHT_BLUE, font_color=WHITE, font_size=30)
            global next_screen_btn_gamemode
            next_screen_btn_gamemode = gamememode_menu.add.button('Next', Gamemode.update_display, button_id='next_id', background_color=LIGHT_BLUE, font_color=WHITE, font_size=35)
            global first_gamemode_quit_btn
            first_gamemode_quit_btn = gamememode_menu.add.button('Quit', pygame_menu.events.EXIT, button_id='quit_id', background_color=DARK_BLUE, font_color=WHITE, font_size=25)
            global first_gamemode_back_btn
            first_gamemode_back_btn = gamememode_menu.add.button('Back to Menu', pygame_menu.events.BACK,button_id='back_id',
                                                cursor=pygame_menu.locals.CURSOR_HAND)
            
#class SettingsMenu:
global resolution
global fps
global theme
global score
global paddleSize


score = 3
resolution = (1080, 720)
fps = 60
theme = 1
paddleSize = "Small"

class SettingsMenu():
    def createSettingsMenu( resolution = (1080,720), fps = 60):
        
        pygame.display.set_caption("Settings")
        WINDOW = pygame.display.set_mode(resolution)
        


        #Creating a custom theme
        customTheme = pygame_menu.Theme(background_color=(0,0,0,0), title_background_color=(0,255,200), 
            title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
            widget_font=pygame_menu.font.FONT_BEBAS,
            title_font_color=(0,0,0),
            title_font=pygame_menu.font.FONT_BEBAS)

        

        global menu
        menu = pygame_menu.Menu("Settings", WINDOW.get_width(), WINDOW.get_height(), theme=customTheme)
        menu.add.selector("Screen Res: ", [("1080x720",1),("800x500",2),("440x280",3)], onchange=SettingsMenu.setResolution)
        menu.add.selector("FPS: ", [(" 60 ", 1), (" 120 ", 2), ("30", 3), ("1000", 4)], onchange=SettingsMenu.setFPS)
        menu.add.selector("Theme: ", [("Original",1), ("Mikey", 2), ("Nostalgia", 3),("Matthew", 4), ("Lil Cornely", 5)], onchange=SettingsMenu.setTheme)
        menu.add.selector('Score to Win: ',[('3',3),('7',7),('11',11),('15',15)], onchange=SettingsMenu.setScore)
        menu.add.selector("Paddle Size: ", [("Small", "Small"), ("Medium", "Medium"), ("Large", "Large"), ("bruh wha?", "wha?")], onchange=SettingsMenu.setPaddleSize)
        menu.add.button('Save', SettingsMenu.saveSettings)
        menu.add.button('Back to Menu', pygame_menu.events.BACK,
                                            cursor=pygame_menu.locals.CURSOR_HAND)
        
        return menu
        
    def setPaddleSize(selected, value):
        global paddleSize
        paddleSize = value

    def setTheme(selected, value):
        global theme
        theme = value

    def setResolution(selected, value):
        global resolution
        if(value == 1):
            resolution = (1080, 720)
        elif(value == 2):
            resolution = (800, 500)
        else:
            resolution = (440, 280)
        
    def setFPS(selected, value):
        global fps
        if(value == 1):
            fps = 60
        elif(value == 2):
            fps = 120
        elif(value == 3):
            fps = 30
        else:
            fps = 1000

    def setScore(selected,value):
        global score 
        if (value == 3):
            score = 3
        elif(value == 7):
            score = 7
        elif (value == 11):
            score = 11
        else:
            score = 15
        

    def saveSettings():
        print(resolution)
        pygame.display.set_mode(resolution)
        #print(f"menu height is now {menu.get_height()}")
        pygame_menu.menu.Menu('heh', resolution[0], resolution[1])
        SettingsMenu.updateMenuSize()
        init_game(gamemode = 'singleplayer', difficulty_left = 'medium', difficulty_right='medium', resolution= resolution, fps = fps, theme = theme, score = score, paddleSize = paddleSize)
        #updateMenuSize()
        #print(f"Changing to {resolution}")
            
    def updateMenuSize():
        menu._width = resolution[0]
        menu._height = resolution[1]
        menu.resize(resolution[0], resolution[1])
        print(menu.get_window_size())
        
        #menu._width = resolution[0]
        #menu._height = resolution[1]
        #menu._window_size = (resolution[0], resolution[1])
        
        #print(f"The menu size is from get: {menu.get_window_size()}")
        pass

import webbrowser
class LeaderboardMenu():
    def draw_leaderboard_menu():
        myimage = pygame_menu.baseimage.BaseImage(
            './assets/leaderboard_bg.jpg',
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
            )
        mytheme = pygame_menu.themes.THEME_DARK
        mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
        mytheme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
        mytheme.title_font = pygame_menu.font.FONT_NEVIS
        mytheme.background_color=(myimage)

                
        leaderboard_submenu = pygame_menu.Menu("Leaderboard", 1080, 720,theme=mytheme)
        url = leaderboard_submenu.add.url("http://127.0.0.1:5000", "Click To Open Leaderboard", font_color=WHITE, font_size=60,cursor=pygame_menu.locals.CURSOR_HAND)
        url.translate(0,-150)
        quit = leaderboard_submenu.add.button("Quit", pygame_menu.events.EXIT, font_color=WHITE, font_size=64,cursor=pygame_menu.locals.CURSOR_HAND)
        quit.translate(0,-150)
        back = leaderboard_submenu.add.button('Back to Menu', pygame_menu.events.BACK,
                                            cursor=pygame_menu.locals.CURSOR_HAND, font_color=WHITE, font_size=64)
        back.translate(0,-150)
        return leaderboard_submenu
Menu.draw_main_menu()