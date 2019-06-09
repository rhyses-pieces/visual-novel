init offset = -1

# Limits the history to 200 blocks for performance purposes.
define config.history_length = 200

screen history(fromPause=False):

    tag menu
    style_prefix "history"
    
    # Free up memory. This screen can get large.
    predict False
    
    # Shortcut.
    key "b" action Return()
    key "mouseup_5" action Return()
    key "game_menu" action Return()
    
    fixed:
        if fromPause == False:
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
            
            add "gui/log_decor_bottom.png":
                alpha 0.3
            text "LOG":
                style "gui_overlay_title"
                
        viewport id "vp":
            mousewheel True
            draggable False
            xsize 1200 xalign 0.5
            ysize 860 yalign 0.49
            yinitial 1.0
            
            vbox:
                xsize 1050
                spacing 38
                at gui_fade(1.3)
                
                null height 15

                for h in _history_list:

                    window:
                        xfill True
                        # Make height of entries variable.
                        ysize None
                        
                        # Lays things out properly when ysize = None.
                        has fixed:
                            yfit True

                        if h.who:
                            
                            hbox:
                                spacing 12
                                if varAdvNameUppercase == True:
                                    label h.who.upper() + ".":
                                        style "history_name"

                                        ## Take the color of the who text from the Character, if
                                        ## set.
                                        if "color" in h.who_args:
                                            text_color h.who_args["color"]
                                            
                                else:
                                    label h.who + ".":
                                        style "history_name"
                                        
                                        if "color" in h.who_args:
                                            text_color h.who_args["color"]

                                text h.what
                            
                        else:
                            
                            text h.what
                            

                if not _history_list:
                    text _(gui.message_log_empty):
                        style "history_text"
                        color Color(color=gui.adv_font_color,alpha=0.5)
                    
                null height 30
        
        ## Add scrollbar.
        if _history_list:
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
            
            
        


style history_window is empty

style history_name:
    text_align 1.0
    xsize 300

style history_name_text:
    font gui.advname_font_face
    size gui.advname_font_size
    color gui.advname_font_color
    kerning gui.advname_font_kerning
    
    text_align 1.0
    xalign 1.0
    
style history_text:
    font gui.adv_font_face
    size gui.adv_font_size
    color gui.adv_font_color
    line_leading gui.adv_font_line

style history_label:
    xfill True

style history_label_text:
    xalign 0.5