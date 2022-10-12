import os, sys, json
import numpy as np
filename = 'stylesheet.csspy.css'
def CSS(dictionary): # CSS
    css = ''
    for key, value in dictionary.items():
        css += key + ' {'
        for k, v in value.items():
            css += k + ': ' + v + ';'
        css += '}'
        css += '\n'
    with open(filename, 'w') as f:
        f.write(css)

def Hex(color): # HEX color
    return '#' + color

def Hsl(h, s, l): # HSL color
    return 'hsl(%d, %d%%, %d%%)' % (h, s, l)

def Rgb(r, g, b): # RGB color
    return 'rgb(%d, %d, %d)' % (r, g, b)

def Rgba(r, g, b, a): # RGBA color
    return 'rgba(%d, %d, %d, %d)' % (r, g, b, a)

def Hsla(h, s, l, a): # HSLA color
    return 'hsla(%d, %d%%, %d%%, %d)' % (h, s, l, a)

def Hsv(h, s, v): # HSV color
    return 'hsv(%d, %d%%, %d%%)' % (h, s, v)

def Hsva(h, s, v, a): # HSVA color
    return 'hsva(%d, %d%%, %d%%, %d)' % (h, s, v, a)

def px(value): # Pixels
    return str(value) + 'px'
bold = 'bold' # font-weight bold
bolder = 'bolder' # font-weight bolder
lighter = 'lighter' # font-weight lighter
normal = 'normal' # font-weight normal
italic = 'italic' # font-style italic
oblique = 'oblique' # font-style oblique
underline = 'underline' # text-decoration underline
overline = 'overline' # text-decoration overline
line_through = 'line-through' # text-decoration line-through
none = 'none' # text-decoration none
capitalize = 'capitalize' # text-transform capitalize
uppercase = 'uppercase' # text-transform uppercase
lowercase = 'lowercase' # text-transform lowercase
inherit = 'inherit' # text-transform inherit
initial = 'initial' # text-transform initial
unset = 'unset' # text-transform unset
left = 'left' # text-align left
right = 'right' # text-align right
center = 'center' # text-align center
justify = 'justify' # text-align justify
justify_all = 'justify-all' # text-align justify-all
start = 'start' # text-align start
end = 'end' # text-align end
match_parent = 'match-parent' # text-align match-parent
inherit = 'inherit' # text-align inherit
initial = 'initial' # text-align initial

