from PIL import Image, ImageOps
from pathlib import Path
import base64
from io import BytesIO
import tyro
from thumbhash import image_to_thumbhash, thumbhash_to_image

def generate_responsive_images(input_image_path: Path):
    # Define sizes and suffixes
    sizes = [(320, "-small"), (640, "-medium"), (1024, "-large"), (1920, "-xlarge")]

    # Set new image storage path inside Jekyll's assets directory
    opt_dir = Path("assets/images/opt")
    opt_dir.mkdir(parents=True, exist_ok=True)

    # Extract base filename and extension
    base_name = input_image_path.stem
    ext = input_image_path.suffix

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
    thumbhash = image_to_thumbhash(str(input_image_path))
    thumbhash_image = thumbhash_to_image(thumbhash)
    thumbhash_path = opt_dir / f"{base_name}-thumbhash.png"
    thumbhash_image.save(thumbhash_path)

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
