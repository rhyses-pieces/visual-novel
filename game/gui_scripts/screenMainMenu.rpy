## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu
    
    add gui.mm_background

    fixed:
        xsize 467 ysize 1080
        xalign 0.85 yalign 1.0
        
        add "gui/mm_overlay.png" yalign 1.0
    
        vbox:
            spacing 25
            xsize 467 yalign 0.75
            
            button:
                style "mm_button"
                at gui_buttonfade
                
                hovered Play("system",guisfx_button_hover)
                action [Play("system",guisfx_button_click),
                        Start()]
                
                add "gui/mm_start_idle.png" at mm_button_line
                text "Start" style "mm_button_text"
            
            button:
                style "mm_button"
                at gui_buttonfade
                
                hovered Play("system",guisfx_button_hover)
                action [Play("system",guisfx_button_click),
                        ShowMenu('load',fromMain=True)]
                
                add "gui/mm_load_idle.png" at mm_button_line
                text "Load" style "mm_button_text"
        
            button:
                style "mm_button"
                at gui_buttonfade
                
                hovered Play("system",guisfx_button_hover)
                action [Play("system",guisfx_button_click),
                        ShowMenu('settings',fromMain=True)]
                
                add "gui/mm_settings_idle.png" at mm_button_line
                text "Settings" style "mm_button_text"
            
            if gui.has_cg or gui.has_mr:
                button:
                    style "mm_button"
                    at gui_buttonfade
                
                    hovered Play("system",guisfx_button_hover)
                    action [Play("system",guisfx_button_click),
                            ShowMenu('extras',fromMain=True)]
                
                    add "gui/mm_extras_idle.png" at mm_button_line
                    text "Extras" style "mm_button_text"
        
            button:
                style "mm_button"
                at gui_buttonfade
                
                hovered Play("system",guisfx_button_hover)
                action [Play("system",guisfx_button_click),
                        Quit()]
                
                add "gui/mm_quit_idle.png" at mm_button_line
                text "Quit" style "mm_button_text"
        
    hbox:
        spacing 20
        xcenter 0.84 ycenter 0.95
        
        button:
            xsize 31 ysize 42
            at gui_buttonfade
            
            hovered Play("system",guisfx_button_hover)
            action [Play("system",guisfx_button_warn),
                    Confirm("Are you sure? This will direct you to a website.",OpenURL(gui.developer_site),no=None)]
            
            add "gui/mm_site_idle.png"
        
        button:
            xsize 23 ysize 43 yoffset -1
            at gui_buttonfade
            
            hovered Play("system",guisfx_button_hover)
            action [Play("system",guisfx_button_click),
                    ShowMenu('about')]
            
            add "gui/mm_help_idle.png"
                
    add gui.mm_logo xcenter 0.769 ycenter gui.mm_logoy


style mm_button:
    xalign 0.5
    xsize 200 ysize 50

style mm_button_text:
    font gui.adv_font_face
    size gui.adv_font_size
    color gui.adv_font_color
    kerning gui.advname_font_kerning
    bold True
    
    text_align 0.5
    xalign 0.5
    
transform mm_button_line:
    xalign 0.5 yoffset 40