"""Open all .jpg files in argument folder, resize them, save to same folder with 'my' postfix"""

#tested with pillow module
#python3 -m pip install --upgrade pip
#python3 -m pip install --upgrade Pillow
#at the time...
from PIL import Image
import glob, os
import sys


def routine(directory):
  size=(1024, 768)
  first = True
  for infile in glob.glob(os.path.join(directory,"*.jpg")):
    filepath_no_ext, extension = os.path.splitext(infile)
    with Image.open(infile) as im:
        #here you can do A LOT of things with it. Some objects changes in memory. RTFM
        resized = im.resize(size)#can also choose resample algorithm, and area box
        resized.save(filepath_no_ext + ".my_save.jpg", "JPEG")
        if (first):
            first = False
            #show does not block. With lots of files it may be rather...painfull...
            im.show()
            resized.show()




def get_checked_path():
  """Extract path from argv and perform simple checks"""
  if (len(sys.argv)<2):
    print("No path to check")
    return None

  if (not os.path.exists(sys.argv[1])):
    print("path does not exist")
    return None

  if (not os.path.isdir(sys.argv[1])):
    print("path is not directory")
    return None
  return sys.argv[1]


if __name__=="__main__":
  directory = get_checked_path()
  if (directory):
    routine(directory)
  print()
  print("Done")
