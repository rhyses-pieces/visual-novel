## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    key "b" action ShowMenu('history')
    key "mousedown_4" action ShowMenu('history')
    key "s" action ShowMenu('save')
    key "l" action ShowMenu('load')
    key "m" action MainMenu(confirm=True)

    window:
        style "nvl_window"
        
        has vbox:
            spacing 38
            
        null height 100
        
        use nvl_dialogue(dialogue)
        
    use nvl_qm
        


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit None is None

                if d.who is not None:
                
                    if varAdvNameUppercase == True:
                        text d.who.upper() + ".  ":
                            id d.who_id
                        
                    else:
                        text d.who:
                            id d.who_id
                
                if d.who is None:
                    text d.what:
                        id d.what_id
                        style "nvl_thought"
                        
                else:
                    text d.what:
                        id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 8

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_window:
    xfill True
    yfill True
    top_margin 0
    bottom_margin 0
    left_margin 0
    right_margin 0

    background "gui_overlay"

style nvl_entry:
    xfill True
    ysize None

style nvl_label:
    xpos 700
    xanchor 1.0
    ypos 1
    yanchor 0.0
    xsize 300
    min_width 300
    text_align 1.0

style nvl_dialogue:
    xpos 710
    xanchor 0.0
    xsize 790
    min_width 790
    text_align 0

style nvl_thought:
    xalign 0.5
    xsize 1100
    min_width 1100
    text_align 0.0
    first_indent 30
    
    
screen nvl_qm():
    add "gui/nvl_qm.png":
        alpha 0.3
        xalign 0.5 ypos 1000
        
    hbox:
        xalign 0.5 ypos 977
        spacing 25
        
        textbutton "LOG":
            hovered Play("system",guisfx_button_hover)
            action [Play("system",guisfx_button_click),
                    ShowMenu('history',fromPause=True)]
            text_style "nvl_qm_button"
            at gui_buttonfade
            
        textbutton "SKIP":
            hovered Play("system",guisfx_button_hover)
            action [Play("system",guisfx_button_click),
                    Skip()]
            text_style "nvl_qm_button"
            at gui_buttonfade
            
        textbutton "AUTO":
            hovered Play("system",guisfx_button_hover)
            action [Play("system",guisfx_button_click),
                    Preference("auto-forward", "toggle")]
            text_style "nvl_qm_button"
            at gui_buttonfade
            
        textbutton "SAVE":
            hovered Play("system",guisfx_button_hover)
            action [Play("system",guisfx_button_click),
                    ShowMenu('save',fromPause=True)]
            text_style "nvl_qm_button"
            at gui_buttonfade
            
        textbutton "LOAD":
            hovered Play("system",guisfx_button_hover)
            action [Play("system",guisfx_button_click),
                    ShowMenu('load',fromPause=True)]
            text_style "nvl_qm_button"
            at gui_buttonfade
            
        textbutton "PAUSE":
            hovered Play("system",guisfx_button_hover)
            action [Play("system",guisfx_button_click),
                    ShowMenu('pause_menu',fromPause=True)]
            text_style "nvl_qm_button"
            at gui_buttonfade
        
style nvl_qm_button:
    font gui.advname_font_face
    size gui.advname_font_size * 0.8
    color gui.advname_font_color
    kerning gui.advname_font_kerning
    
    text_align 0.5
    xalign 0.5