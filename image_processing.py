import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def apply_blur(image: np.ndarray) -> np.ndarray:
    """Applies a Gaussian blur filter to the image."""
    return cv.GaussianBlur(image, (7, 7), 0)

def detect_contours(image: np.ndarray) -> np.ndarray:
    """Detects contours in the image using the Canny edge detector."""
    # Convert to grayscale if not already
    if len(image.shape) == 3:
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return cv.Canny(image, 150, 175)

def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """Converts the image to grayscale."""
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def rotate_image(image: np.ndarray, angle: float, rot_point: tuple = None) -> np.ndarray:
    """Rotates the image by a given angle around a specified point."""
    (height, width) = image.shape[:2]
    if rot_point is None:
        rot_point = (width // 2, height // 2)
    
    rotMat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(image, rotMat, dimensions)

def apply_sharpen(image: np.ndarray) -> np.ndarray:
    """Applies a sharpening filter to the image."""
    # Placeholder for sharpen logic
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    return cv.filter2D(image, -1, kernel)

def generate_histogram(image: np.ndarray):
    """Generates and displays color histograms for the image."""
    plt.figure()
    plt.title('Colour Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')
    colors = ('b', 'g', 'r')
    # If the image is grayscale, plot a single histogram
    if len(image.shape) == 2 or image.shape[2] == 1:
        hist = cv.calcHist([image], [0], None, [256], [0, 256])
        plt.plot(hist, color='gray')
        plt.xlim([0, 256])
    else:
        for i, col in enumerate(colors):
            hist = cv.calcHist([image],[i], None, [256], [0, 256])
            plt.plot(hist, color=col)
            plt.xlim([0, 256])
    plt.show()
