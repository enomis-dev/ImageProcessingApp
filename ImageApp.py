from tkinter import Tk
from gui_components import ImageApp

def main():
    root = Tk()
    app = ImageApp(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()
