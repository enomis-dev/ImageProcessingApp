# ImageProcessingApp

A simple desktop application for basic image processing tasks, built with Python's Tkinter, Pillow, Matplotlib, and OpenCV. This application allows users to open, view, and apply various transformations and filters to images.

![ImageProcessingApp](https://github.com/SimoneDeGasperis/ImageProcessingApp/assets/36958248/
b5058d4f-c395-4d4d-8f55-e592f6671009)

## Features

*   **Open and Save Images:** Load images from your local file system and save processed images.
*   **Image Display:** View images within the application window.
*   **Basic Transformations:**
    *   Grayscale Conversion
    *   Rotation
*   **Image Filters:**
    *   Blur
    *   Contour Detection
*   **Histograms:** Display color histograms of the active image.

## Installation

To get started with the ImageProcessingApp, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/SimoneDeGasperis/ImageProcessingApp.git
    cd ImageProcessingApp
    ```

2.  **Create and activate a virtual environment:**

    It's recommended to use a virtual environment to manage dependencies.

    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    Install the required Python packages from `pyproject.toml` in editable mode. This will install all declared dependencies.

    ```bash
    pip install -e .
    ```

## Usage

To run the application, ensure your virtual environment is activated and then execute the `ImageApp.py` file:

```bash
python ImageApp.py
```

## How to Use

1.  **Open an Image:**
    *   Go to `File > Open` from the menu bar.
    *   Select an image file (e.g., `.bmp`, `.jpg`, `.png`).
2.  **Apply Filters/Transformations:**
    *   Use the buttons on the left panel (e.g., "Filters", "Gray", "Rotate") to apply various operations.
    *   For filters, a new window might appear to select specific filter options.
3.  **View Histograms:**
    *   Click the "Histograms" button to display the color histograms of the current image.
4.  **Save Image:**
    *   Go to `File > Save` to save the processed image.



