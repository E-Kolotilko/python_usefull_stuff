"""Run ldd on all .so files in directory and look for 'not found' in stdout. If found scream 'NOT OK!!!' """
import os
import sys
import subprocess


def get_ldd_str(file_path):
  cmd_res = subprocess.run(['ldd',file_path],stdout=subprocess.PIPE)
  if (cmd_res.returncode != 0):
    print("Return code is not 0 for "+file_path) 
  #This decode buisiness is rather hardcore stuff for python<3.7....
  return cmd_res.stdout.decode()

def routine():
  if (len(sys.argv)<2):
    print("No path to check")
    return

  if (not os.path.exists(sys.argv[1])):
    print("path does not exist")
    return

  if (not os.path.isdir(sys.argv[1])):
    print("path is not directory")
    return

  files = os.listdir(sys.argv[1])

  if len(files) == 0 :
    print('No files to check')

  for a_file in files:
    if a_file.endswith('.so'):
      current_file = os.path.join(sys.argv[1], a_file)
      print("Checking "+a_file+' ...',end=' ')
      ldd_str = get_ldd_str(current_file)
      message = 'NOT OK!!!' if ('not found' in ldd_str) else "" 
      print(message)

if __name__=="__main__":
  routine()
  print()
  print("Done")






