init offset = -1

## ADV screen ##################################################################

screen say(who, what):
    style_prefix "say"
    zorder 999
    
    window:
        id "window"

        if who is not None:

            window:
                style "namebox"
                if varAdvNameUppercase == True:
                    text who.upper() id "who"
                else:
                    text who id "who"
        
        if who is not None:
            text what id "what" ypos 114
        else:
            text what id "what" ypos 47
        
    use adv_qm()


    ## Phone settings for side images. Not applicable, but kept for backwards
    ## compatibility.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize 278
    background Image("gui/adv_textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos 300
    xanchor 0.0
    xsize 800
    ypos 47
    ysize 50

style say_label:
    font gui.advname_font_face
    size gui.advname_font_size
    color gui.advname_font_color
    kerning gui.advname_font_kerning
    
    xalign 0.0
    yalign 0.5

style say_dialogue:
    font gui.adv_font_face
    size gui.adv_font_size
    color gui.adv_font_color
    line_leading gui.adv_font_line
    
    xpos 300
    xsize 1190
    
## ADV Quick Menu ##################################################################

screen adv_qm():

    ## Shortcuts ###################################################################
    
    key "b" action ShowMenu('history')
    key "mousedown_4" action ShowMenu('history')
    key "s" action ShowMenu('save')
    key "l" action ShowMenu('load')
    key "m" action MainMenu(confirm=True)
    
    ## Layout ######################################################################
    
    imagebutton auto "gui/adv_qm_hideui_%s.png":
        xpos 1767 ypos 793
        hovered [Play("system",guisfx_button_hover),
                Show("qm_tooltip",ttcontent="HIDE UI",ttxpos=1680,ttypos=797)]
        unhovered Hide("qm_tooltip")
        action [Play("system",guisfx_button_click),
                Hide("qm_tooltip"),
                HideInterface()]
        at gui_buttonfade
        
    add "gui/adv_qm_decor.png":
        xpos 1608 ypos 1030
    
    text "QUICK MENU":
        style "caption_small"
        xpos 1647 ypos 1021
        color Color(color=gui.adv_font_color, alpha=0.5)
        text_align 0.5
    
    hbox:
        spacing 19
        xpos 1605 ypos 870
        
        imagebutton auto "gui/adv_qm_log_%s.png":
            hovered [Play("system",guisfx_button_hover),
                    Show("qm_tooltip",ttcontent="LOG",ttxpos=1610,ttypos=844)]
            unhovered Hide("qm_tooltip")
            action [Play("system",guisfx_button_click),
                    Hide("qm_tooltip"),
                    ShowMenu('history')]
            at gui_buttonfade
        imagebutton auto "gui/adv_qm_skip_%s.png":
            hovered [Play("system",guisfx_button_hover),
                    Show("qm_tooltip",ttcontent="SKIP",ttxpos=1680,ttypos=844)]
            unhovered Hide("qm_tooltip")
            action [Play("system",guisfx_button_click),
                    Hide("qm_tooltip"),
                    Skip()]
            at gui_buttonfade
        imagebutton auto "gui/adv_qm_auto_%s.png":
            hovered [Play("system",guisfx_button_hover),
                    Show("qm_tooltip",ttcontent="AUTO",ttxpos=1744,ttypos=844)]
            unhovered Hide("qm_tooltip")
            action [Play("system",guisfx_button_click),
                    Hide("qm_tooltip"),
                    Preference("auto-forward", "toggle")]
            at gui_buttonfade
        
    hbox:
        spacing 19
        xpos 1605 ypos 948
         
        imagebutton auto "gui/adv_qm_save_%s.png":
            hovered [Play("system",guisfx_button_hover),
                    Show("qm_tooltip",ttcontent="SAVE",ttxpos=1603,ttypos=921)]
            unhovered Hide("qm_tooltip")
            action [Play("system",guisfx_button_click),
                    Hide("qm_tooltip"),
                    ShowMenu('save')]
            at gui_buttonfade
        imagebutton auto "gui/adv_qm_load_%s.png":
            hovered [Play("system",guisfx_button_hover),
                    Show("qm_tooltip",ttcontent="LOAD",ttxpos=1672,ttypos=921)]
            unhovered Hide("qm_tooltip")
            action [Play("system",guisfx_button_click),
                    Hide("qm_tooltip"),
                    ShowMenu('load')]
            at gui_buttonfade
        imagebutton auto "gui/adv_qm_menu_%s.png":
            hovered [Play("system",guisfx_button_hover),
                    Show("qm_tooltip",ttcontent="MENU",ttxpos=1744,ttypos=921)]
            unhovered Hide("qm_tooltip")
            action [Play("system",guisfx_button_click),
                    Hide("qm_tooltip"),
                    ShowMenu('pause_menu')]
            at gui_buttonfade
            
style caption_small:
    font gui.adv_font_face 
    size gui.adv_font_size * 0.45
    bold True
    color gui.adv_font_color
    kerning 2
    
style caption_med:
    font gui.adv_font_face
    size gui.adv_font_size * 0.6
    bold True
    color gui.adv_font_color
            
image gui_indicator_skip:
    "gui/indicator_skip.png"
    alpha 1.0
    block:
        linear 0.7 alpha 0.0
        linear 0.7 alpha 1.0
        pause 0.2
        repeat
        
screen qm_tooltip(ttcontent,ttxpos,ttypos):
    zorder 9999
    text ttcontent:
        style "caption_med"
        xpos ttxpos ypos ttypos
        at gui_fade_inout(0.0,0.3)
        
        
## Indicators ######################################################################
            
screen indicator(_layer="top_layer"):
    
    zorder 100
    style_prefix "skip"
    
    if _rollback:
        if config.skipping == "slow" or config.skipping == "fast":
            add "gui_indicator_skip" xalign 0.5 yalign 0.5

init python:
    config.skip_indicator = None
    config.overlay_screens.append("indicator")