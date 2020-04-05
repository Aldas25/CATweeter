from twython import Twython
import requests

from cat_request import get_random_cat_url

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def tweet_random_cat_image ():

    image_file = 'cat_image.jpg'

    image_url = get_random_cat_url()

    img_data = requests.get(image_url).content
    with open(image_file, 'wb') as handler:
        handler.write(img_data)

    photo = open(image_file, 'rb')
    message = '(from "TheCatAPI")'

    response = twitter.upload_media(media=photo)
    twitter.update_status(status=message, media_ids=[response['media_id']])
    print("Tweeted (photo url: {}): {}".format(image_url, message))