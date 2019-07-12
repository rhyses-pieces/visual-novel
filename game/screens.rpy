################
# FIRST NAME SCREEN
label firstname_input:
    
    window hide

    $ first_name = renpy.input("{i}What is my first name?{/i}\n\n[[Please enter a name. \nIf none given, the default is Ash.]]", length=16, default=first_name)

    $ first_name = first_name.strip()

    #  Default Name
    if first_name == "":
        $ first_name = "Meteor"

    call screen first_input_confirm

    $ result = _return

    if result == 0: #Accepted name
        hide screen first_input_confirm
        jump lastname_input
    else: #Rejected name
        hide screen first_input_confirm
        $ first_name = ""
        jump firstname_input

    $ renpy.pause()
    
################
# LAST NAME SCREEN
label lastname_input:
    
    window hide

    $ last_name = renpy.input("{i}What is my last name?{/i}\n\n[[Please enter a name. \nIf none given, the default is Robinson.]]", length=16, default=last_name)

    $ last_name = last_name.strip()

    #  Default Name
    if last_name == "":
        $ last_name = "Survivor"

    call screen last_input_confirm

    $ result = _return

    if result == 0: #Accepted name
        hide screen last_input_confirm
        jump confirm_name
    else: #Rejected name
        hide screen last_input_confirm
        $ last_name = ""
        jump lastname_input

    $ renpy.pause()