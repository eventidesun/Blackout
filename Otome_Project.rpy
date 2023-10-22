# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define G = Character("Gilbert")


#DEFINE IMAGES

image Gilbert:
    "bidenj.png"
    zoom 3

image Gilbert1:
    "bidenj.png"
    zoom 1
image Gilbert2:
    "bidenj.png"
    zoom 0.5
 
image rye field:
    "rye field.jpeg"
    zoom 3.5

# SCREEN CENTER
init:
    $ screen_center = Position(xpos=0.5, ypos=0.7)

# SHAKE
init:
    transform shaking:
        linear 0.1 xoffset -2 yoffset 2 
        linear 0.1 xoffset 3 yoffset -3 
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 0 yoffset 0
        repeat

init:
    transform shaking1:
        linear 0.1 xoffset -5 yoffset 5 
        linear 0.1 xoffset 7 yoffset -7 
        linear 0.1 xoffset 5 yoffset -5
        linear 0.1 xoffset -7 yoffset 7
        linear 0.1 xoffset 5 yoffset 5
        repeat


# The game starts here.

label start:

    #PROLOGUE BEGINS

    "The field of rye is vast, you see no end to it. The rye ears are so hefty with grains they bow to each other. Yet they are not entwined, each stem carefully avoiding another."
    "The rye grows high, enveloping you in its waves as if you are stranded in the middle of the ocean, with your head showing just above its surface."

    # Show a background
    scene rye field

    "The light travels through the bronze of the field as the sun slowly moves up, and the tear-like morning dew, cold and crisp, drips silently from the stems and disappears in the rich dark dirt beneath."
    "The wind carries around whispers of the rye ears, and you hear voices. But they are muffled, unclear. You are not sure if you can distinguish any words from it."

    "Do they talk about you? Do they judge you? Or encourage?"
    "The unfamiliar gazes focused on you feel like damp clothes sticking to your body. It is not pleasant, but the feeling soothes you, almost grounds you even."
    # Show an image
    show Gilbert with fade

    "The rye ears are turning with the gust of wind, and then you see him. A figure of pure white, all blinding light and shining gold. It has his hair, his lopsided smile."

    scene rye field at shaking
    show Gilbert1 at screen_center

    "You start running towards it, but the rye is too thick. It slows you down, grasps you with its prickly body. Each step feels heavier than the next one, until you eventually decide to give up. So much struggle - and what for, in the end?"

    scene rye field at shaking1
    show Gilbert2 at screen_center

    "You drown in the field of bronze, the rye holding you tight, until the figure on the horizon is swallowed up by more rye."

    scene black 
    "You wake up."

    # This ends the game.

    return
