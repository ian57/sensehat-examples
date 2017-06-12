from sense_hat import SenseHat

sense = SenseHat()

O = (0, 255, 0) # Green
X = (0, 0, 0) # Black

creeper_pixels = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, X, X, O, O, X, X, O,
    O, X, X, O, O, X, X, O,
    O, O, O, X, X, O, O, O,
    O, O, X, X, X, X, O, O,
    O, O, X, X, X, X, O, O,
    O, O, X, O, O, X, O, O
]

sense.set_pixels(creeper_pixels)
