# ------ Importing the frameworks --------

import customtkinter as ctk

from settings import *


class App(ctk.CTk):

    def __init__(self):
        super().__init__(fg_color=BACKGROUND_COLOR)

        # window setup
        self.title('Spotify Exceed')
        self.geometry(str(WINDOW_WIDTH) + 'x' + str(WINDOW_HEIGHT))
        self.resizable(False, False)
        self.columnconfigure((0, 1, 2, 3),  weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

        # widgets
        Frame(self)
        Entry(self)
        Logo(self)
        EntryTexts(self)

        # mainloop
        self.mainloop()


class Logo(ctk.CTkLabel):

    def __init__(self, parent):
        super().__init__(master=parent,
                         text='',
                         image=LOGO_IMAGE,
                         fg_color=FRAME_COLOR)

        self.place(relx=0.35, rely=0.11)


class Frame(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(master=parent,
                         width=FRAME_WIDTH - 90,
                         height=FRAME_HEIGHT - 101,
                         fg_color=BACKGROUND_COLOR)

        self.image_frame = ctk.CTkLabel(master=parent,
                                        image=FRAME_IMAGE,
                                        text='')

        self.image_frame.place(relx=0.03, rely=0.02)

        self.place(relx=0.3, rely=0.1)


class Entry(ctk.CTkLabel):

    def __init__(self, parent):
        super().__init__(master=parent,
                         fg_color=FRAME_COLOR,
                         image=ENTRY_IMAGE,
                         text='',
                         width=100)

        self.image_entry = ctk.CTkEntry(master=parent,
                                        fg_color=FRAME_COLOR,
                                        border_width=0,
                                        text_color='black')

        self.image_entry.grid(row=1, column=0, padx=100)

        self.grid(row=1, column=0, padx=100)


class EntryTexts(ctk.CTkLabel):

    def __init__(self, parent):
        font = ctk.CTkFont(family="Arial", size=16, weight='bold')
        super().__init__(master=parent,
                         fg_color=FRAME_COLOR,
                         text='     URL',
                         text_color='black',
                         font=font)

        self.place(relx=0.1, rely=0.35)


if __name__ == '__main__':
    App()
