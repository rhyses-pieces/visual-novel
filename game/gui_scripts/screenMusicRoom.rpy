init offset = -1

################
# INSTRUCTIONS #
################

# One and only step!

# Step 1:
# Add your music files in the song_list at line 23.
# Make sure you copy the format of the previous records.

# Check the Ren'Py documentation for more info:
# https://www.renpy.org/doc/html/rooms.html


##############
# BEGIN CODE #
##############

init python:
    
    mr = MusicRoom()
    
    ######## ADD MUSIC FILES HERE ##############
    
    # Add music file references here.
    # The format goes:
    # "path to music file.ogg":['Title', 'Composer']
    # Be sure to add a comma after every item except the last one!
    
    song_list = {"music/silence_min.ogg":['Silence', 'the universe'],
                "music/boil and bubble.ogg":['Boil and Bubble', 'Luna Chai'],
                "music/kid in blue.ogg":['Kid in Blue', 'Luna Chai Li'],
                "music/random encounter.ogg":['Random Encounter', 'Moon Tea']
                }
    
    # This lists default values for song_name and song_description to prevent errors.
    song_name = ""
    song_description = ""
    
    # This automatically adds an mr.add record for every song in the list.
    # Songs are always unlocked while always_unlocked = True.
    for track, detail in song_list.iteritems():
        mr.add(track, always_unlocked = True, action=[SetVariable("song_name",detail[0]),SetVariable("song_description",detail[1])])

##########
# SCREEN #
##########

screen music_room:

    tag menu
    predict False
    key "game_menu" action ShowMenu('extras',fromMain=True,doTrans=False)
    
    add gui.mm_background
    
    fixed:
        at gui_fade_out
            
        add "gui_overlay"
        
        use exit_button(clickaction=ShowMenu('extras',fromMain=True,doTrans=False),doTrans=False)
        
        add "gui/log_decor_top.png" at gui_overlaydecor_top
        
    frame:
        background None
        xsize 1200 
        at gui_overlaydecor_bottom
        
        add "gui/music_decor_bottom.png":
            alpha 0.3
        
        text "MUSIC ROOM":
            style "gui_overlay_title"
            
    frame:
        xsize 439 ysize 572
        xalign 0.5 yalign 0.5
        at gui_fade(1.0)
        
        add "gui/music_playerframe.png" yalign 0.5
        
        add "gui/music_playericon.png" xalign 0.5 yalign 0.2
        
        vbox:
            xalign 0.5 yalign 0.55
            text song_name:
                style "music_sub"
            text song_description.upper():
                style "gui_overlay_title"
                yoffset 0
        
        hbox:
            xalign 0.5 yalign 0.8
            spacing 30
            
            button:
                xsize 71 ysize 96
                at gui_buttonfade
                hovered Play("system",guisfx_button_hover)
                action [Play("system",guisfx_button_click),
                        mr.Previous()
                        ]
                
                add "gui/music_prev.png"
            
            button:
                xsize 71 ysize 96
                at gui_buttonfade
                hovered Play("system",guisfx_button_hover)
                action [Play("system",guisfx_button_click),
                        # Must be mr.Play("string") for
                        # the mr.add action to work.
                        mr.Play(renpy.music.get_playing())
                        ]
                
                add "gui/music_play.png"
            
            button:
                xsize 71 ysize 96
                at gui_buttonfade
                hovered Play("system",guisfx_button_hover)
                action [Play("system",guisfx_button_click),
                        mr.Next()
                        ]
                
                add "gui/music_next.png"
    
    # Make music change upon entering / exiting room.
    on "replace" action Stop("music")
    on "replaced" action Play("music", config.main_menu_music, fadeout=1.0)
    
            
style music_sub:
    font gui.adv_font_face
    size gui.adv_font_size
    color gui.adv_font_color
    
    xalign 0.5
    text_align 0.5