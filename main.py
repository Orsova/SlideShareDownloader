import os
import requests
for i in range(1,562):
    url = 'IMAGEURLPARTONE'+str(i)+'PART2.jpg'
    page = requests.get(url)

    f_ext = os.path.splitext(url)[-1]
    f_name = 'page{}{}'.format(i,f_ext)
    with open(f_name, 'wb') as f:
        f.write(page.content)
    if page.status_code == 200:
        print ("Downloading page: "+ str(i))
    else:
        print ("Done!")
        exit()
