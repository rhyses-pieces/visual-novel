init offset = -1

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice
        
style choice_button is default:
    font gui.adv_font_face
    size gui.adv_font_size * 0.85
    color gui.adv_font_color
    kerning gui.advname_font_kerning * 0.5
    
    text_align 0.0
    bold True

screen choice(items):
    modal False
    
    fixed:
        at gui_fade_inout
        add "gui_overlay"

        vbox:
            xsize 954
            yoffset -115
            xalign 0.5 yalign 0.5
            spacing 30
            
            for i in items:
                button:
                    text i.caption style "choice_button_text"
                    hovered Play("system",guisfx_button_hover)
                    action [Play("system",guisfx_button_click),
                            i.action]
                    add "gui/choice_option.png"
                    
                    at gui_buttonfade_enter(0.5)

style choice_vbox:
    xpos 475
    ypos 0.4
    yanchor 0.5

    spacing 45

style choice_button_text is default:
    font gui.adv_font_face
    size gui.adv_font_size * 0.85
    color gui.adv_font_color
    kerning gui.advname_font_kerning * 0.5
    
    text_align 0.0
    bold True