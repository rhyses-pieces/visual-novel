if selgen == True:
                    vbox:
                        style_prefix "radio"
                        label _("Gender")
                        textbutton _("Male") action [Function(dgender, "guy"), SetVariable("MCgender", "male")]
                        textbutton _("Female") action [Function(dgender, "gal"), SetVariable("MCgender", "female")]
                        textbutton _("Nonbinary") action [Function(dgender, "nb"), SetVariable("MCgender", "nonbinary")]
                else:
                    pass
                if selpron == True:
                    vbox:
                        style_prefix "radio"
                        label _("Pronouns")
                        textbutton _("He/Him") action [Function(dpronouns, "he"), SetVariable("they", "he")]
                        textbutton _("She/Her") action [Function(dpronouns, "she"), SetVariable("they", "she")]
                        textbutton _("They/Them") action [Function(dpronouns, "they"), SetVariable("they", "they")]
                        textbutton _("Custom") action [Show("cpron"), Show("bsub"), Show("bob"), Show("bposs"), Show("bref")]
                else:
                    pass﻿

## Pronouns screen ##############################################################

screen cpron():

    modal True

    zorder 100

    style_prefix "cpron"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _("Custom Pronouns:"):
                style "cpron_prompt"
                xalign 0.5
            hbox:
                vbox:
                    text "Subjective: "
                    text "Objective: "
                    text "Possessive: "
                    text "Reflexive: "
                vbox:
                    xsize 150

            hbox:
                style_prefix "radio"
                textbutton _("Singular") action SetVariable("tempplu", False)
                textbutton _("Plural") action SetVariable("tempplu", True)
            hbox:
                textbutton _("Ok") action [Function(cpronouns, tempsub.strip(), tempob.strip(), tempposs.strip(), tempref.strip(), tempplu), Hide("cpron"), Hide("bsub"), Hide("bob"), Hide("bposs"), Hide("bref")]
                if pronquestion==True:
                    textbutton _("Cancel") action [Hide("cpron"), Hide("bsub"), Hide("bob"), Hide("bposs"), Hide("bref"), Jump("pronques")]
                else:
                    textbutton _("Cancel") action [Hide("cpron"), Hide("bsub"), Hide("bob"), Hide("bposs"), Hide("bref")]

    key "game_menu" action Hide("cpron")


style cpron_frame is gui_frame
style cpron_prompt is gui_prompt
style cpron_prompt_text is gui_prompt_text
style cpron_button is gui_medium_button
style cpron_button_text is gui_medium_button_text

style cpron_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style cpron_prompt_text:
    text_align 0.5
    layout "subtitle"
style cpron_promtex:
    line_leading 7
style cpron_button:
    properties gui.button_properties("cpron_button")

style cpron_button_text:
    properties gui.button_text_properties("cpron_button")

style cpron_hbox:
    xalign 0.5
    spacing 100
screen isub:
    button xysize(1280, 720) keysym "K_RETURN" action [Hide("isub"), Show("bsub")]
    zorder 115
    input value VariableInputValue("tempsub") length 6 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '-" xpos 0.541 ypos 0.365
screen iob:
    button xysize(1280, 720) keysym "K_RETURN" action [Hide("iob"), Show("bob")]
    zorder 115
    input value VariableInputValue("tempob") length 6 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '-" xpos 0.541 ypos 0.411
screen iposs:
    button xysize(1280, 720) keysym "K_RETURN" action [Hide("iposs"), Show("bposs")]
    zorder 115
    input value VariableInputValue("tempposs") length 6 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '-" xpos 0.541 ypos 0.456
screen iref:
    button xysize(1280, 720) keysym "K_RETURN" action [Hide("iref"), Show("bref")]
    zorder 115
    input value VariableInputValue("tempref") length 12 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '-" xpos 0.541 ypos 0.502
screen bsub:
    zorder 110
    textbutton [tempsub] style "promtex" xpos 0.541 ypos 0.365 action [Show("isub"), Hide("bsub")]
screen bob:
    zorder 110
    textbutton [tempob] style "promtex" xpos 0.541 ypos 0.411 action [Show("iob"), Hide("bob")]
screen bposs:
    zorder 110
    textbutton [tempposs] style "promtex" xpos 0.541 ypos 0.456 action [Show("iposs"), Hide("bposs")]
screen bref:
    zorder 110
    textbutton [tempref] style "promtex" xpos 0.541 ypos 0.502 action [Show("iref"), Hide("bref")]

init python:
    def dpronouns(pronouns):
        global MCpronouns
        global theyare
        global they
        global them
        global their
        if pronouns == "she":
            MCpronouns = "she/her"
            theyare = "she is"
            they = "she"
            them = "her"
            their = "hers"
            themselves = "herself"
            plural = False
        if pronouns == "he":
            MCpronouns="he/him"
            theyare = "he is"
            they = "he"
            them = "him"
            their = "his"
            themselves = "himself"
            plural = False
        if pronouns == "they":
            MCpronouns = "they/them"
            theyare = "they are"
            they = "they"
            them = "them"
            their = "their"
            themselves = "themself"
            plural = False
        return

    def cpronouns(sub, ob, poss, ref, plu):
        global MCpronouns
        global theyare
        global they
        global them
        global their
        global cpron
        MCpronouns = sub+"/"+ob
        if plu:
            theyare = sub+" are"
        else:
            theyare = sub+" is"
        they = sub
        them = ob
        their = poss
        themselves = ref
        cpron = True
        return

    def dgender(gender):
        global MCgender
        global person
        if gender == "guy":
            MCgender = "male"
            person = "man"
            sweetheart = "boyfriend"
            spouse = "husband"
            parent = "father"
        if gender == "gal":
            MCgender = "female"
            person = "woman"
            sweetheart = "girlfriend"
            spouse = "wife"
            parent = "mother"
        if gender == "nb":
            MCgender = "nonbinary"
            person = "person"
            sweetheart = "sweetheart"
            spouse = "spouse"
            parent = "parent"
        return
