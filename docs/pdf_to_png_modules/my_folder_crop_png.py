"""
Paste in a full folder path to crop pngs therewithin to pngs @GMC 2025
"""
import pathlib

import magick_crop_png
# import wand_png_to_png


def get_png_files(png_folder_path):
    png_files = []
    for file in pathlib.Path(png_folder_path).iterdir():
        if file.is_file() and file.suffix == ".png":
            png_files.append(file.name)
    return png_files


def convert_folder(png_folder_path, pngs_files):
    for filename in pngs_files:
        png_file_path = png_folder_path / filename
        magick_crop_png.crop_png(png_file_path)
        # comment out wand or magick
        # wand_png_to_png.png_to_png(png_file_path)


# a raw r string is used since backslashes are normally escape characters
# paste in windows png full file path
pasted_folder_path = r"C:\Users\gmccarthy\Documents\PC_RTD_GITHUB_resources\PC-algorithms\docs\flowcharts\mermaidfiles\selection"

# r"C:\Users\gmccarthy\Documents\PC_RTD_GITHUB_resources\PC-algorithms\docs\flowcharts\mermaidfiles"

png_folder_path = pathlib.PureWindowsPath(pasted_folder_path)
pngs_files = get_png_files(png_folder_path)
convert_folder(png_folder_path, pngs_files)
print("done")