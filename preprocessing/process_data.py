import os
import PIL

def rename_pictures(path):
    for file in os.listdir(path):
        os.rename(path+file, path+file.spilt('.')[len(file)-1]+'.jpg' )


rename_pictures(r'C:\Users\Graham Dobbie\Documents\machine_learning\face_recognition\images\faces')