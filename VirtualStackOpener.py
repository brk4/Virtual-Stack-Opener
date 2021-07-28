import os

from java.io import File, FilenameFilter
from ij import ImagePlus




#folder = "C:/Users/benny/APS_Data_rec/try_center/wood_002/"
folder = "/Users/decarlo/Downloads/tiff/"



tiff_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.tiff')]

print(tiff_files)
