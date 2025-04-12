from pdf2image import convert_from_path
import os

def convert_pdf_to_images(pdf_path, output_folder="converted_cards", dpi=300):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    images = convert_from_path(pdf_path, dpi=dpi)
    image_paths = []

    for i, img in enumerate(images):
        path = os.path.join(output_folder, f"card_{i+1}.jpg")
        img.save(path, "JPEG")
        image_paths.append(path)

    return image_paths