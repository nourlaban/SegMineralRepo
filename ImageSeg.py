import tkinter as tk
from tkinter import filedialog
import rasterio
from PIL import Image, ImageTk  # Import PIL for image display
import numpy as np  # Import NumPy for array manipulation

import numpy as np
import cv2
import matplotlib.pyplot as plt

def upload_image():
    global image_data  # Use a global variable to store image data
    file_path = filedialog.askopenfilename(title="Select Image File (6 bands)", filetypes=[("TIF files", "*.tif *.tiff")])
    if file_path:
        try:
            with rasterio.open(file_path) as src:
                image_data = src.read()  # Read all bands at once
                print("Image uploaded successfully!")
                print("Number of bands:", image_data.shape[0])

        except Exception as e:
            print(f"Error reading image: {e}")

def filter_and_print_image():
    global image_data
    if image_data is None or image_data.shape[0] != 6:
        print("Error: No image data loaded or incorrect number of bands.")
        return

    try:
        # Select any 3 bands for RGB display (modify these indices as needed)
        red_band = image_data[0]
        green_band = image_data[1]
        blue_band = image_data[2]

        # Create an RGB image by stacking the selected bands
        rgb_image = np.dstack((red_band, green_band, blue_band))

        # Display the RGB image
        display_image(rgb_image)

    except Exception as e:
        print(f"Error filtering image: {e}")

def display_image(img):
    # Convert NumPy array to a format compatible with tkinter
    
    img = Image.fromarray(img.astype('uint8'))
    img_tk = ImageTk.PhotoImage(img)

    # Create a new tkinter window to display the image
    window = tk.Toplevel()
    window.title("Filtered Image")

    # Add a label to display the image with some styling
    label = tk.Label(window, image=img_tk, bg="white", padx=20, pady=20)
    label.pack()

    # Keep a reference to the image to prevent it from being garbage collected
    label.image = img_tk


def pseudo_coloring():
    

    # Define a color map for your classes
    file_path = filedialog.askopenfilename(title="Select Image File (6 bands)", filetypes=[("TIF files", "*.tif *.tiff")])
    class_colors = {
        0: (0, 0, 0),    # Class 0: Black
        1: (255, 0, 0),  # Class 1: Red
        2: (0, 255, 0),  # Class 2: Green
        3: (0, 0, 255),  # Class 3: Blue
        # Add more classes and colors as needed
        4: (255, 0, 255),
        6: (0, 0, 255),
        13:(0, 255, 255),
        16: (30, 80, 255),
        100:(0, 100, 255) 
    }

    # Load your classified image
    classified_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    unique_values  = np.unique(classified_image)

    # Create an empty pseudo-RGB image
    pseudo_rgb_image = np.zeros((classified_image.shape[0], classified_image.shape[1], 3), dtype=np.uint8)

    # Map class labels to colors
    for class_label, color in class_colors.items():
        pseudo_rgb_image[classified_image == class_label] = color

    # Save or display the pseudo-RGB image
    #cv2.imwrite('pseudo_rgb_image.png', pseudo_rgb_image)
   
    

    # Load the pseudo-RGB image
    #pseudo_rgb_image = cv2.imread('pseudo_rgb_image.png')

    # Convert from BGR to RGB
    pseudo_rgb_image = cv2.cvtColor(pseudo_rgb_image, cv2.COLOR_BGR2RGB)

    # Display the image
    plt.imshow(pseudo_rgb_image)
    plt.axis('off')  # Hide axis
    plt.show()


# GUI setup
root = tk.Tk()
root.title("Spectral Image Processing")
root.geometry("500x300")  # Set initial size of the main window

upload_button = tk.Button(root, text="Upload Image", command=pseudo_coloring, font=("Arial", 16), bg="blue", fg="white")
upload_button.pack(pady=20)

display_button = tk.Button(root, text="Display Image", command=filter_and_print_image, font=("Arial", 16), bg="green", fg="white")
display_button.pack(pady=20)

root.mainloop()



