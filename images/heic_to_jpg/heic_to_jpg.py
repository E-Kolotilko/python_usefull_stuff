from PIL import Image
import os
from pillow_heif import register_heif_opener
import sys


SOURCE_EXTENSION='heic'
SOURCE_DEFAULT = 'source'
DEST_SUFFIX = '_converted'

def convert(source_folder, dest_folder, dest_extention = 'jpg', report_count = 10):
  register_heif_opener()
  cycle_counter = 0;
  file_counter = 0
  source_files = os.listdir(source_folder)
  print('Starting converting files...')
  for a_file in source_files:
    if a_file.lower().endswith(SOURCE_EXTENSION):
      image=Image.open(source_folder+'/'+a_file)
      dest_name = a_file[:-len(SOURCE_EXTENSION)]
      image.save(dest_folder+'/'+dest_name+dest_extention)
      image.close()
      file_counter+=1
      cycle_counter+=1
      if report_count and cycle_counter>=report_count:
        print(f'{file_counter} files processed')
        cycle_counter = 0
    else:
      print(f'Skipping {a_file} (not {SOURCE_EXTENSION})')
  print(f'Done converting files... {file_counter} files converted')


def get_conversion_paths():
  #making it 2 or 3 because you like to F around a lot and use weird paths that breaks into several paths....
  source = (sys.argv[1]) if 2<=len(sys.argv)<=3 else SOURCE_DEFAULT
  destination = (sys.argv[2]) if len(sys.argv)==3 else (SOURCE_DEFAULT + DEST_SUFFIX)
  while not os.path.exists(source):
    source = input('Source path is not found. Enter path:\n')
  #TODO : do you REALLY need this?
  while os.path.exists(destination):
    if not os.path.isdir(destination):
      print('File exists and is not a directory')
    elif input('Destination folder already exists. Would you like to continue? (y/n)\n').lower().startswith('y'):
      break
    destination = input('Enter destination\n')
  if not os.path.exists(destination):
    os.mkdir(destination)
  return source, destination


if __name__=='__main__':
  source, destination = get_conversion_paths()
  convert(source, destination)
  print('Done')
