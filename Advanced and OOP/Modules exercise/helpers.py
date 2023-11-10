from canvas import app


def cleans_screen():
    for el in app.grid_slaves():
        el.destroy()
