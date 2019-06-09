init offset = -1

screen extras(fromMain=True,doTrans=True):
    
    tag menu
    key "game_menu" action Return()
    
    if fromMain:
        add gui.mm_background
    
    fixed:
        if doTrans:
            at gui_fade_inout
            
        add "gui_overlay"
        
        if doTrans:
            add "gui/log_decor_top.png" at gui_overlaydecor_top
        else:
            add "gui/log_decor_top.png" xalign 0.5 ypos 104 alpha 0.3
        
        use exit_button(doTrans=False)
        
        frame:
            background None
            xsize 1200
            if doTrans:
                at gui_overlaydecor_bottom
            else:
                xalign 0.5 ypos 967
            
            add "gui/extras_decor_bottom.png":
                alpha 0.3
                
            text "EXTRAS":
                style "gui_overlay_title"
                
        hbox:
            spacing 50
            xalign 0.5
            yalign 0.5
            
            if doTrans:
                at gui_fade(1.0)
            
            if gui.has_cg:
                button:
                    if gui.has_mr:
                        hovered [Play("system",guisfx_button_hover),
                                Show("pause_tooltip",ttcontent="CG Gallery",ttxpos=0.415,ttypos=630)]
                    else:
                        hovered [Play("system",guisfx_button_hover),
                                Show("pause_tooltip",ttcontent="CG Gallery",ttxpos=0.5,ttypos=630)]
                    unhovered Hide("pause_tooltip")
                    action [Play("system",guisfx_button_click),
                            Hide("pause_tooltip"),
                            ShowMenu('cg_page1')]
                
                    xsize 275 ysize 260
                    at gui_buttonfade
                
                    add "gui/extras_cg_idle.png" xalign 0.5
            
            if gui.has_mr:
                button:
                    if gui.has_cg:
                        hovered [Play("system",guisfx_button_hover),
                                Show("pause_tooltip",ttcontent="Music Room",ttxpos=0.585,ttypos=630)]
                    else:
                        hovered [Play("system",guisfx_button_hover),
                                Show("pause_tooltip",ttcontent="Music Room",ttxpos=0.5,ttypos=630)]
                    unhovered Hide("pause_tooltip")
                    action [Play("system",guisfx_button_click),
                            Hide("pause_tooltip"),
                            ShowMenu('music_room')]
                
                    xsize 275 ysize 260
                    at gui_buttonfade
                
                    add "gui/extras_music_idle.png" xalign 0.5