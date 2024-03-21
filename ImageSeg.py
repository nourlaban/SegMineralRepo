import tkinter as tk
from tkinter import filedialog
import rasterio
from PIL import Image  # Import PIL for image display
import numpy as np  # Import NumPy for filtering

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
        # Replace this with your desired filter algorithm (e.g., averaging)
        filtered_data = np.mean(image_data, axis=0)  # Simple average filter across all bands

        # Select and combine desired bands (assuming bands are grayscale)
        red, green, blue = filtered_data[:3]  # Select first 3 bands for RGB
        combined_image = np.dstack((red, green, blue))  # Combine bands for RGB image

        # Display the filtered image
        display_image(combined_image)

        print("Image filtered and displayed successfully!")

    except Exception as e:
        print(f"Error filtering image: {e}")

# ... (display_image function and GUI setup remain the same)

def display_image(img):
    # Convert to a format suitable for PIL
    pil_image = Image.fromarray(img.astype('uint8'))

    # Display the image
    pil_image.show()

# GUI setup
root = tk.Tk()
root.title("Spectral Image Processing")

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

filter_button = tk.Button(root, text="Filter and Display Image", command=filter_and_print_image)
filter_button.pack()

root.mainloop()
