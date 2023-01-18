import os
from PIL import Image
import pillow_heif


def print_directory_contents(path):
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            print_directory_contents(child_path)
        else:
            if child_path.endswith('.HEIC'):
                convert_heic_to_jpg(child_path)


def convert_heic_to_jpg(path):
    heif_file = pillow_heif.read_heif(path)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
    )
    file_name = os.path.basename(path)
    image.save(os.path.splitext(file_name)[0] + ".jpg", format(
        "JPEG"), quality=80, optimize=True, progressive=True)


print_directory_contents("path/to/folder")
