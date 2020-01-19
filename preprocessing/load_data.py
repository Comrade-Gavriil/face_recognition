from google_images_download import google_images_download


def download_images (args):
    response = google_images_download.googleimagesdownload()
    absolute_image_paths = response.download(args)

args = {'keywords':'faces', 'limit':'100', 'output_directory':'images', 'chromedriver':'C:\\Program Files\\ChromeDriver\\chromedriver.exe'}

download_images(args)