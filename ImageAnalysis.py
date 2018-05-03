from PIL import Image
from os import listdir

data = {}

path = ''
for dir in listdir('data'):
    path = 'data/'+dir+'/'
    print('For an angle of {} degrees, the distances measured of the projectile where...'.format(dir))
    for file in listdir(path):

        if '.png' in file:
            im = Image.open(path+file)
            width, height = im.size
            data[dir]=width
            print('{}'.format(width))
  
