from PIL import Image
import customtkinter as ctk

# ------ All constants is here ---------

# colors
BACKGROUND_COLOR = '#007A5B'
FRAME_COLOR = '#00cc99'

# window/frame settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

LOGO_WIDTH = 256
LOGO_HEIGHT = 120

FRAME_WIDTH = 750
FRAME_HEIGHT = 566

ENTRY_WIDTH = 200
ENTRY_HEIGHT = 75
# images
LOGO_IMAGE = ctk.CTkImage(Image.open(r'images/Logo.png'), size=(LOGO_WIDTH, LOGO_HEIGHT))
FRAME_IMAGE = ctk.CTkImage(Image.open(r'images/Frame.png'), size=(FRAME_WIDTH, FRAME_HEIGHT))
ENTRY_IMAGE = ctk.CTkImage(Image.open(r'images/Neon Entry.png'), size=(ENTRY_WIDTH, ENTRY_HEIGHT))

