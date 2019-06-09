init offset = -1

screen pause_menu(fromPause=False):
    
    tag menu
    key "game_menu" action Return()
    
    fixed:
        if not fromPause:
            at gui_fade_inout
        else:
            at gui_fade_out
            
        add "gui_overlay"
        
        add "gui/log_decor_top.png" at gui_overlaydecor_top
        
        use exit_button
        
        frame:
            background None
            xsize 1200
            at gui_overlaydecor_bottom
            
            add "gui/pause_decor_bottom.png":
                alpha 0.3
            text "PAUSE MENU":
                style "gui_overlay_title"
                
        grid 3 2:
            spacing 50
            xalign 0.5
            yalign 0.5
            
            at gui_fade(1.0)
            
            button:
                hovered [Play("system",guisfx_button_hover),
                        Show("pause_tooltip",ttcontent="Log",ttxpos=0.33,ttypos=473)]
                unhovered Hide("pause_tooltip")
                action [Play("system",guisfx_button_click),
                        Hide("pause_tooltip"),
                        ShowMenu('history',fromPause=True)]
                
                xsize 275 ysize 260
                at gui_buttonfade
                
                add "gui/pause_log_idle.png" xalign 0.5
                
            button:
                hovered [Play("system",guisfx_button_hover),
                        Show("pause_tooltip",ttcontent="Save",ttxpos=0.5,ttypos=473)]
                unhovered Hide("pause_tooltip")
                action [Play("system",guisfx_button_click),
                        Hide("pause_tooltip"),
                        ShowMenu('save',fromPause=True)]
                
                xsize 275 ysize 260
                at gui_buttonfade
                
                add "gui/pause_save_idle.png" xalign 0.5
                
            button:
                hovered [Play("system",guisfx_button_hover),
                        Show("pause_tooltip",ttcontent="Load",ttxpos=0.67,ttypos=473)]
                unhovered Hide("pause_tooltip")
                action [Play("system",guisfx_button_click),
                        Hide("pause_tooltip"),
                        ShowMenu('load',fromPause=True)]
                
                xsize 275 ysize 260
                at gui_buttonfade
                
                add "gui/pause_load_idle.png" xalign 0.5
                
            button:
                hovered [Play("system",guisfx_button_hover),
                        Show("pause_tooltip",ttcontent="Settings",ttxpos=0.33,ttypos=782)]
                unhovered Hide("pause_tooltip")
                action [Play("system",guisfx_button_click),
                        Hide("pause_tooltip"),
                        ShowMenu('settings',fromPause=True)]
                
                xsize 275 ysize 260
                at gui_buttonfade
                
                add "gui/pause_settings_idle.png" xalign 0.5
            
            button:
                hovered [Play("system",guisfx_button_hover),
                        Show("pause_tooltip",ttcontent="Main Menu",ttxpos=0.5,ttypos=782)]
                unhovered Hide("pause_tooltip")
                action [Play("system",guisfx_button_warn),
                        Hide("pause_tooltip"),
                        MainMenu(confirm=True)]
                
                xsize 275 ysize 260
                at gui_buttonfade
                
                add "gui/pause_mainmenu_idle.png" xalign 0.5
                
            button:
                hovered [Play("system",guisfx_button_hover),
                        Show("pause_tooltip",ttcontent="Quit",ttxpos=0.67,ttypos=782)]
                unhovered Hide("pause_tooltip")
                action [Play("system",guisfx_button_warn),
                        Hide("pause_tooltip"),
                        Quit(confirm=True)]
                
                xsize 275 ysize 260
                at gui_buttonfade
                
                add "gui/pause_quit_idle.png" xalign 0.5
                
screen pause_tooltip(ttcontent,ttxpos,ttypos):
    zorder 9999
    text ttcontent:
        style "caption_pause"
        xcenter ttxpos ycenter ttypos
        at gui_fade_inout(0.0,0.3)
        
style caption_pause:
    font gui.adv_font_face
    size gui.adv_font_size
    color gui.adv_font_color