init offset = -2

transform gui_buttonfade(beginalpha=0.3):
    alpha beginalpha
    on idle:
        linear 0.3 alpha beginalpha
    on selected_idle:
        linear 0.3 alpha 1.0
    on hover:
        linear 0.3 alpha 1.0
    on selected_hover:
        linear 0.3 alpha 1.0
        
transform gui_buttonfade_enter(delaytimer=0.0,duration=0.5,beginalpha=0.3):
    alpha 0.0
    pause delaytimer
    linear duration alpha beginalpha
    on idle:
        linear 0.3 alpha beginalpha
    on hover:
        linear 0.3 alpha 1.0
        
transform gui_saveempty(beginalpha=0.3):
    linear 0.3 alpha beginalpha
    on idle:
        linear 0.3 alpha beginalpha
    on selected_idle:
        linear 0.3 alpha beginalpha
    on hover:
        linear 0.3 alpha 1.0
    on selected_hover:
        linear 0.3 alpha 1.0
        
transform gui_savefull:
    on idle:
        linear 0.3 alpha 1.0
    on selected_idle:
        linear 0.3 alpha 1.0
    on hover:
        linear 0.3 alpha 0.5
    on selected_hover:
        linear 0.3 alpha 0.5

transform gui_savedelete(beginalpha=0.3):
    on idle:
        linear 0.3 alpha beginalpha
    on selected_idle:
        linear 0.3 alpha beginalpha
    on hover:
        linear 0.3 alpha 1.0
    on selected_hover:
        linear 0.3 alpha 1.0
        
transform gui_cgbutton:
    alpha 1.0
    on idle:
        linear 0.3 alpha 1.0
    on hover:
        linear 0.3 alpha 0.3
        
transform gui_cgview:
    alpha 1.0 size(1920,1080)
    xalign 0.5 yalign 0.5
        
transform gui_fade(delaytimer=0.0, duration=0.5,beginalpha=1.0):
    alpha 0.0
    pause delaytimer
    linear duration alpha beginalpha
    
transform gui_fade_inout(delaytimer=0.0, duration=0.5):
    alpha 0.0
    pause delaytimer
    linear duration alpha 1.0
    on hide:
        linear duration alpha 0.0
        
transform gui_fade_out(duration=0.5):
    alpha 1.0
    on hide:
        linear duration alpha 0.0
        
###########
# OVERLAY #
###########

image gui_overlay:
    "gui/choice_overlay.png"
    alpha gui.overlay_opacity
        
transform gui_overlaydecor_top:
    alpha 0.0 
    xalign 0.5 ypos 104
    xoffset -200 yoffset 400
    pause 0.4
    parallel:
        linear 0.3 alpha 0.3
    parallel:
        easein 0.3 xoffset 0
    pause 0.2
    easein 0.5 yoffset 0
        
transform gui_overlaydecor_bottom:
    alpha 0.0 
    xalign 0.5 ypos 967
    xoffset 200 yoffset -400
    pause 0.4
    parallel:
        linear 0.3 alpha 1.0
    parallel:
        easein 0.3 xoffset 0
    pause 0.2
    easein 0.5 yoffset 0
    
define gui_exit_xpos = 1830
define gui_exit_ypos = 25
define gui_exit_parameters = 0.8