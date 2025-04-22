import reflex as rx

class State(rx.State):
    """No dynamic state needed for Hello World."""

def index():
    # A centered greeting.
    return rx.center(
        rx.text("Hello, world!", font_size="2em"),
        width="100%",
        height="100vh",
    )

app = rx.App()
app.add_page(index, title="Hello World")