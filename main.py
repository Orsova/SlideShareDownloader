import os
import requests
from PIL import Image
import glob
import natsort

# img url should be the first high resolution jpg in the image sequence

projectdirectory = ""
# urllist = open("imglist.txt").readlines()

imgurl = ""

urlsplit = imgurl.split("-1-")

for i in range(1,562):
    url = urlsplit[0]+"-"+str(i)+"-"+urlsplit[1]
    page = requests.get(url)

    f_ext = os.path.splitext(url)[-1]
    f_name = 'page{}{}'.format(i,f_ext)
    with open(f_name, 'wb') as f:
        f.write(page.content)
    if page.status_code == 200:
        print ("Downloading page: "+ str(i))
    else:
        print ("Ended.")
        print ("Page "+str(i)+" empty. Deleting page.")
        os.remove("./page"+str(i)+".jpg")

        print ("Combining files...")

        files = glob.glob('*.jpg')

        print ("File names: "+str(files))

        print ("Sorting filenames.")

        sortedfiles = natsort.natsorted(files,reverse=False)

        print ("Sorted file names: "+str(sortedfiles))

        print ("Building PDF.")

        images = [
            Image.open(projectdirectory + f)
            for f in sortedfiles
        ]

        pdf_path = "./document.pdf"

        images[0].save(
            pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
        )

        print ("Deleting JPG files.")

        for filename in glob.glob('./*.jpg'):
            os.remove(filename)

        print ("Done.")

        break
