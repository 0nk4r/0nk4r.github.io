# /// script
# requires-python: ">=3.11"
# dependencies = [
#   "pillow",
#   "tyro",
#   "thumbhash-python",
# ]
# ///


from PIL import Image, ImageOps
from pathlib import Path
import base64
from io import BytesIO
import tyro
from thumbhash import image_to_thumbhash, thumbhash_to_image


def generate_responsive_images(input_image_path: Path):
    # Define the sizes and suffixes
    sizes = [(320, "-small"), (640, "-medium"), (1024, "-large"), (1920, "-xlarge")]

    # Create opt directory if it doesn't exist
    opt_dir = input_image_path.parent / "opt"
    opt_dir.mkdir(exist_ok=True)

    # Extract the base filename
    base_name = input_image_path.stem
    ext = input_image_path.suffix

    width = 200
    new_height = 200

    # Process each size
    for width, suffix in sizes:
        # Open the original image
        with Image.open(input_image_path) as img:
            img = ImageOps.exif_transpose(img) or img
            # Calculate the new height maintaining the aspect ratio
            aspect_ratio = img.height / img.width
            new_height = int(width * aspect_ratio)

            # Resize the image
            resized_img = img.resize((width, new_height), Image.Resampling.LANCZOS)

            # Save the resized image in opt directory
            resized_image_path = opt_dir / f"{base_name}{suffix}{ext}"
            resized_img.save(resized_image_path)
            print(f"Saved resized image: {resized_image_path}")

    # thumbhash
    thumbhash = image_to_thumbhash(str(input_image_path))
    thumbhash_image = thumbhash_to_image(thumbhash)
    thumbhash_path = opt_dir / f"{base_name}-thumbhash.png"
    thumbhash_image.save(thumbhash_path)

    # Convert the thumbhash image to Base64
    buffered = BytesIO()
    thumbhash_image.save(buffered, format="PNG")

    # Generate the Jekyll template insertion code
    template_code = f"""
{{% include responsive_image.html base_image_name="{base_name}" alt="Your Alt Text Here" 
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
