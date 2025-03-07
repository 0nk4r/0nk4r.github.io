from PIL import Image, ImageOps
from pathlib import Path
import base64
from io import BytesIO
import tyro
from thumbhash import image_to_thumb_hash, thumb_hash_to_rgba  # Fixed import

def generate_responsive_images(input_image_path: Path):
    # Define sizes and suffixes
    sizes = [(320, "-small"), (640, "-medium"), (1024, "-large"), (1920, "-xlarge")]

    # Set new image storage path inside Jekyll's assets directory
    opt_dir = Path("assets/images/opt")
    opt_dir.mkdir(parents=True, exist_ok=True)

    # Extract base filename and extension
    base_name = input_image_path.stem
    ext = input_image_path.suffix

    width, new_height = None, None  # To store the last width/height for Jekyll template

    # Process each size
    for width, suffix in sizes:
        with Image.open(input_image_path) as img:
            img = ImageOps.exif_transpose(img)
            aspect_ratio = img.height / img.width
            new_height = int(width * aspect_ratio)

            # Resize and save
            resized_img = img.resize((width, new_height), Image.Resampling.LANCZOS)
            resized_image_path = opt_dir / f"{base_name}{suffix}{ext}"
            resized_img.save(resized_image_path)
            print(f"Saved resized image: {resized_image_path}")

    # Generate thumbhash
    try:
        with Image.open(input_image_path) as img:
            img = img.convert("RGBA")  # Ensure RGBA format
            thumbhash = image_to_thumb_hash(img.tobytes())

            # Decode thumbhash back to RGBA
            width, height, rgba_data = thumb_hash_to_rgba(thumbhash)
            thumbhash_image = Image.frombytes("RGBA", (width, height), rgba_data)

            # Save thumbhash image
            thumbhash_path = opt_dir / f"{base_name}-thumbhash.png"
            thumbhash_image.save(thumbhash_path)
            print(f"Saved thumbhash image: {thumbhash_path}")
    except Exception as e:
        print(f"Error generating thumbhash: {e}")

    # Jekyll `{% include %}` snippet
    template_code = f"""
{{% include responsive_image.html base_image_name="opt/{base_name}" alt="Your Alt Text Here" 
    width="{width}" height="{new_height}" %}}
"""
    print("\nJekyll template insertion code:\n")
    print(template_code)

def main(in_path: str):
    input_path = Path(in_path)
    if input_path.is_file():
        generate_responsive_images(input_path)
    elif input_path.is_dir():
        for file in input_path.iterdir():
            if file.is_file() and file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                generate_responsive_images(file)

if __name__ == "__main__":
    tyro.cli(main)
