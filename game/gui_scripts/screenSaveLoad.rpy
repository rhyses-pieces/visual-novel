init offset = -1

screen save(fromPause=False):

    tag menu
    
    key "s" action Return()
    key "game_menu" action Return()

    use file_slots(_("Save"),fromPause=fromPause)


screen load(fromPause=False,fromMain=False):

    tag menu
    
    key "l" action Return()
    key "game_menu" action Return()
    
    if fromMain:
        add gui.mm_background

    use file_slots(_("Load"),fromPause=fromPause)


screen file_slots(title,fromPause=False):
    
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    
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
            
            add "gui/saveload_decor_bottom.png":
                alpha 0.3
            
            if title == _("Save"):
                text "SAVE":
                    style "gui_overlay_title"
            else:
                text "LOAD":
                    style "gui_overlay_title"

        ## The grid of file slots.
        grid 3 2:
            style_prefix "slot"

            xalign 0.5
            yalign 0.59

            spacing 30
            
            at gui_fade(1.0)

            for i in range(3 * 2):

                $ slot = i + 1

                button:
                    hovered Play("system",guisfx_button_hover)
                    if FileLoadable(slot) == True:
                        action [Play("system",guisfx_button_warn),
                                FileAction(slot)]
                    else:
                        action [Play("system",guisfx_button_click),
                            FileAction(slot)]
                    
                    xalign 0.5
                    xsize 400 ysize 300
                    
                    if FileLoadable(slot) == True:
                        at gui_savefull
                    else:
                        at gui_saveempty
                    
                    # Add screenshot.
                    add FileScreenshot(slot):
                        xalign 0.5
                        size (333,187)
                        yalign 0.35
                        
                    # Add button. Needs to be above screenshot.
                    add "gui/saveload_file_idle.png":
                        xalign 0.5
                    
                    # File number.
                    text "#" + FileSlotName(slot,6,quick=u'Q'):
                        style "slot_number_text"
                        xalign 0.5 yalign 0.5 yoffset -124
                    
                    # File time.
                    text FileTime(slot, format=_("%B %d, %Y\n%I:%M %p"), empty=_("Empty")):
                        style "slot_time_text"
                        xalign 0.5 yalign 0.0 yoffset 230
                        
                        # {#file_time}%A - Day of the week
                    
                    # Add delete button.
                    if FileLoadable(slot) == True:
                        button:
                            hovered [Play("system",guisfx_button_hover),
                                    Show("file_savedelete",slot=slot)]
                            unhovered Hide("file_savedelete")
                            action [Play("system",guisfx_button_warn),
                                    FileDelete(slot)]
                            
                            xsize 17 ysize 17
                            xalign 0.9 yalign 0.043
                            
                            background "gui/saveload_delete_idle.png"
                            
                            at gui_savedelete
                    

        ## Page navigation buttons.
        hbox:
            xalign 0.5
            ypos 174
            ysize 50

            spacing 18
            
            at gui_fade(1.0)
            
            #textbutton _("<") action FilePagePrevious()
            
            text "PAGE.":
                style "page_text"

            #if config.has_autosave:
            #    textbutton _("{#auto_page}A") action FilePage("auto"):
            #        text_style "page_text"

            if config.has_quicksave:
                textbutton _("{#quick_page}Q"):
                    text_style "page_text"
                    
                    hovered Play("system",guisfx_button_hover)
                    action [Play("system",guisfx_button_click),
                            FilePage("quick")]
                    
                    at gui_buttonfade_enter(1.0)

            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 10):
                textbutton "[page]":
                    text_style "page_text"
                    
                    hovered Play("system",guisfx_button_hover)
                    action [Play("system",guisfx_button_click),
                            FilePage(page),
                            Function(renpy.restart_interaction)]
                    
                    #if page ==:
                    #    at gui_fade(1.0)
                    #else:
                    at gui_buttonfade
            
            #if FileCurrentPage() is not 5:
            #    textbutton _(">") action FilePageNext()

screen file_savedelete(slot):
    textbutton "DELETE?":
        text_style "caption_small"
        text_align 1.0 xanchor 1.0
        
        if slot == 1:
            xpos 670 ycenter 300
        if slot == 2:
            xpos 1100 ycenter 300
        if slot == 3:
            xpos 1530 ycenter 300
        if slot == 4:
            xpos 670 ycenter 631
        if slot == 5:
            xpos 1100 ycenter 631
        if slot == 6:
            xpos 1530 ycenter 631
        
        at gui_fade_inout(0.0,0.3)

style page_text:
    font gui.adv_font_face
    size gui.adv_font_size
    color gui.adv_font_color
    bold True
    
    xalign 0.5 yalign 0.5
    
style page_textbutton:
    xalign 0.5 yalign 0.5

style slot_time_text:
    font gui.adv_font_face
    size gui.adv_font_size * 0.8
    color gui.adv_font_color
    line_spacing 0 - gui.adv_font_size * 0.25
    
    text_align 0.5
    
style slot_number_text:
    font gui.adv_font_face
    size gui.adv_font_size * 0.7
    color gui.adv_font_color
    bold True
    
    kerning gui.advname_font_kerning

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"

style page_button:
    xalign 0.5