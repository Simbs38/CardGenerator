import cv2
from PIL import Image
import numpy as np
INPUT_DIR = "../input/images/"    
OUTPUT_DIR = "../output/"

blue = {'R': 101, 'G': 165, 'B': 243}
red = {'R': 191, 'G': 67, 'B': 66}
yellow = {'R': 249, 'G': 232, 'B': 134}
green = {'R': 97, 'G': 139, 'B': 74}
purple = {'R': 74, 'G': 49, 'B': 77}

def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        print('123')
        # check if exists in unique_list or not 
        if x not in unique_list: 
            print('456')
            unique_list.append(x) 
    # print list 
    return(unique_list)
      

def put_text(file_name,text,INPUT_DIR = "../input/images/", font = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1,color = (0, 0, 0),thickness = 2):
    path = INPUT_DIR + file_name
    image = cv2.imread(path) ## Reading an image in default mode  
    
    y0, dy = 1500, 30
    for i, line in enumerate(text.split('\n')):
        y = y0 + i*dy
        cv2.putText(image, line, (120, y ), font, fontScale,color,thickness, cv2.LINE_AA) 
    return(image)

def change_cube_color(im, color):
    rows,cols,length = im.shape

    for i in range(rows):
      for j in range(cols):
         k = im[i,j]
         if(k[0] != 0):
             im[i,j] = [color['B'],color['G'],color['R'],im[i,j,3]]     #BGR   
    return(im)

def save_image(image , file_name, OUTPUT_DIR = "../output/"):
    cv2.imwrite(OUTPUT_DIR + file_name, image)
    
def prepare_cubes(file_name, colors, INPUT_DIR = "../input/images/"):
     path_cube = INPUT_DIR + file_name
     im = cv2.imread(path_cube,cv2.IMREAD_UNCHANGED)
     for color in colors:
         im = change_cube_color(im,color)
         save_image(im,'cube_s{}_{}_{}.png'.format(color['B'],color['G'],color['R']))
         
""" cubes = [blue, blue, red, green] """         
def build_cubes(cubes, card_name, INPUT_DIR = "../input/images/", OUTPUT_DIR = "../output/"):
    ## https://www.geeksforgeeks.org/python-pil-image-resize-method/
    background = Image.open(INPUT_DIR + card_name)
    # resize the image
    size = (1354,2030)
    background = background.resize(size,Image.ANTIALIAS)
    
    x=80
    y0,dy = 120, 90
    x0,dx = 80, 40
    for i,cube in list(enumerate(cubes)):
        ii = i
        img = Image.open(OUTPUT_DIR  + 'cube_s{}_{}_{}.png'.format(cube['B'],cube['G'],cube['R']))
        new_size = (80,80)
        img = img.resize(new_size)
        if(i > 1 & i%2==0):
            x = x0 + i*dx
            ii = 0
        if(i > 1 & i%2!=0):
            ii=1
        y = y0 + ii*dy
        background.paste(img, (y, x), img)
    background.save(INPUT_DIR+'item_card.png',"PNG")
        
    ## return(background)
    


path_card = INPUT_DIR + "evento.png"

img = cv2.imread(path_card,cv2.IMREAD_UNCHANGED)

rows,cols,length = img.shape

values=[]
for i in range(rows):
      for j in range(cols):
         k = img[i,j]
         if(k[0] != 0):
             if(img[i,j][0] == 51):   
                 #values.append(img[i,j])
                 img[i,j] = [97,139,74,img[i,j,3]]     #BGR   
             if(img[i,j][0] == 54):   
                 #values.append(img[i,j])
                 img[i,j] = [101,165,243,img[i,j,3]]     #BGR   
             if(img[i,j][0] == 62):   
                 #values.append(img[i,j])
                 img[i,j] = [191,67,66,img[i,j,3]]     #BGR   
             if(img[i,j][0] == 207):
                 #values.append(img[i,j])
                 img[i,j] = [74,49,77,img[i,j,3]]     #BGR   
             if(img[i,j][0] == 80):   
                 #values.append(img[i,j])
                 img[i,j] = [247,232,134,img[i,j,3]]     #BGR   
            
           
cv2.imshow("window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()





[0,1,2,3]==[1,1,2,3]












#colors = [blue,red,yellow,green,purple]

#prepare_cubes('cube.png',colors)

#card = build_cubes(cubes,"evento.png")

#img = put_text("item_card.png",'Esta carta nao faz grande cena.\nMas ao menos e bonita')
#save_image(img,'item_card.png')



"""
img = put_text('decisao.png','lalala\nlalalalalalala\nlala')
save_image(img,'decssss.png')

blue = {'R': 101, 'G': 165, 'B': 243}
red = {'R': 191, 'G': 67, 'B': 66}
yellow = {'R': 249, 'G': 232, 'B': 134}
green = {'R': 97, 'G': 139, 'B': 74}
purple = {'R': 74, 'G': 49, 'B': 77}

colors = [blue,red,yellow,green,purple]

prepare_cubes('cube.png',colors)
"""