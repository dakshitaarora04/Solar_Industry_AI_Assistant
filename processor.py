from PIL import Image, ImageFilter
import numpy as np

def load_image(image_file):
    image = Image.open(image_file).convert("RGB")
    return image

def extract_rooftop_area(image):
    gray = image.convert("L")
    blurred = gray.filter(ImageFilter.GaussianBlur(radius=1.5))
    arr = np.array(blurred)
    edges = (arr > 100).astype(np.uint8) * 255
    return edges
