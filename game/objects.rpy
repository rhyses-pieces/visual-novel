init -1:
    # Declare characters used by this game. The color argument colorizes the
    # name of the character.

    define narrator = Character(None,ctc="ctc_default",ctc_pause="ctc_default")

    define nvl_narrator = NVLCharacter(None,kind=nvl,what_style="nvl_thought",ctc="ctc_default",ctc_pause="ctc_default")


    
    
#################
# Character Name
#################
    $ first_name = ""
    $ last_name = ""
    
#########################
## Character Pronouns
    default he = "he"
    default him =  "him"
    default his = "his"
    default He = "He"
    default Him = "Him"
    default His = "His"
    default is_ = "is"
    default was = "was"
    default has_ = "has"
    default s = "s"
    default es = "es"
    default ies = "ies"
    
##########
# Images #
##########
    image ref = "gui/mm_background.jpg"
    image cg1 = "images/cg1.jpg"
    image cg2 = "images/cg2.jpg"
    image cg3 = "images/cg3.jpg"