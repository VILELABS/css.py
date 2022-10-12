from css import *

css = CSS({
    'body': {
        'background-color': Hex('000000'),
        'color': Hsl(0, 0, 0),
        'font-family': 'Arial',
        'font-size': px(12),
        'font-style': italic,
        'font-weight': bold,
        'text-align': center,
        'text-decoration': underline,
        'text-transform': uppercase,
    },
    'p': {
        'font-size': px(14),
        'font-style': normal,
        'font-weight': normal,
        'text-align': left,
        'text-decoration': none,
        'text-transform': lowercase,
    },
})