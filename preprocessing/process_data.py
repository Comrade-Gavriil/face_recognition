import os
from PIL import Image

def rename_pictures(path):
    for file in os.listdir(path):
        src = os.path.join(path,file)
        filename, file_extension = os.path.splitext(file)
        new_filename = filename.split('.')[-1]
        dst = os.path.join(path,new_filename+file_extension)
        
        try:
           os.rename(src,dst) 
        except: 
            pass

def resize_images(path):
    for image in os.listdir(path):
        try:    
            file_path = os.path.join(path,image)
            im = Image.open(file_path)
            out = im.resize((128,128))
            out.save(file_path)
        except:
            print("File: %s couldn't be resized" % (file_path))


            

path = 'C:\\Users\\Graham Dobbie\\Documents\\machine_learning\\face_recognition\\images\\faces'
rename_pictures(path)
resize_images(path)