import os
import requests
from PIL import Image
import glob
import natsort
from bs4 import BeautifulSoup
import csv
import ocrmypdf

#usersettings

projectdirectory = "/Users/cyanotype/Desktop/Python/pythonProject/"

# open URL list

with open('urls.csv', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:

        ssurlraw = str(row)
        ssurl = ssurlraw.split("'")

        print (ssurl[1])

        # parse image url from slideshare url

        ssurlget = requests.get(ssurl[1])
        print (ssurlget)
        soup = BeautifulSoup(ssurlget.text, features="html.parser")
        rawimgurla = soup.find('picture', attrs={'data-testid':'slide-image-picture'}).find("source")['srcset']
        rawimgurlb = rawimgurla.split(" ")[4]
        rawimgurlc = rawimgurlb.split("?")
        imgurl = rawimgurlc[0]

        # split image url and download images

        urlsplit = imgurl.split("-1-")
        print (imgurl)

        for i in range(1,562):

            url = urlsplit[0] + "-" + str(i) + "-" + urlsplit[1]

            urlstatus = requests.get(url)

            if urlstatus.status_code == 200:
                print ("URL Fine.")
            else:
                print ("URL Adjusted.")
                url = urlsplit[0] + "-" + urlsplit[1] + "-" + str(i) + "-" + urlsplit[2]

            page = requests.get(url)

            f_ext = os.path.splitext(url)[-1]
            f_name = 'page{}{}'.format(i,f_ext)
            with open(f_name, 'wb') as f:
                f.write(page.content)
            if page.status_code == 200:
                print ("Downloading page: "+ str(i))
                print (url)
            else:
                print ("Ended.")
                os.remove("./page"+str(i)+".jpg")
                break

        # combine images into PDF

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

        docname = str(ssurl[1])
        docname2 = docname.split("/")
        print (docname2[4])
        docname3 = docname2[4]

        pdf_path = "./"+docname3+".pdf"
        images[0].save(
            pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
        )

        # delete JPG files

        print ("Deleting JPG files.")

        for filename in glob.glob('./*.jpg'):
            os.remove(filename)

        print ("Document Finished.")
