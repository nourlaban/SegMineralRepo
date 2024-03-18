import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import os

# Path to the raster image
input_data_path = "D:\Github\Mineral\input_data\omar"
image_path = os.path.join(input_data_path,"Ziron1.tif")

# Open the raster image
with rasterio.open(image_path) as src:
    # Read the 6 bands
    red = src.read(1)  # Red band
    green = src.read(2)  # Green band
    blue = src.read(3)  # Blue band
    band4 = src.read(4)  # Band 4
    band5 = src.read(5)  # Band 5
    band6 = src.read(6)  # Band 6
    
    # Combine bands into RGB image
    rgb_image = [red, green, blue]
    
    # Plot the RGB image
    plt.figure(figsize=(10, 10))
    show(rgb_image)
    plt.show()
