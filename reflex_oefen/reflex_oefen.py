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
    return rx.hstack(
        # Left column - Create/Browse/Edit
        rx.vstack(
            rx.card(
                rx.text("Create", font_size="1.5em"),
                size="2",
                width="90%",
                height="15vh",
                margin_bottom="1em",
                box_shadow="5px 5px 10px rgba(0, 0, 0, 0.09), -5px -5px 10px rgba(255, 255, 255, 0.4)",
                border_radius="8px",
                background="linear-gradient(145deg, #daffda, #c4ecc4)",
            ),
            rx.card(
                rx.text("Browse", font_size="1.5em"),
                size="2",
                width="90%",
                height="15vh",
                margin_bottom="1em",
                box_shadow="5px 5px 10px rgba(0, 0, 0, 0.09), -5px -5px 10px rgba(255, 255, 255, 0.4)",
                border_radius="8px",
                background="linear-gradient(145deg, #daffda, #c4ecc4)",
            ),
            rx.card(
                rx.text("Edit", font_size="1.5em"),
                size="2",
                width="90%",
                height="15vh",
                margin_bottom="1em",
                box_shadow="5px 5px 10px rgba(0, 0, 0, 0.09), -5px -5px 10px rgba(255, 255, 255, 0.4)",
                border_radius="8px",
                background="linear-gradient(145deg, #daffda, #c4ecc4)",
            ),
            align="center",
            justify="center",
            width="33.33%",
            height="100vh",
            bg="linear-gradient(45deg, #ccffcc 0%, #add8e6 100%)",
            padding="2em",
        ),
        
        # Middle column - Live Conversation
        rx.vstack(
            rx.card(
                rx.text("Chat Interface", font_size="1.5em"),
                size="2",
                width="90%",
                height="60%",
                box_shadow="5px 5px 10px rgba(0, 0, 0, 0.09), -5px -5px 10px rgba(255, 255, 255, 0.4)",
                border_radius="8px",
                background="linear-gradient(145deg, #ffdfdf, #ecc4c4)",
            ),
            align="center",
            justify="center",
            width="33.33%",
            height="100vh",
            bg="linear-gradient(45deg, #ffcccc 0%, #add8e6 100%)",
            padding="2em",
        ),
        
        # Right column - Ideate/Organize/Visualize
        rx.vstack(
            rx.card(
                rx.text("Ideate", font_size="1.5em"),
                size="2",
                width="90%",
                height="15vh",
                margin_bottom="1em",
                box_shadow="5px 5px 10px rgba(0, 0, 0, 0.09), -5px -5px 10px rgba(255, 255, 255, 0.4)",
                border_radius="8px",
                background="linear-gradient(145deg, #eddcff, #d4c4e6)",
            ),
            rx.card(
                rx.text("Organize", font_size="1.5em"),
                size="2",
                width="90%",
                height="15vh",
                margin_bottom="1em",
                box_shadow="5px 5px 10px rgba(0, 0, 0, 0.09), -5px -5px 10px rgba(255, 255, 255, 0.4)",
                border_radius="8px",
                background="linear-gradient(145deg, #eddcff, #d4c4e6)",
            ),
            rx.card(
                rx.text("Visualize", font_size="1.5em"),
                size="2",
                width="90%",
                height="15vh",
                margin_bottom="1em",
                box_shadow="5px 5px 10px rgba(0, 0, 0, 0.09), -5px -5px 10px rgba(255, 255, 255, 0.4)",
                border_radius="8px",
                background="linear-gradient(145deg, #eddcff, #d4c4e6)",
            ),
            align="center",
            justify="center",
            width="33.33%",
            height="100vh",
            bg="linear-gradient(45deg, #e6ccff 0%, #add8e6 100%)",
            padding="2em",
        ),
        width="100%",
        height="100vh",
        spacing="0",
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