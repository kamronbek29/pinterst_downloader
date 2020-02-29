from urllib import request

import requests
from pyquery import PyQuery as pq


# Function to get download url
def get_download_url(link):
    # Make request to website 
    post_request = requests.post('https://www.expertsphp.com/download.php', data={'url': link})

    # Get content from post request
    request_content = post_request.content
    str_request_content = str(request_content, 'utf-8')
    download_url = pq(str_request_content)('table.table-condensed')('tbody')('td')('a').attr('href')
    
    if '.mp4' in str(download_url):
        print('Pinterest videeo download url: ', download_url)
    else:
        print('Pinterest image download url: ', download_url)

    return download_url


# Function to download video
def download_video(url):
    video_to_download = request.urlopen(url).read()
    with open('pinterest_video.mp4', 'wb') as video_stream:
        video_stream.write(video_to_download)


# Function to download image
def download_image(url):
    image_to_download = request.urlopen(url).read()
    with open('pinterest_iamge.jpg', 'wb') as photo_stream:
        photo_stream.write(image_to_download)


if __name__ == "__main__":
    url = input('Please, put your pinterest url: ')
    what_to_download = input('\nWhat do you want to download?\n1. Video\n2. Photo\nWrite here 1 or 2: ')

    print('\nPlease, wait, your file is downloading!')

    download_url = get_download_url(url)
    if str(what_to_download) == '1':
        download_video(download_url)
    else:
        download_image(download_url)

    print('Your file was successfully saved!')
