from java.io import File, FilenameFilter
from ij import ImagePlus
import re
class Filter(FilenameFilter):
	def accept(self, dir, name):
		reg = re.compile("\.tif$")
		m = reg.search(name)
		if m:
			return 1
		else:
			return 0

folder = "C:/Users/benny/APS_Data_rec/try_center/wood_002/"
tifs = [Opener().openImage(folder, file.name) for file in File(folder).listFiles(Filter())]
print(tifs)
