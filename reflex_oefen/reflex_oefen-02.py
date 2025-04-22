import reflex as rx


class State(rx.State):
    """App state."""
    name: str = ""
    greeted: bool = False

    # runs for BOTH Enter‑key and button click
    def handle_submit(self, form_data: dict):
        self.name = form_data.get("name", "")
        if self.name.strip():
            self.greeted = True

    @rx.var
    def greeting(self) -> str:
        return f"Hello {self.name}"


def index() -> rx.Component:
    return rx.center(
        rx.form(                               # ← puts input & button in same form
            rx.vstack(
                rx.input(
                    name="name",               # name needed for form_data dict
                    placeholder="What is your name?",
                    width="20em",
                    on_change=State.set_name,
                ),
                rx.button(
                    "Submit",
                    type="submit",             # button now submits the form
                    width="10em",
                ),
                rx.cond(
                    State.greeted,
                    rx.text(State.greeting, font_size="2em"),
                ),
                align="center",
            ),
            on_submit=State.handle_submit,     # Enter OR click end up here
        ),
        width="100%",
        height="100vh",
    )


app = rx.App()
app.add_page(index, title="Hello Name")