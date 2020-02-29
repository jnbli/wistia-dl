#!/usr/bin/env python3
import sys
import re
import requests
import progressbar
from urllib.request import urlretrieve



class MyProgressBar():
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.pbar:
            self.pbar=progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()

def download(vid_id):
	# vid_id = "g5pnf59ala"
	url1 = "http://fast.wistia.net/embed/iframe/"+vid_id
	html = requests.get(url1, allow_redirects=True).content
	if html != b'{"error":true,"iframe":true}':
		# print(html)
		print('downloading:', vid_id)
		r1 = re.findall(r"\"url\":\".*?\.bin\"", str(html))[0]
		# print(r1)
		url2 = r1[7:-5]+".mp4"
		urlretrieve(url2, vid_id+".mp4", MyProgressBar())
	else:
		print('nonexistant id:', vid_id)

args = sys.argv[1:]

if len(args) > 0:
	for i in args:
		download(i)
else:
	print("Usage: wistia video id(s) expected as argument")





####PROGRESS BAR (UNTESTED)####
# import progressbar
# import urllib.request


# pbar = None


# def show_progress(block_num, block_size, total_size):
#     global pbar
#     if pbar is None:
#         pbar = progressbar.ProgressBar(maxval=total_size)

#     downloaded = block_num * block_size
#     if downloaded < total_size:
#         pbar.update(downloaded)
#     else:
#         pbar.finish()
#         pbar = None


# urllib.request.urlretrieve(model_url, model_file, show_progress)




###GET WEBSITE HTML####
# import requests
# r = requests.get('http://fast.wistia.net/embed/iframe/g5pnf59ala', allow_redirects=True)
# print(r.content)


####DOWNLOAD FILE FROM URL####
# from urllib import request
# request.urlretrieve ("http://africau.edu/images/default/sample.pdf", "sample.pdf")