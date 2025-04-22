# probleem met donkere balk, en de input velden zijn niet goed leesbaar
import reflex as rx


class State(rx.State):
    submitted_name: str = ""

    # ---------- handlers ----------
    def handle_submit(self, form_data: dict):
        name = form_data.get("name", "").strip()
        if name:
            self.submitted_name = name

    def clear_name(self):
        self.submitted_name = ""

    # ---------- computed ----------
    @rx.var
    def greeting(self) -> str:
        return f"Hello {self.submitted_name}"


def login_card() -> rx.Component:
    """The neumorphic login form."""
    return rx.form(
        rx.vstack(
            rx.heading("Login", size="5"),
            rx.input(
                name="name",
                placeholder="Username",
                width="100%",
                class_name="neumorphic neumorphic-input",
            ),
            rx.input(
                name="password",
                placeholder="Password",
                type_="password",
                width="100%",
                class_name="neumorphic neumorphic-input",
            ),
            rx.hstack(
                rx.button(
                    "Submit",
                    type="submit",
                    width="8em",
                    class_name="neumorphic neumorphic-button",
                ),
                rx.button(
                    "Clear",
                    type="button",
                    width="8em",
                    class_name="neumorphic neumorphic-button",
                    on_click=State.clear_name,
                ),
                spacing="3",                       # Radix spacing token
            ),
            rx.cond(
                State.submitted_name != "",
                rx.text(State.greeting,
                        font_size="1.5em",
                        margin_top="1em"),
            ),
            align="center",
            width="300px",
            class_name="neumorphic neumorphic-card",
        ),
        on_submit=State.handle_submit,
    )


def index() -> rx.Component:
    # extra rx.center so it stays centered even if CSS fails to load
    return rx.center(login_card(), width="100%", height="100vh")


# -------- app --------
app = rx.App(
    stylesheets=["neumorphic.css"],   # <link> injected automatically
)
app.add_page(index, title="Neumorphic Login")
