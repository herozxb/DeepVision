import os, sys
from PIL import Image
from send2trash import send2trash
  
def is_jpg(filename):
  try:
    i=Image.open(filename)
    return i.format =='JPEG'
  except IOError:
    return False
  
cdir = "."
if len(sys.argv)>1:
  cdir = sys.argv[1]
i=j=k=0
for root, dirs, fnames in os.walk(cdir):
  sys.stderr.write(" %s\n"% root)
  j += 1
  dirs.sort()
  jpegs = filter(lambda fn: fn.lower().endswith((".jpg",".jpeg")), fnames)
  for fn in jpegs:
    fpath = os.path.join(root, fn)
    if not is_jpg(fpath):
      sys.stderr.write("  %s\n"%fn)
      send2trash(fpath)
      k += 1
  #i += len(jpegs)
  
print("%s files scanned in %s dirs. %s files removed." %(i, j, k))
