from PIL import Image
from os import listdir

data = []

path = ''
for dir in listdir('data'):
    path = 'data/'+dir+'/'
    print('For an angle of {} degrees, the distances measured of the projectile where...'.format(dir))
    for file in listdir(path):

        if '.png' in file:
            im = Image.open(path+file)
            width, height = im.size
            data.append([dir,'',width])
            print('{}'.format(width))

import csv
with open('Angle-Distance_Data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)  
