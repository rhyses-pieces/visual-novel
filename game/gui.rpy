# NOTE:
# Default Ren'Py theme code is moved to gui_scripts/renpyDefault.rpy.

init offset = -2

init python:
    gui.init(1920, 1080)

#~~~~~~~~~~~~~~~~~~~~#
# Customize Your UI! #
#~~~~~~~~~~~~~~~~~~~~#

#############
# Game Info #
#############

# Name of the game, which shows up in your window, etc.
define config.name = _("Fade")

## The version of the game.
define config.version = "1.0"

## The name of the developer.
define gui.developer_name = "Moon Tea Creative"

## Name of your build. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.
define build.name = "Fade"

## Save directory. This controls where Ren'Py will place the save files.
## The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
## Linux: $HOME/.renpy/<config.save_directory>
##
## Change this to the name of your game, with some random numbers for good
## measure (in case someone else makes a game of the same name).

define config.save_directory = "Fade-1511469406"

# Your website. This will be clickable via the "web" icon on the main menu
# in the lower corner.
define gui.developer_site = "http://lunachaili.com"

###########
# Visuals #
###########

# The opacity of the menus' overlay.
define gui.overlay_opacity = 0.7

# The image for your main menu.
define gui.mm_background = "gui/mm_background.jpg"

# The logo of your game on the main menu.
define gui.mm_logo = "gui/logo.png"

# The ycenter of the logo (how far down the screen it is). Recommended is 0.25.
define gui.mm_logoy = 0.25


#################
# Sound Effects #
#################

# INSTRUCTIONS:
# Replace the file paths with files to your desired sound effect.

# Sound when a button is hovered.
define guisfx_button_hover = "sfx/silence_sec.ogg"

# Sound when a button is clicked.
define guisfx_button_click = "sfx/silence_sec.ogg"

# Sound when a warning pops up, like when deleting a file, etc.
define guisfx_button_warn = "sfx/silence_sec.ogg"

# Music for the main menu.
define config.main_menu_music = "music/silence_min.ogg"

# If you don't want voices, set this to False
define config.has_voice = False

###############
# Font Styles #
###############

# INSTRUCTIONS:
# Fonts on the other screens will automatically change
# when you change the fonts in this category.

## Name text: font
define gui.advname_font_face = "gui/Nunito 700.ttf"

## Name text: size
define gui.advname_font_size = 34

## Name text: color
define gui.advname_font_color = '#ffffff'

# Name text: kerning. This is the amount of pixels between each letter.
define gui.advname_font_kerning = 3

## Name text: uppercase. Change to False if you don't want auto uppercase.
init -10 python:
    varAdvNameUppercase = True

## Dialogue text: font
define gui.adv_font_face = "gui/Nunito 300.ttf"

## If you have a different font face for Bold, replace the following fonts.
## Put your normal font where "Nunito 300" is, and your bold font where
## "Nunito 700" is.
init python:
    config.font_replacement_map["gui/Nunito 300.ttf", True, False] = ("gui/Nunito 700.ttf", False, False)

## If you have a different font face for Italic, replace the following fonts.
    #config.font_replacement_map["gui/Nunito 300.ttf", False, True] = ("gui/Nunito 300 italic.ttf", False, False)

## Dialogue text: size
define gui.adv_font_size = 34

## Dialogue text: color
define gui.adv_font_color = '#ffffff'

## Dialogue text: line leading. The amount of pixels between each line.
define gui.adv_font_line = 1


##############
# CG Gallery #
##############

# If you don't want a CG gallery, set this to false.
define gui.has_cg = True

# INSTRUCTIONS:
# The CG gallery is a special Ren'Py screen and requires some
# custom coding for you to add in your own CGs.

# You will also have to create thumbnails that are 334x188
# for your CGs to show properly.

# You can edit the screen under gui_scripts/screenGallery.rpy.

# Check the Ren'Py documentation for the image gallery here:
# https://www.renpy.org/doc/html/rooms.html


##############
# Music Room #
##############

# If you don't want a music room, set this to false.
define gui.has_mr = False


###################
# Custom Messages #
###################

# INSTRUCTIONS:
# Replace the following strings with your own messages, if desired.

init python:

    ## Text shown when the log is empty.
    gui.message_log_empty =     "The log is empty. Play more."

    ## General confirm text.
    gui.message_confirm =       "Are you sure?"

    ## Confirm text when deleting save.
    gui.message_deletesave =    "Are you sure you want to delete this save?"

    ## Confirm text when overwriting save.
    gui.message_overwrite =     "Are you sure you want to overwrite this save?"

    ## Confirm text when loading save.
    gui.message_load    =       "Loading will lose unsaved progress. Are you sure?"

    ## Confirm text when quitting.
    gui.message_quit    =       "Are you sure you want to quit?"

    ## Confirm text when going to the main menu.
    gui.message_mainmenu =      "Returning to the main menu will lose unsaved progress. Are you sure?"

    ## Confirm text when slow skipping -- doesn't do anything with this template.
    gui.message_slowskip =      "Are you sure you want to begin skipping?"

    ## Confirm text when skipping to next choice.
    gui.message_fastskip =      "Are you sure you want to skip dialogue to the next choice?"

    ## Confirm text when ending a replay -- doesn't do anything with this template.
    gui.message_replay  =       "Are you sure you want to end the replay?"
