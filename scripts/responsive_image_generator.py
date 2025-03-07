import os
import sys
import tyro
from PIL import Image
from thumbhash import image_to_thumb_hash, thumb_hash_to_image

def resize_image(image_path, output_path, size):
    with Image.open(image_path) as img:
        img = img.resize(size, Image.LANCZOS)
        img.save(output_path, "JPEG")
        print(f"Saved resized image: {output_path}")

def generate_responsive_images(input_dir):
    sizes = {
        "small": (320, 240),
        "medium": (640, 480),
        "large": (1280, 960),
        "xlarge": (1920, 1440)
    }
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            base_name, ext = os.path.splitext(filename)
            input_path = os.path.join(input_dir, filename)
            
            for size_name, dimensions in sizes.items():
                output_file = f"{base_name}-{size_name}.jpeg"
                output_path = os.path.join(input_dir, "opt", output_file)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                resize_image(input_path, output_path, dimensions)
                
                # Generate and save ThumbHash
                with Image.open(output_path) as img:
                    thumb_hash = image_to_thumb_hash(img)
                    print(f"Generated ThumbHash for {output_file}: {thumb_hash}")

def main(in_path: str):
    if not os.path.exists(in_path):
        print("Error: Input path does not exist.")
        sys.exit(1)
    generate_responsive_images(in_path)

if __name__ == "__main__":
    tyro.cli(main)
