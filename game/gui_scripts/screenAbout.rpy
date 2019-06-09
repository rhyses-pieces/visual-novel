init offset = -1

screen about():

    tag menu
    key "game_menu" action Return()
    
    add gui.mm_background
    
    fixed:
        at gui_fade_inout
        add "gui_overlay"
        
        add "gui/log_decor_top.png" at gui_overlaydecor_top
            
        use exit_button
        
        frame:
            background None
            xsize 1200
            at gui_overlaydecor_bottom
            
            add "gui/about_decor_bottom.png":
                alpha 0.3
            text "ABOUT":
                style "gui_overlay_title"
                
        viewport id "vp":
            mousewheel True
            draggable False
            xsize 1200 xalign 0.5
            ysize 860 yalign 0.49
            yinitial 0.0
            
            
            vbox:
                xsize 1050
                spacing 0
                at gui_fade(1.3)
                
                text " "
                text " "

                text config.name.upper() style "history_name_text" text_align 0.5 xalign 0.5
                text "version [config.version!t]\n(c) 2017 [gui.developer_name!t]\n\n Made with Ren'Py [renpy.version_only]":
                    style "history_text"
                    text_align 0.5
                    xalign 0.5
                    
                text " "
                text " "
                
                hbox:
                    spacing 70
                    
                    vbox:
                        spacing 10
                        style_prefix "history"
                        text "{b}HOTKEY{/b}"
                        text "CTRL"
                        text "ESC"
                        text "H"
                        text "B"
                        text "S"
                        text "L"
                        text "A"
                        text "SHIFT+S"
                        
                    vbox:
                        spacing 10
                        style_prefix "history"
                        text "{b}MOUSE{/b}"
                        text " "
                        text "RMB"
                        text "MMB"
                        text "Scroll Up"
                        text " "
                        text " "
                        text " "
                        text " "
                        
                    vbox:
                        spacing 10
                        style_prefix "history"
                        text "{b}DESCRIPTION{/b}"
                        text "Skips dialogue while held down."
                        text "Opens the game menu"
                        text "Hides the user interface."
                        text "Opens the log/history."
                        text "Opens the save menu."
                        text "Opens the load menu."
                        text "Toggles auto forward mode."
                        text "Takes a screenshot."
                        
                text " "
                text " "
                    
        
        ## Add scrollbar.
        vbar:
            value YScrollValue("vp")
            xsize 15
            ysize 686
            xpos 1543
            ypos 189
            
            thumb_shadow None
            
            thumb               "gui/log_idle_thumb.png"
            hover_thumb         "gui/log_idle_thumb.png"
            base_bar            "gui/log_idle_bar.png"
            hover_base_bar      "gui/log_idle_bar.png"
            
            hovered Play("system",guisfx_button_hover)
            
            at gui_buttonfade_enter(1.3)