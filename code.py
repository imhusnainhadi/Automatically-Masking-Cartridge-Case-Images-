from PIL import Image, ImageDraw

def mask_cartridge_case(image_path):
    # Load the image
    original_image = Image.open(image_path).convert('RGB')
    draw = ImageDraw.Draw(original_image)

    # Define colors for each feature
    colors = {'breech-face': (255, 0, 0),   # Red for breech-face impression
              'aperture-shear': (0, 255, 0),  # Green for aperture shear
              'firing-pin': (255, 0, 255),   # Purple for firing pin impression
              'firing-pin-drag': (0, 255, 255)}  # Light blue for firing pin drag

    # Example: Draw rectangles for different features
    breech_face_box = (100, 100, 200, 200)
    aperture_shear_box = (250, 100, 350, 200)
    firing_pin_box = (100, 250, 200, 350)
    firing_pin_drag_box = (250, 250, 350, 350)

    draw.rectangle(breech_face_box, outline=None, fill=colors['breech-face'])
    draw.rectangle(aperture_shear_box, outline=None, fill=colors['aperture-shear'])
    draw.rectangle(firing_pin_box, outline=None, fill=colors['firing-pin'])
    draw.rectangle(firing_pin_drag_box, outline=None, fill=colors['firing-pin-drag'])

    # Example: Draw an arrow for firing pin drag direction
    arrow_start = (50, 50)
    arrow_end = (100, 100)
    draw.line([arrow_start, arrow_end], fill=(0, 0, 255), width=2)

    # Save or display the modified image
    original_image.show()
    # original_image.save('output_image.jpg')

# Example usage
image_path = '/content/990900142.jpg'
mask_cartridge_case(image_path)
