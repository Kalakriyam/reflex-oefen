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

    def get_image(self):
        """Get the image from the prompt."""
        if self.prompt == "snorren":
            return rx.window_alert("Hoi schatje, ik wist niet dat jij het was :-)")

        self.processing, self.complete = True, False
        yield
        response = openai_client.images.generate(
            prompt=self.prompt, n=1, size="1024x1024"
        )
        self.image_url = response.data[0].url
        self.processing, self.complete = False, True
    
    def set_greeting(self):
        """Set the greeting with the user's name."""
        self.greeting = f"Hallo {self.name}"
        
    def set_name(self, name):
        """Set the user's name."""
        self.name = name


def index():
    return rx.vstack(
        rx.link("Ga naar Browse", href="/browse"),
        rx.link("Ga naar Conversation", href="/conversation"),
        # First container - Image generation
        rx.center(
            rx.vstack(
                rx.heading("Voice UI", font_size="1.5em"),
                rx.button(
                    "I'll say the text below:",
                    on_click=State.get_image,
                    width="25em",
                    loading=State.processing
                ),
                rx.input(
                    placeholder="Schrijf hier een tekst",
                    on_blur=State.set_prompt,
                    width="25em",
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
            height="40vh",
            bg="linear-gradient(45deg, #ffcccc 0%, #add8e6 100%)",
            margin_top="1em",
        ),
        width="100%",
    )

def browse():
    return rx.text("Browse pagina")

def conversation():
    return rx.text("Conversation pagina")
# Add state and page to the app.
app = rx.App()
app.add_page(index, title="Reflex: Voice UI")
app.add_page(browse, title="Browse pagina")
app.add_page(conversation, title="Conversation pagina")