import reflex as rx
import openai
import dotenv
import os

dotenv.load_dotenv()    

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)


class State(rx.State):
    """The app state."""

    prompt = ""
    image_url = ""
    processing = False
    complete = False
    name = ""
    greeting = ""
    chat_mode = "hidden"
    


# ── 1.  NEW chat_box helper  ─────────────────────────────────────────────
def chat_box() -> rx.Component:
    """Static chat history + text input (no backend)."""
    return rx.vstack(
        rx.scroll_area(
            rx.vstack(
                rx.text("AI:  →  Hallo! Waarmee kan ik helpen?"),
                rx.text("Jij:  →  Gewoon even testen."),
                rx.text("AI:  →  Weet je het zeker?"),
                rx.text("Jij:  →  Natuurlijk, ik weet toch waarom ik deze chat startte?"),
                rx.text("AI:  →  Iets zegt me dat er meer aan de hand is..."),
                rx.text("Jij:  →  ?! Waar heb je het over man?"),
                spacing="3",
            ),
            height="calc(90% - 3.5rem)",
            type="scroll",
            scrollbars="vertical",
            px="0.5em",
            # pb="2em",
            # style={"flex": 1},
        ),
        

        spacing="1", # only 0, 1, 2, etc are allowed. No decimals, no 'em'
        height="100%",
        width="90%",
        pb="2px",
        # justify="start",
    )

def index():
    return rx.hstack(
        # Left column - Create/Continue
        rx.vstack(
            rx.card(
                rx.text("Create", font_size="1.5em"),
                size="2",
                width="90%",
                height="30vh",
                margin_bottom="2em",
                box_shadow="5px 5px 10px rgba(0, 0, 0, 0.09), -5px -5px 10px rgba(255, 255, 255, 0.4)",
                border_radius="10px",
                background="linear-gradient(145deg, #ccffd8, #b8e6c2)",
            ),
            rx.card(
                rx.text("Continue", font_size="1.5em"),
                size="2",
                width="90%",
                height="30vh",
                margin_bottom="0em",
                box_shadow="5px 5px 10px rgba(0, 0, 0, 0.09), -5px -5px 10px rgba(255, 255, 255, 0.4)",
                border_radius="10px",
                background="linear-gradient(145deg, #d8ffcc, #c2e6b8)",
            ),
            align="end",
            justify="center",
            width="30%",
            height="100vh",
            # bg="linear-gradient(45deg, #ccffcc 0%, #add8e6 100%)",
            padding="2em",
        ),
        
        # Middle column - Conversate (should be 'exchange')
        rx.vstack(
            rx.card(
                rx.text("Conversate", font_size="1.5em"),

                # fade-in / fade-out purely with pseudo styles
                rx.box(
                    chat_box(),
                    opacity=0,
                    transition="opacity 0.25s ease",
                    _hover={"opacity": 1},
                    _focus_within={"opacity": 1},
                    height="80%",
                    width="100%",
                    border="1px solid black",
                ),
                rx.divider(), # sharp line at the bottom of the message history
                rx.input(
                    placeholder="Type …",
                    width="100%",
                    
                    # px="1em",
                    # style={"paddingBottom": "2em"},
                ),
                size="2",
                width="90%",
                height="80%",
                box_shadow="5px 5px 10px rgba(0,0,0,0.09), -5px -5px 10px rgba(255,255,255,0.4)",
                # border="1px solid black",
                border_radius="10px",
                background="linear-gradient(145deg, #ffdfcc, #e6c8b8)",
            ),
            align="center",
            justify="center",
            width="40%",
            height="100vh",
            # bg="linear-gradient(45deg, #ffcccc 0%, #add8e6 100%)",
            padding="2em",
        ),
        
        # Right column - Ideate/Find
        rx.vstack(
            rx.card(
                rx.text("Ideate", font_size="1.5em"),
                size="2",
                width="90%",
                height="30vh",
                margin_bottom="2em",
                box_shadow="5px 5px 10px rgba(0, 0, 0, 0.09), -5px -5px 10px rgba(255, 255, 255, 0.4)",
                border_radius="10px",
                background="linear-gradient(145deg, #d8ccff, #c2b8e6)",
            ),
            rx.card(
                rx.text("Find", font_size="1.5em"),
                size="2",
                width="90%",
                height="30vh",
                margin_bottom="0em",
                box_shadow="5px 5px 10px rgba(0, 0, 0, 0.09), -5px -5px 10px rgba(255, 255, 255, 0.4)",
                border_radius="10px",
                background="linear-gradient(145deg, #ccccff, #b8b8e6)",
            ),
            align="start",
            justify="center",
            width="30%",
            height="100vh",
            # bg="linear-gradient(45deg, #e6ccff 0%, #add8e6 100%)",
            padding="2em",
        ),
        width="100%",
        height="100vh",
        spacing="0",
        bg="linear-gradient(45deg, #ccffcc 0%, #add8e6 100%)",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index, title="Reflex: Voice UI")