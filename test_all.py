import pillow_tools


def test_gif_resize():
    pillow_tools.OptimizeToSize('snake.gif', maxWidth=200, maxHeight=200)