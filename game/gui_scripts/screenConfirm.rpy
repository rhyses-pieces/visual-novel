init offset = -1

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 99999

    style_prefix "confirm"
    
    fixed:
        at gui_fade_inout
        add "gui/choice_overlay.png":
            if gui.overlay_opacity <= 0.7:
                alpha 0.85
            else:
                alpha gui.overlay_opacity
        
        vbox:
            xalign 0.5 yalign 0.5
            spacing 375
            add "gui/log_decor_top.png":
                alpha 0.3
            add "gui/log_decor_top.png":
                alpha 0.3
            
        vbox:
            xalign 0.5 yalign 0.5
            spacing 35
            
            frame:
                xalign 0.5
                xsize 773 ysize 100
                
                if message == gui.ARE_YOU_SURE:
                    text gui.message_confirm style "confirm_prompt_text"
                elif message == gui.DELETE_SAVE:
                    text gui.message_deletesave style "confirm_prompt_text"
                elif message == gui.OVERWRITE_SAVE:
                    text gui.message_overwrite style "confirm_prompt_text"
                elif message == gui.LOADING:
                    text gui.message_load style "confirm_prompt_text"
                elif message == gui.QUIT:
                    text gui.message_quit style "confirm_prompt_text"
                elif message == gui.MAIN_MENU:
                    text gui.message_mainmenu style "confirm_prompt_text"
                elif message == gui.END_REPLAY:
                    text gui.message_replay style "confirm_prompt_text"
                elif message == gui.SLOW_SKIP:
                    text gui.message_slowskip style "confirm_prompt_text"
                elif message == gui.FAST_SKIP_SEEN or message == gui.FAST_SKIP_UNSEEN:
                    text gui.message_fastskip style "confirm_prompt_text"
                else:
                    text _(message) style "confirm_prompt_text"
            
            hbox:
                xalign 0.5 
                spacing 125
                xoffset -15
                
                button:
                    hovered Play("system",guisfx_button_hover)
                    action [Play("system",guisfx_button_click),
                            no_action]
                    at gui_buttonfade
                    
                    focus_mask None
                    xalign 0.5
                    xsize 108
                    
                    add "gui/confirm_no_idle.png"
                    text "No":
                        style "confirm_button_text"
                        xoffset 43
                    
                button:
                    hovered Play("system",guisfx_button_hover)
                    action [Play("system",guisfx_button_click),
                            yes_action]
                    at gui_buttonfade
                    
                    focus_mask None
                    xalign 0.5
                    xsize 108
                    
                    add "gui/confirm_yes_idle.png"
                    text "Yes":
                        style "confirm_button_text"
                        xoffset 47
                        
    ## Right-click and escape answer "no".
    key "game_menu" action no_action

style confirm_prompt_text:
    font gui.adv_font_face
    size gui.adv_font_size
    color gui.adv_font_color
    text_align 0.5
    xalign 0.5 yalign 0.5

style confirm_button_text:
    font gui.adv_font_face
    size gui.adv_font_size
    color gui.adv_font_color
    bold True
    
    yalign 0.5 yoffset -1