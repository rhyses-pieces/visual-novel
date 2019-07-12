# The game starts here
label start:

    # Stop main menu music.
    stop music
    scene ref:
        size (1920, 1080)
    window show
    #
    
    "Hello, what's your name?"
    
    ########################
    # Character Name
    label naming_character:
    
    $ first_name = renpy.input("{i}What is my first name?{/i} \n(If no name given, the default is Meteor.)")
    $ first_name = first_name.strip()
    if first_name == "":
        $ first_name = "Meteor"
    
    $ last_name = renpy.input("{i}What is my last name?{/i} \n(If no name given, the default is Survivor.)")
    $ last_name = last_name.strip()
    if last_name == "":
        $ last_name = "Survivor"
    
    "So your name is [first_name] [last_name]?"
    
    menu:
        extend " "
        "Yes.":
            pass
        "No.":
            jump naming_character   
    #######################
    
    #######################
    # Pronoun Selection
    label pronoun_selection:
    
    "Please select the pronouns for [first_name] [last_name]."
    menu:
        extend " "
        "He/Him":
            pass
        "She/Her":
            $ he, him, his = "she", "her", "her"
            $ He, Him, His = "She", "Her", "Her"
        "They/Them":
            $ he, him, his = "they", "them", "their"
            $ He, Him, His = "They", "Them", "Their"
            $ is_, was, s, es = "are", "were", "", ""
            $ ies, has_ = "y", "have"
    
    "Did you hear what [first_name] [last_name] said? [He] told me [he] went to school and saw someone lighting the bleachers on fire. But [he] [was] blamed for it because [he] [was] at the wrong place in the wrong time. [He] [has_] a big staff though, so what if [he] really [was] involved?"
    
    
    "Is this pronoun choice correct?"
    menu:
        extend " "
        "Yes.":
            pass
        "No.":
            jump pronoun_selection
    #######################
    
    "Hello, world."

    narrator "You've created a new Ren'Py game."

    scene cg1:
        size (1920, 1080)

    narrator "Once you add a story, pictures, and music, you can release it to the world!"

    scene cg2:
        size (1920, 1080)

    narrator "But, soft! what light through yonder window breaks? It is the east, and
       Juliet is the sun. O true apothecary, Thy drugs are quick. Thus with a kiss
       I die."

    scene cg3:
        size (1920, 1080)

    "Lorem ipsum dolor sit amet, consectetur adipiscing elit,
     sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
     Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris..."

    "Add text here! Use extend to keep the textbox visible during the choice!"

    menu:
        extend " "
        "I'm addicted to coding!":
            pass
        "I really should go to bed!":
            pass
        "Nah, energy drinks.":
            pass
        "I want midnight ramen please":
            pass

    narrator "You thought that choice meant something... but the joke's on you!"

    narrator "It's completely meaningless! Ahahahahahaha!"

    "Four score and seven years ago our fathers brought forth on this continent,
     a new nation, conceived in Liberty, and dedicated to the proposition that
     all men are created equal."

    "Now we are engaged in a great civil war, testing whether that nation, or any
     nation so conceived and so dedicated, can long endure."

    "We are met on a great battle-field of that war."

    "We have come to dedicate a portion of that field, as a final resting place
     for those who here gave their lives that that nation might live. It is
     altogether fitting and proper that we should do this."

    "But, in a larger sense, we can not dedicate -- we can not consecrate -- we
     can not hallow -- this ground."

    "The brave men, living and dead, who struggled here, have consecrated it, far
     above our poor power to add or detract. The world will little note, nor long
     remember what we say here, but it can never forget what they did here."

    nvl_narrator "Ooh cool beans."

    "It is for us the living, rather, to be dedicated here to the unfinished work
     which they who fought here have thus far so nobly advanced."

    "It is rather for us to be here dedicated to the great task remaining before us
     -- that from these honored dead we take increased devotion to that cause for
     which they gave the last full measure of devotion..."

    "-- that we here highly resolve that these dead shall not have died in vain --
     that this nation, under God, shall have a new birth of freedom --"

    "-- and that government of the people, by the people, for the people, shall not
     perish from the earth."

    scene ref:
        size (1920, 1080)

    nvl_narrator "But really, these kinds of epic speeches should be happening in NVL." with dissolve

    nvl_narrator "Four score and seven years ago our fathers brought forth on this continent,
    a new nation, conceived in Liberty, and dedicated to the proposition that
    all men are created equal."

    nvl_narrator "I like this speech. It was short."

    nvl_narrator "Now we are engaged in a great civil war, testing whether that nation, or any
    nation so conceived and so dedicated, can long endure."

    nvl_narrator "We have come to dedicate a portion of that field, as a final resting place
     for those who here gave their lives that that nation might live. It is
     altogether fitting and proper that we should do this."

    nvl clear

    nvl_narrator "But, in a larger sense, we can not dedicate -- we can not consecrate -- we
     can not hallow -- this ground."

    nvl_narrator "The brave men, living and dead, who struggled here, have consecrated it, far
     above our poor power to add or detract. The world will little note, nor long
     remember what we say here, but it can never forget what they did here."

    nvl_narrator "It is for us the living, rather, to be dedicated here to the unfinished work
     which they who fought here have thus far so nobly advanced."

    extend " It is rather for us to be here dedicated to the great task remaining before us
     -- that from these honored dead we take increased devotion to that cause for
     which they gave the last full measure of devotion --"

    extend " that we here highly resolve that these dead shall not have died in vain --
     that this nation, under God, shall have a new birth of freedom --"

    nvl clear

    nvl_narrator "-- and that government of the people, by the people, for the people, shall not
     perish from the earth."

    narrator "There, that was more fitting. Don't you think?" with dissolve

    # This ends the game.

    return
