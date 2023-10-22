# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kasumi")
define g = Character("Goro")

#Define Images
image Kasumi happy:
    "kasumi happy.png"
    zoom 3

image Kasumi ouch:
    "kasumi ouch.png"
    zoom 3

image Kasumi oh:
    "Kasumi shocked.png"
    zoom 3

image Kasumi sad:
    "Kasumi Dejected.png"
    zoom 3

image Goro happy:
    "Goro smile.png"
    zoom 3


image Goro norm:
    "Goro norm.png"
    zoom 3

image School:
    "school.jpeg"
    zoom 4
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene School
label bgm:
    play music "audio/bgm persona.mp3" fadein 1.0 volume 0.5

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Kasumi happy

    # These display lines of dialogue.

    k "Look I managed to code!"
    show Kasumi ouch 
    k "But we need to make our own characters, I don't wanna get sued..."
    show Kasumi oh 
    k "Is that senpai?"
    show Kasumi oh at left 
    show Goro norm at right with moveinright
    g "Oh Kasumi hmm, what are you doing here?"
menu:
    "Playing flute":
        jump choices1_a
    "Crying":
        jump choices1_b

label choices1_a:
    show Goro happy
    g "omg euphonium outslays!"
    jump choices1_common
label choices1_b:
    show Goro happy
    g "lol wtf ur a loser"
    jump choices1_common

label choices1_common:
    show Kasumi sad
    k "sigh..."
    # This ends the game.
    return

