import reflex as rx


class State(rx.State):
    sentence_draft: str = ""
    name_draft: str = ""
    sentence: str = ""
    name: str = ""

    # ------------ handlers ------------
    def submit(self, form_data: dict):
        self.sentence = self.sentence_draft.strip()
        self.name = self.name_draft.strip()

    def clear(self):
        self.sentence_draft = ""
        self.name_draft = ""
        self.sentence = ""
        self.name = ""

    # ------------ computed ------------
    @rx.var
    def greeting(self) -> str:
        if self.sentence and self.name:
            return f"{self.sentence}, {self.name}!"
        return ""


def card() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Greetings Generator", size="5"),
            rx.input(
                name="sentence",
                placeholder="Enter a greeting sentence",
                on_change=State.set_sentence_draft,
                width="100%",
                class_name="neumorphic neumorphic-input",
            ),
            rx.input(
                name="name",
                placeholder="Enter a name",
                on_change=State.set_name_draft,
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
                    on_click=State.clear,
                ),
                spacing="3",
            ),
            rx.cond(
                State.greeting != "",
                rx.text(State.greeting, font_size="1.8em", margin_top="1em"),
            ),
            align="center",
            width="340px",
            class_name="neumorphic neumorphic-card",
        ),
        on_submit=State.submit,
    )

def index() -> rx.Component:
    return rx.center(
        card(),
        width="100%",
        height="100vh",
        justify="center",  # Ensures horizontal centering
        align="center",    # Ensures vertical centering
        background_color="var(--bg)"
    )


app = rx.App(stylesheets=["neumorphic_final.css"])
app.add_page(index, title="Greetings Generator")