from Paddle import Paddle
import pygame

def get_move_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    """Return "up" or "down", depending on which way the paddle should go to
    align its centre with the centre of the ball
   
    Keyword arguments:
    paddle_frect -- a rectangle representing the coordinates of the paddle
                    paddle_frect.pos[0], paddle_frect.pos[1] is the top-left
                    corner of the rectangle
                    paddle_frect.size[0], paddle_frect.size[1] are the 
                    dimensionsof the paddle along the x and y axis, 
                    respectively
   other_paddle_frect --
                    a rectangle representing the opponent paddle. It is 
                    formattedin the same way as paddle_frect
   
   ball_frect --    a rectangle representing the ball. It is formatted in the 
                    same way as paddle_frect
   table_size --    table_size[0], table_size[1] are the dimensions of the table,
                    along the x and the y axis respectively
   
   The coordinates look as follows:
   
            0             x
            |------------->
            |
            |             
            |
        y   v
    """          
   
    if paddle_frect.pos[1]+paddle_frect.size[1]/2 < ball_frect.pos[1]+ball_frect.size[1]/2:
        return "down"
    else:
        return "up"



def get_move_player_right():
    """Return "up" or "down", depending on which key the player presses. 
    In singleplayer mode, the user uses the up and down arrow keys. In multiplayer mode, the left player used the 'w' and 's' keys, 
    and the right player uses the up and down keys"""          
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        return "down"
    elif keys[pygame.K_UP]:
        return "up"

def get_move_player_left():
    """Return "up" or "down", depending on which key the player presses. 
    In singleplayer mode, the user uses the up and down arrow keys. In multiplayer mode, the left player used the 'w' and 's' keys, 
    and the right player uses the up and down keys"""          
    keys = pygame.key.get_pressed()

    if keys[pygame.K_s]:
        return "down"
    elif keys[pygame.K_w]:
        return "up"

def get_paddle_difficulty(difficulty, fRect, paddle_size, max_angle, facing, isAI):
    easy_speed = 4
    medium_speed = 5
    hard_speed = 6

    if difficulty == "easy":
        return Paddle(fRect, paddle_size, easy_speed, max_angle, facing, isAI)
    elif difficulty == "medium":
        return Paddle(fRect, paddle_size, medium_speed, max_angle, facing, isAI)
    else:
        return Paddle(fRect, paddle_size, hard_speed, max_angle, facing, isAI)