import cv2
from PIL import Image


class ImgIcon:
    
    def __init__(self):
        self.blue = {'R': 101, 'G': 165, 'B': 243}
        self.red = {'R': 191, 'G': 67, 'B': 66}
        self.yellow = {'R': 249, 'G': 232, 'B': 134}
        self.green = {'R': 97, 'G': 139, 'B': 74}
        self.purple = {'R': 74, 'G': 49, 'B': 77}
        

    
    def translate_colors(self,requirements):
        
        colors = []
        for r in requirements:
            if(r.lower() == 'v'):
                colors.append(self.blue)
            elif(r.lower() == 'r'):
                colors.append(self.red)
            elif(r.lower() == 'm'):
                colors.append(self.yellow)
            elif(r.lower() == 'e'):
                colors.append(self.green)
            elif(r.lower() == 'p'):
                colors.append(self.purple)
            else:
                print(r.lower() == 'r')
        return(colors)

        
    @staticmethod
    def build_cubes(cubes,weight = 80, width=120,INPUT_DIR = "rcs/"):
    ## https://www.geeksforgeeks.org/python-pil-image-resize-method/
        background = Image.open(INPUT_DIR)
        # resize the image
        size = (1354,2030)
        background = background.resize(size,Image.ANTIALIAS)
        
        x=weight
        y0,dy = width, 90
        x0,dx = 80, 40
        for i,cube in list(enumerate(cubes)):
            ii = i
            img = Image.open('rcs/cube_s{}_{}_{}.png'.format(cube['B'],cube['G'],cube['R']))
            new_size = (80,80)
            img = img.resize(new_size)
            if(i > 1 & i%2==0):
                x = x0 + i*dx
                ii = 0
            if(i > 1 & i%2!=0):
                ii=1
            y = y0 + ii*dy
            background.paste(img, (y, x), img)
        background.save(INPUT_DIR,"PNG")