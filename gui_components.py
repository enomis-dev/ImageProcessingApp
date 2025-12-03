from tkinter import *
from tkinter.ttk import Separator
from PIL import ImageTk, Image
import cv2 as cv
import os
from copy import deepcopy

# import filedialog module
from tkinter import filedialog

from Filters import Filters
import image_processing


class ImageApp(Frame):

    # Constructor
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # Instantiates the vertical separator
        self.separator = None
        # Menu bar
        self.menuBar = None
        # File menu
        self.filemenu = None
        # Edit Menu
        self.editmenu = None
        # Help Menu
        self.helpmenu = None
        # Image Canvas
        self.canvas = None
        # canvas width and heigth
        self.WIDTH_CANVAS = 804
        self.HEIGHT_CANVAS = 654
        # Add buttons
        self.button_filter = None
        self.button_crop = None
        self.button_draw = None
        self.button_hist = None
        self.button_gray = None
        self.button_translate = None
        self.button_rotate = None
        # Original image
        self.original_image = None
        # Processed image
        self.processed_image = None
        # Create Tkinter window
        self.create_window()
        # Create Menu
        self.create_menu()
        # Create Image Viewer
        self.create_widgets()

    # Define window geometry
    def create_window(self):
        self.master.geometry('1200x800')
        self.master.title("Image processing App")
        #self.master.attributes("-fullscreen", True)
        #w, h = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        #self.master.geometry("%dx%d+0+0" % (w, h))
        self.master.resizable(True, True)
        # Separator object
        self.separator = Separator(self.master, orient='vertical')
        self.separator.place(relx=0.2, rely=0, relwidth=0.2, relheight=1.0)
        # Add Filter button
        self.button_filter = Button(self.master, text="Filters", height=3, width=15, bd = 4,  command=self.open_filters_window)
        self.button_filter.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.1)
        # Add Crop button
        self.button_crop = Button(self.master, text="Crop", height=3, width=15, bd = 4)
        self.button_crop.place(relx=0.05, rely=0.17, relwidth=0.1, relheight=0.1)
        # Add Draw button
        self.button_draw = Button(self.master, text="Draw", height=3, width=15, bd = 4)
        self.button_draw.place(relx=0.05, rely=0.29, relwidth=0.1, relheight=0.1)
        # Add Histograms button
        self.button_hist = Button(self.master, text="Histograms", height=3, width=15, bd=4, command=self.show_histograms_command)
        self.button_hist.place(relx=0.05, rely=0.41, relwidth=0.1, relheight=0.1)
        # Add Rotate button
        self.button_rotate = Button(self.master, text="Rotate", height=3, width=15, bd=4, command=self.rotate_command)
        self.button_rotate.place(relx=0.05, rely=0.53, relwidth=0.1, relheight=0.1)
        # Add Translate button
        self.button_translate = Button(self.master, text="Translate", height=3, width=15, bd=4)
        self.button_translate.place(relx=0.05, rely=0.65, relwidth=0.1, relheight=0.1)
        # Add GrayScale conversion button
        self.button_gray = Button(self.master, text="Gray", height=3, width=15, bd=4, command=self.apply_grayscale_command)
        self.button_gray.place(relx=0.05, rely=0.77, relwidth=0.1, relheight=0.1)
        # Add GrayScale conversion button
        self.button_gray = Button(self.master, text="Original image", height=1, width=15, bd=4,
                                  command=self.original)
        self.button_gray.place(relx=0.8, rely=0.1, relwidth=0.15, relheight=0.15)


    # Create horizontal menu
    def create_menu(self):
        self.menuBar = Menu(self.master)
        self.master.config(menu=self.menuBar)
        self.filemenu = Menu(self.menuBar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.donothing)
        self.filemenu.add_command(label="Open", command=self.open_img)
        self.filemenu.add_command(label="Save", command=self.save_img)
        self.filemenu.add_command(label="Save as...", command=self.donothing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close", command=self.on_exit)
        self.menuBar.add_cascade(label="File", menu=self.filemenu)

        self.editmenu = Menu(self.menuBar, tearoff=0)
        self.editmenu.add_command(label="Undo", command=self.donothing)

        self.editmenu.add_separator()

        self.editmenu.add_command(label="Cut", command=self.donothing)
        self.editmenu.add_command(label="Copy", command=self.donothing)
        self.editmenu.add_command(label="Paste", command=self.donothing)
        self.editmenu.add_command(label="Delete", command=self.clear_canvas)
        self.editmenu.add_command(label="Select All", command=self.donothing)

        self.menuBar.add_cascade(label="Edit", menu=self.editmenu)
        self.helpmenu = Menu(self.menuBar, tearoff=0)
        self.helpmenu.add_command(label="Help Index", command=self.donothing)
        self.helpmenu.add_command(label="About...", command=self.donothing)
        self.menuBar.add_cascade(label="Help", menu=self.helpmenu)

    def create_widgets(self):
        self.canvas = Canvas(self.master, bg="gray", width=800, height=650)
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Function to open an image
    def open_img(self):
        # Select the Imagename  from a folder
        try:
            filepath = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("Image",
                                                          "*.bmp*"),
                                                         ("all files",
                                                          "*.*")))
            # If we don't select a file simply return
            if filepath is None:
                return
            self.original_image = cv.imread(filepath)
            self.original_image = cv.cvtColor(self.original_image, cv.COLOR_BGR2RGB)
            self.processed_image = deepcopy(self.original_image)
        except IOError:
            print("Error: Invalid file format")
        self.show_image()

    # Show image function
    def show_image(self):
        # Get image dimensions
        shapes = self.processed_image.shape
        height = shapes[0]
        width  = shapes[1]
        ratio = height / width

        new_width = width
        new_height = height

        # resize the image
        if height > self.HEIGHT_CANVAS or width > self.WIDTH_CANVAS:
            if ratio < 1:
                new_width = self.WIDTH_CANVAS
                new_height = int(new_width * ratio)
            else:
                new_height = self.HEIGHT_CANVAS
                new_width = int(new_height * (width / height))

        self.shown_image = cv.resize(self.processed_image, (new_width, new_height), interpolation=cv.INTER_AREA)

        # PhotoImage class is used to add image to widgets, icons etc
        self.shown_image = ImageTk.PhotoImage(Image.fromarray(self.shown_image))

        # Re-compute the ratio
        self.ratio = height / new_height

        # Add the image to the canvas
        self.canvas.config(width=new_width, height=new_height)
        self.canvas.create_image(new_width / 2, new_height / 2, anchor=CENTER, image=self.shown_image)

    # Function to save the image
    def save_img(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".png",
                                        filetypes=(("PNG file", "*.png"), ("All Files", "*.*")))
        if file is None:
            return
        else:
            abs_path = os.path.abspath(file.name)
            self.img.save(abs_path)

    # TODO function
    def donothing(self):
        filewin = Toplevel(self.master)
        button = Button(filewin, text="TODO")
        button.pack()

    # Function to exit from the application
    def on_exit(self):
        self.quit()

    # Clean the canvas
    def clear_canvas(self):
        self.canvas.delete("all")

    # New command methods to call image_processing functions
    def open_filters_window(self):
        if self.processed_image is not None:
            filters_window = Tk()
            # Pass the current processed image and a reference to update the main app
            app_filters = Filters(master=filters_window, image=self.processed_image)
            filters_window.wait_window(filters_window)
            # After the filter window closes, retrieve the updated image
            updated_image = app_filters.get_processed_image()
            if updated_image is not None:
                self.processed_image = updated_image
                self.show_image()

    def show_histograms_command(self):
        if self.processed_image is not None:
            image_processing.generate_histogram(self.processed_image)
            print('Histograms displayed')

    def rotate_command(self):
        if self.processed_image is not None:
            # For now, hardcode angle, later we can add a dialog for user input
            self.processed_image = image_processing.rotate_image(self.processed_image, 90)
            self.show_image()

    def apply_grayscale_command(self):
        if self.processed_image is not None:
            self.processed_image = image_processing.convert_to_grayscale(self.processed_image)
            self.show_image()

    def original(self):
        self.processed_image = deepcopy(self.original_image)
        print('Update canvas')
        self.show_image()
