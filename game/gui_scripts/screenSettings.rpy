## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen settings(fromPause=False,fromMain=False):

    tag menu
    key "game_menu" action Return()
    
    python:
        xy = renpy.get_physical_size()
        
    if fromMain:
        add gui.mm_background
    
    fixed:
        if fromPause == False:
            at gui_fade_inout
        else:
            at gui_fade_out
        add "gui_overlay"
        
        use exit_button
        
        add "gui/log_decor_top.png" at gui_overlaydecor_top
            
        frame:
            background None
            xsize 1200
            at gui_overlaydecor_bottom
            
            add "gui/settings_decor_bottom.png":
                alpha 0.3
                
            text "SETTINGS":
                style "gui_overlay_title"
        vbox:
            xsize 1200
            xalign 0.5 yalign 0.45
            spacing 60
            at gui_fade(1.0)
            
            hbox:
                xsize 1200 ysize 200
            
                grid 2 3:
                    xalign 0.0
                    spacing 10
                    
                    text "Display" style "settings_header"
                
                    null height 1
                
                    button:
                        xsize 220 ysize 60
                        at gui_buttonfade
                        
                        hovered Play("system",guisfx_button_hover)
                        action [SelectedIf(xy[0] < 1350),
                                Play("system",guisfx_button_click),
                                Preference("display", 0.67)]
                        
                        add "gui/settings_1280_idle.png"
                        text "1280 x 720" style "settings_button_text"
                     
                    button:
                        xalign 1.0
                        xsize 240 ysize 60
                        at gui_buttonfade
                        
                        hovered Play("system",guisfx_button_hover)
                        action [SelectedIf(preferences.fullscreen == False and xy[0] >= 1700),
                                Play("system",guisfx_button_click),
                                Preference("display", 1.0)]
                        
                        add "gui/settings_1920_idle.png"
                        text "1920 x 1080" style "settings_button_text"
                    
                    button:
                        xsize 250 ysize 60
                        at gui_buttonfade
                        
                        hovered Play("system",guisfx_button_hover)
                        action [Play("system",guisfx_button_click),
                                Preference("display", "fullscreen")]
                        
                        add "gui/settings_fullscreen_idle.png"
                        text "FULLSCREEN" style "settings_button_text"

                    null height 1
                
                grid 2 2:
                    xalign 1.0
                    spacing 10
                    
                    text "Skip" style "settings_header"
                
                    null height 1
                
                    button:
                        xsize 250 ysize 60
                        at gui_buttonfade
                        
                        hovered Play("system",guisfx_button_hover)
                        action [Play("system",guisfx_button_click),
                                Preference("skip", "seen")]
                        
                        add "gui/settings_read_idle.png"
                        text "READ TEXT" style "settings_button_text"
                     
                    button:
                        xalign 1.0
                        xsize 200 ysize 60
                        at gui_buttonfade
                        
                        hovered Play("system",guisfx_button_hover)
                        action [Play("system",guisfx_button_click),
                                Preference("skip", "all")]
                        
                        add "gui/settings_all_idle.png"
                        text "ALL TEXT" style "settings_button_text"
                        
            vbox:
                xsize 1200 ysize 200
                yoffset -40
                spacing 40
                
                vbox:
                    xsize 1200 ysize 70
                    xalign 0.5
                    
                    text "Text Speed" style "settings_header" xalign 0.5
                    
                    hbox:
                        xsize 1200 xalign 0.5
                        spacing 13
                        
                        text "SLOW":
                            xsize 85 xalign 1.0
                            style "caption_med"
                            kerning gui.advname_font_kerning
                        
                        bar:
                            hovered Play("system",guisfx_button_hover)
                            value Preference("text speed")
                            base_bar "gui/settings_text_bar.png"
                            thumb "gui/settings_text_thumb.png"
                            
                            xsize 987 ysize 22
                            xalign 0.5 yoffset 3
                            at gui_buttonfade
                        
                        text "FAST":
                            xsize 85 xalign 0.0 xoffset 4
                            style "caption_med"
                            kerning gui.advname_font_kerning
                
                vbox:
                    xsize 1200
                    xalign 0.5 ysize 70
                    text "Auto Forward Pause" style "settings_header" xalign 0.5
                    
                    hbox:
                        xsize 1200 xalign 0.5
                        spacing 13
                        
                        text "SHORT":
                            xsize 85 xalign 1.0
                            style "caption_med"
                            kerning gui.advname_font_kerning
                        
                        bar:
                            hovered Play("system",guisfx_button_hover)
                            value Preference("auto-forward time")
                            base_bar "gui/settings_text_bar.png"
                            thumb "gui/settings_text_thumb.png"
                            
                            xsize 987 ysize 22
                            xalign 0.5 yoffset 3
                            at gui_buttonfade
                        
                        text "LONG":
                            xsize 85 xalign 0.0 xoffset 4
                            style "caption_med"
                            kerning gui.advname_font_kerning
                            
            grid 2 2:
                xsize 1200 xfill True ysize 140
                spacing 30
                
                hbox:
                    xsize 505 ysize 30
                    xalign 0.0
                    
                    text "Music" style "settings_header" xsize 150 ysize 30
                    
                    bar:
                        hovered Play("system",guisfx_button_hover)
                        value Preference("music volume")
                        style "settings_bar_volume"
                        at gui_buttonfade
                
                hbox:
                    xsize 505 ysize 30
                    xalign 1.0
                    
                    text "System" style "settings_header" xsize 150 ysize 30
                    
                    bar:
                        hovered Play("system",guisfx_button_hover)
                        value MixerValue("systemMixer")
                        style "settings_bar_volume"
                        at gui_buttonfade
                
                hbox:
                    xsize 505 ysize 30
                    xalign 0.0
                    
                    text "Sound" style "settings_header" xsize 150 ysize 30
                    
                    bar:
                        hovered Play("system",guisfx_button_hover)
                        value Preference("sound volume")
                        style "settings_bar_volume"
                        at gui_buttonfade
                
                hbox:
                    xsize 505 ysize 30
                    xalign 1.0
                    
                    if config.has_voice:
                        text "Voice" style "settings_header" xsize 150 ysize 30
                        
                        bar:
                            hovered Play("system",guisfx_button_hover)
                            value Preference("voice volume")
                            style "settings_bar_volume"
                            at gui_buttonfade
                    else:
                        null height 1
                        

style settings_header:
    font gui.adv_font_face
    size gui.adv_font_size
    color gui.adv_font_color
    
style settings_button_text:
    font gui.adv_font_face
    size gui.adv_font_size * 0.8
    color gui.adv_font_color
    kerning gui.advname_font_kerning
    
    xoffset 37
    yoffset -12
    
    bold True
    
style settings_bar_volume:
    xsize 346 ysize 15
    xalign 1.0 yalign 0.5
    left_bar "gui/settings_volume_full.png"
    right_bar "gui/settings_volume_empty.png"