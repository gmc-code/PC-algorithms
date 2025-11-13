from pathlib import Path
import subprocess


def crop_png(png_path, dpi=300, margin_mm=2):
    """Crop a PNG using ImageMagick and add vertical margin in mm.

    Args:
        png_path (Path): Full path to the original PNG file.
        dpi (int): Dots per inch for conversion.
        margin_mm (float): Margin in millimeters to preserve top and bottom.
    """
    margin_px = int((margin_mm / 25.4) * dpi)
    # cropped_path = png_path.with_name(f"{png_path.stem}_crop{png_path.suffix}")
    cropped_path = png_path.with_name(f"{png_path.stem}{png_path.suffix}")

    subprocess.run([
        'magick',
        str(png_path),
        '-trim',
        '+repage',
        '-bordercolor', 'white',
        '-border', f'{margin_px}x{margin_px}',  # horizontal x vertical
        str(cropped_path)
    ], check=True)

    print(f"Cropped image saved as: {cropped_path}")


def process_png(png_file_path):
    """Crop a PNG file and save the result with '_crop' in the filename.

    Args:
        png_file_path (Path): Full file path of the PNG.
    """
    crop_png(png_file_path)
