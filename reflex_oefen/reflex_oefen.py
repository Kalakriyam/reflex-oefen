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
    image_data = ""

    def get_image(self):
        """Generate an image from the prompt and store it as a base-64 data-URI
        so the frontend receives the actual picture, not an expiring link.
        """
        if self.prompt == "snorren":
            return rx.window_alert("Hoi schatje, ik wist niet dat jij het was :-)")

        # show spinner
        self.processing, self.complete = True, False
        yield

        # OpenAI Python ≥ 1.12 – Images endpoint, return base-64 instead of URL
        response = openai_client.images.generate(
            model="dall-e-3",          # image model – GPT-4.1 is a chat model
            prompt=self.prompt,
            n=1,
            size="1024x1024",
            response_format="b64_json"  # <- this gives you raw image data
        )

        # build a data-URI the <img> tag can display
        b64_png = response.data[0].b64_json
        self.image_data = f"data:image/png;base64,{b64_png}"

        # stop spinner
        self.processing, self.complete = False, True
    
    def set_greeting(self):
        """Set the greeting with the user's name."""
        self.greeting = f"Hallo {self.name}"
        
    def set_name(self, name):
        """Set the user's name."""
        self.name = name

def browse():
    return rx.center(
        rx.card(
            # hier komt je kaart-inhoud
            rx.text("Dit is een mooie kaart"),
            rx.button("Klik hier"),
            padding="20px",
        border_radius="10px",
        box_shadow="0 4px 8px rgba(0,0,0,0.2)",
        bg="white",
        width="400px",  # of wat je wilt
        ),
    width="100%",
    height="100vh",
    bg="#f0f0f0"  # achtergrondkleur van de pagina
    )

def index():
    return rx.vstack(
        rx.hstack(
            rx.link("Ga naar Browse", href="/browse"),
            rx.spacer(),
            rx.link("Ga naar Conversation", href="/conversation"),
            width="100%",
        ),
        # First container - Image generation
        rx.center(
            rx.vstack(
                rx.heading("Voice UI", font_size="1.5em"),
                rx.button(
                    "I'll create an image based on the text below:",
                    on_click=State.get_image,
                    width="25em",
                    loading=State.processing
                ),
                rx.input(
                    placeholder="Schrijf hier een tekst",
                    on_blur=State.set_prompt,
                    width="20em",
                ),
                rx.cond(
                    State.complete,
                    rx.image(src=State.image_url, width="20em"),
                ),
                align="center",
            ),
            width="50%",
            height="40vh",
            bg="linear-gradient(45deg, #ccffcc 0%, #add8e6 100%)",
        ),
        
        # Second container - Conversation
        rx.center(
            rx.vstack(
                rx.heading("Conversation", font_size="1.5em"),
                rx.button(
                    "Choose Voice",
                    width="25em",
                    on_click=State.set_greeting,
                ),
                rx.input(
                    placeholder="Wat is je naam?",
                    on_blur=State.set_name,
                    width="25em",
                ),
                rx.cond(
                    State.greeting != "",
                    rx.text(State.greeting),
                    rx.text(""),
                ),
                align="center",
            ),
            width="50%",
            height="40%",
            bg="linear-gradient(45deg, #ffcccc 0%, #add8e6 100%)",
            margin_top="1em",
            align_self="flex-end",
        ),
        width="100%",
    )

def conversation():
    return rx.text("Conversation pagina")
# Add state and page to the app.
app = rx.App()
app.add_page(index, title="Reflex: Voice UI")
app.add_page(browse, title="Browse pagina")
# app.add_page(conversation, title="Conversation pagina")