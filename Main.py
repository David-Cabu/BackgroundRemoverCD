import customtkinter as ctk
import AppGraphics as graphics


if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    app = graphics.App()
    app.after(0, lambda: app.state('zoomed'))
    app.mainloop()