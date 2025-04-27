# app.py – layout tweaked for "designer-level" proportions
import reflex as rx
from typing import List

# ----------  theme ---------- #
COLORS = {
    "primary": "#1A365D",
    "secondary": "#2A4365",
    "accent": "#3182CE",
    "background": "#F7FAFC",
    "text": "#1A202C",
}

# ----------  spacing & size constants ---------- #
INNER_BOX_SPACING = "1.75rem"     # space between boxes inside a column
COLUMN_GAP = "2rem"          # space between the three columns (reduced slightly)
PAGE_HORIZONTAL_PAD = "clamp(1rem, 4vw, 3rem)"  # adjusted padding

# ----------  shared styles ---------- #
COLUMN_STYLE = {
    # "border_radius": "1rem", # Removed for seamless columns
    "padding": "1.75rem",
    "height": "100%",
    "spacing": INNER_BOX_SPACING, # Use spacing for vstack
}

BOX_STYLE = {
    "background_color": "rgba(255, 255, 255, 0.9)", # Slightly transparent white
    "padding": "1.5rem",
    "border_radius": "0.5rem",
    "box_shadow": "0 3px 8px rgba(0, 0, 0, 0.08)",
    "width": "100%", # Ensure boxes take full width of vstack
}

BOX_TITLE_STYLE = {
    "font_size": "1.5rem",
    "font_weight": "600",
    "margin_bottom": "0.5rem",
    "color": COLORS["text"],
}

# ----------  helpers ---------- #
def content_box(title: str, flex_grow: int = 1) -> rx.Component:
    """Reusable box with title and placeholder body."""
    return rx.box(
        rx.heading(title, style=BOX_TITLE_STYLE),
        rx.text("Box content placeholder"),
        style=BOX_STYLE,
        flex_grow=flex_grow, # Use flex_grow for vertical sizing within vstack
    )

# ----------  page ---------- #
def index() -> rx.Component:
    # Define Gradients
    left_gradient = "linear-gradient(135deg, #48BB78 0%, #38A169 100%)" # Green
    middle_gradient = "linear-gradient(135deg, #00C6FB 0%, #005BEA 100%)" # Blue (prev right)
    right_gradient = "linear-gradient(135deg, #6B46C1 0%, #B794F4 100%)" # Purple (prev middle)

    return rx.container(
        rx.flex(
            # Left Column (VStack)
            rx.vstack(
                content_box("Create", flex_grow=1),
                content_box("Continue", flex_grow=1),
                background=left_gradient,
                style=COLUMN_STYLE,
                flex_basis="0", # Allow shrinking
                flex_grow=1,  # Grow equally initially
            ),
            # Middle Column (VStack)
            rx.vstack(
                content_box("Conversation", flex_grow=1),
                background=middle_gradient,
                style=COLUMN_STYLE,
                flex_basis="0",
                flex_grow=1.8, # Grow wider
            ),
            # Right Column (VStack)
            rx.vstack(
                content_box("Ideate", flex_grow=1),
                content_box("Find", flex_grow=1),
                background=right_gradient,
                style=COLUMN_STYLE,
                flex_basis="0",
                flex_grow=1,
            ),
            direction={"initial": "column", "md": "row"}, # Stack vertically on small/medium, row on large
            height="100%",  # fills container height
            width="100%",   # fills container width
            align_items="stretch", # Ensure vstacks take full height
        ),
        max_width="100%",
        width="100%", # Explicitly set width
        padding="0", # Explicitly set padding to 0
        margin="0", # Explicitly set margin to 0
        height="100%",
        background_color=COLORS["background"],
        color=COLORS["text"],
    )


# ----------  app ---------- #
app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
    ],
    style={
        "font_family": "'Inter', sans-serif",
        "background_color": COLORS["background"],
        "color": COLORS["text"],
    },
)

app.add_page(index)
