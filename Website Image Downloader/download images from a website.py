#Download images from a website
#import required libraries
import urllib.request
import os
import re
import numpy as arraymaker
from bs4 import BeautifulSoup

#REPLACE WITH URL TO SCRAP
URL = input("Enter URl to scrape ")			
soup = BeautifulSoup(urllib.request.urlopen(URL).read() ,features="html.parser")
imgs = soup.findAll("image",{"alt":True, "src":True})

# Write all the links of images we got from beautifulsoup to a txt file 
f = open("im.txt","w+")
for i in imgs:
	print(i)
	f.write(str(i) + '\n')
f.close()

image = ""
# simple os function for downloading from url
def download(image):
	downloadlink = "wget " + image
	os.system(downloadlink)

# Find end position of required image url 
def endPosition(name,start):
	length = len(name)
	newName = name[start:length]
	count = 0
	position = start
	while (count == 0):
		for i in newName:
			position += 1
			#loop until position of ending " for url link found
			if (i == '"'):
				count += 1
				break
	ending = position - 1
	return ending

# Extracting the contents of im.txt line by line			
fp = open("im.txt","r+")
line = fp.readline()
while ( line != ''):
	search = 'src="'
	se = re.search(search,line)
	start = se.end()
	# Call endPosition function for finding the end position of image url in extracted line
	end = endPosition(line,start)
	image = line[start:end]
	if (image !=''):
		# call download function for downloading the images in root folder
		download(image)
	# Read next line from im.txt
	line = fp.readline()


