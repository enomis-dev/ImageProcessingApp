from tkinter import *
from tkinter.ttk import Separator
from PIL import ImageTk, Image
import cv2 as cv
import os

import image_processing


class Filters(Frame):
    #Constructor
    def __init__(self, master = None, image = None):
        super().__init__(master)
        self.master = master

        # Add buttons
        self.button_sharpen = None
        self.button_blur = None
        self.button_contours = None

        # input image
        self.processed_image = image

        self.create_window()

    # Define window geometry
    def create_window(self):
        self.master.geometry('600x500')
        self.master.title("Filters window")
        #self.master.attributes("-fullscreen", True)
        #w, h = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        #self.master.geometry("%dx%d+0+0" % (w, h))
        #self.master.state('zoomed')
        self.master.resizable(True, True)
        # Add Filter button
        self.button_sharpen = Button(self.master, text="Sharpen", height=3, width=15, bd = 4, command=self.apply_sharpen_filter)
        self.button_sharpen.place(relx=0.5, rely=0.05, relwidth=0.1, relheight=0.1)
        # Add Crop button
        self.button_blur = Button(self.master, text="Blur", height=3, width=15, bd = 4, command=self.apply_blur_filter)
        self.button_blur.place(relx=0.5, rely=0.17, relwidth=0.1, relheight=0.1)
        # Add Draw button
        self.button_contours = Button(self.master, text="Contours", height=3, width=15, bd = 4, command=self.apply_contours_filter)
        self.button_contours.place(relx=0.5, rely=0.29, relwidth=0.1, relheight=0.1)

    # Sharpen the image
    def apply_sharpen_filter(self):
        if self.processed_image is not None:
            self.processed_image = image_processing.apply_sharpen(self.processed_image)
            self.master.destroy()

    # Blur the image
    def apply_blur_filter(self):
        if self.processed_image is not None:
            self.processed_image = image_processing.apply_blur(self.processed_image)
            self.master.destroy()

    # Convert the image to gray and draw contours
    def apply_contours_filter(self):
        if self.processed_image is not None:
            self.processed_image = image_processing.detect_contours(self.processed_image)
            self.master.destroy()

    def get_processed_image(self):
        return self.processed_image
