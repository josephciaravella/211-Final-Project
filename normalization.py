from math import sqrt

RED = [0.732532, 0.117098, 0.150371]
BLUE = [0.194934, 0.246254, 0.558812]
GREEN = [0.138353, 0.512719, 0.348928]
#BLACK = [0.468148, 0.307427,0.224424]


def normalize(rgb):
    sum = rgb[0]+rgb[1]+rgb[2]
    red = rgb[0]/sum
    green = rgb[1]/sum
    blue = rgb[2]/sum

    return [red, green, blue]


def color_dist(rgb, norm_rgb):
    return sqrt((norm_rgb[0] - rgb[0])**2 + (norm_rgb[1] - rgb[1])**2 + (norm_rgb[2] - rgb[2])**2 )

def determine_color(rgb):
    red_dist = color_dist(rgb, RED)
    blue_dist = color_dist(rgb, BLUE)
    green_dist = color_dist(rgb, GREEN)

    min_dist = red_dist
    color = 'Red'
    

    if green_dist < min_dist:
        min_dist = green_dist
        color = 'Green'

    if blue_dist < min_dist:
        min_dist = blue_dist
        color = 'Blue'

    if min_dist > 0.25:
        color = 'Wood'
        
    return color

    