import os
from google_images_download import google_images_download

class dataHandeler():
    def __init__(self):
        self.data_path = r'..\images'
    
    
    def download_images (self,args):
        response = google_images_download.googleimagesdownload()
        print(args)
        absolute_image_paths = response.download(args)


    def rename_pictures(self, data_category):
        path = os.path.join(self.data_path,data_category)

        for file in os.listdir(path):
            src = os.path.join(path,file)
            filename, file_extension = os.path.splitext(file)
            new_filename = filename.split('.')[-1]
            dst = os.path.join(path,new_filename+file_extension)
            
            try:
                os.rename(src,dst) 
            except: 
                pass

    def resize_images(self, data_category):
        path = os.path.join(self.data_path,data_category)

        for image in os.listdir(path):
            try:    
                file_path = os.path.join(path,image)
                im = Image.open(file_path)
                out = im.resize((128,128))
                out.save(file_path)
            except:
                print("File: %s couldn't be resized" % (file_path))

    def make_data_set(self, size, non_face_categories):

        def create_search_query(keyword,size):
            return  {'keywords':keyword, 'limit':size, 'output_directory':'images', 'chromedriver':'C:\\Drivers\\ChromeDriver\\chromedriver.exe'}
        
        query = create_search_query('yeet', int(size/2))

        self.download_images(query)
        path = os.path.join(self.data_path, '\\'+'yeet')

        self.rename_pictures(path)
        self.resize_images(path)
        
        for category in non_face_categories:
            query = create_search_query(category, int(size/(2*len(non_face_categories))))

            self.download_images(query)
            path = os.path.join(self.data_path,'\\'+category)

            self.rename_pictures(path)
            self.resize_images(path)

dataHandeler = dataHandeler()

keywords = ('cars', 'birds', 'dogs', 'cats', 'trees', 'houses')

dataHandeler.make_data_set(size=100, non_face_categories=keywords)