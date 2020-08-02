import requests
import bs4
from pathlib import Path 
import os

directory = input("enter name of directory: ")
parent_dir = 'C:/Users/skoli/Documents/wikipediaimagesscraped/' #edit this parent directory with the parent 
                                                                #folder where you want your images
path = os.path.join(parent_dir,directory)
os.mkdir(path)
url = input('please paste url: ')
data_folder = Path(path)
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text,'lxml')
images = soup.select('.thumbimage') 
#paste the name of the class of images,
#this is a list containing all data in the class, 
#from which we must extract image links
images_list = []
#in the soup.select, we will obtain a list of all the classes of .thumbimage.
#the below for loop extracts the source of each of the images in the list and adds them to a seperate list
for i in range(len(images)):
	image = images[i]           
	images_list.append(image['src'])
#now we have a list with the sources of the images
#to get the link of each image, we add https to the nameof the link
#we then create a file and write to it the content of the link

count = 1
for link in images_list:
	images_link = requests.get('https:'+link)
	open_file = data_folder/Path("image"+ str(count) +'.jpg')
	f=open(open_file,'wb')#writebinary
	f.write(images_link.content)
	f.close()
	count+=1
print("your image is available at directory: " + str(path))	
