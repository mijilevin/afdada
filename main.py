basic.show_number(3)
basic.pause(100)
basic.show_number(2)
basic.pause(100)
basic.show_number(1)
basic.pause(100)
basic.show_leds("""
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    """)

def on_forever():
    pass
basic.forever(on_forever)
