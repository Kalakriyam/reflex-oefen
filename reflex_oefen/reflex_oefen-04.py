import reflex as rx


class State(rx.State):
    submitted_name: str = ""

    def handle_submit(self, form_data: dict):
        name = form_data.get("name", "").strip()
        if name:
            self.submitted_name = name

    def clear_name(self):
        self.submitted_name = ""

    @rx.var
    def greeting(self) -> str:
        return f"Hello {self.submitted_name}"


def index() -> rx.Component:
    return rx.center(
        rx.form(
            rx.vstack(
                rx.input(
                    name="name",
                    placeholder="What is your name?",
                    width="20em",
                ),
                rx.hstack(                     # ← uses token spacing "3"
                    rx.button(
                        "Submit",
                        type="submit",
                        width="10em",
                        transition="transform 300ms ease",
                        _hover={"transform": "scale(1.15)"},
                        
                    ),
                    rx.button(
                        "Clear",
                        type="button",
                        width="10em",
                        on_click=State.clear_name,
                    ),
                    spacing="3",              # tokens 0‑9 only
                ),
                rx.cond(
                    State.submitted_name != "",
                    rx.text(State.greeting, font_size="2em"),
                ),
                align="center",
            ),
            on_submit=State.handle_submit,
        ),
        width="100%",
        height="100vh",
        # background_image="linear-gradient(to top right, darkblue 0%, black 100%)",
        background_color="darkblue",
    )


app = rx.App()
app.add_page(index, title="Hello Name")