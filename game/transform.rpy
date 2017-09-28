# All the transforms go into this file

transform from_right(easein_time=3.0, pause_time=3, xdestination=0.5):
    subpixel True
    alpha 0.0 xalign 1.0 xanchor 0.0
    pause_time
    parallel:
        easein easein_time alpha 1.0
    parallel:
        easein easein_time xalign xdestination
    on hide:
        alpha 1 zoom 1 xanchor xdestination
        block:
            linear 0.1 zoom 1.1
            linear 0.5 zoom 0

transform from_left(easein_time=3.0, pause_time=0, xdestination=0.5):
    subpixel True
    alpha 0.0 xalign 0.0 xanchor 0.0
    pause_time
    parallel:
        easein easein_time alpha 1.0
    parallel:
        easein easein_time xalign xdestination
    on hide:
        alpha 1 zoom 1 xanchor xdestination
        block:
            linear 0.1 zoom 1.1
            linear 0.5 zoom 0

transform from_top(easein_time=3.0, pause_time=0, ydestination=0.5):
    subpixel True
    alpha 0.0 yalign 0.0 yanchor 0.0
    pause_time
    parallel:
        easein easein_time alpha 1.0
    parallel:
        easein easein_time yalign ydestination
    on hide:
        alpha 1 zoom 1 yanchor ydestination
        block:
            linear 0.1 zoom 1.1
            linear 0.5 zoom 0

transform elastic_splash(zoom_value=1.0, rotate_value=-3.0, time_value=0.0):
    alpha 0.0
    zoom 4.0
    time time_value
    subpixel True
    alpha 1.0
    linear 0.2 zoom zoom_value
    pause 1
    easein_elastic 1.5 rotate rotate_value
    on hide:
        easein 1.0 yalign 1.0

transform zoom(zoom_value):
    zoom zoom_value

transform rotate(value):
    rotate_pad True
    rotate value