"""
Paste in a png file path to convert the png to a png @GMC 2023
"""
import pathlib

import magick_crop_png


# png_file_path = input("Enter a windows full file path: ")

# a raw r string is used since backslashes are normally escape characters
# paste in windows full file path
pasted_png_file_path = r"C:\Users\gmccarthy\Documents\PC_RTD_GITHUB_resources\PC-algorithms\docs\flowcharts\pythonfiles\Area_rectangle.png"


# get file path object
png_file_path = pathlib.PureWindowsPath(pasted_png_file_path)
magick_crop_png.crop_png(png_file_path)
