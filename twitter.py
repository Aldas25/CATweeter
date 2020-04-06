import os
import requests
import tweepy

from cat_request import get_random_cat_url

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def twitter_api ():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    # Verify twitter api credentials (checking if all api keys are correct)
    try:
        api.verify_credentials()
    except tweepy.error.TweepError as err:
        print("TweepError during authentication: {}".format(err))
    except:
        print("Unexpected error during authentication")
        raise
    else:
        print("Authentication OK")
    
    return api

def get_image(file, url):
    # Download that image from url link
    img_data = requests.get(url).content
    with open(file, 'wb') as handler:
        handler.write(img_data)

def tweet_random_cat_image ():

    image_file = 'cat_image.jpg'

    # Get random cat image url link using get_random_car_url
    try:
        image_url = get_random_cat_url()
    except:
        print ("Unexpected error while getting url for cat image")
        raise

    get_image(image_file, image_url)

    # Create an API object
    api = twitter_api ()
        
    message = u"\u1F604"

    message += '\n\n(from "TheCatAPI")'

    # Tweet an image
    try:
        api.update_with_media(image_file, status=message)
        os.remove(image_file)
    except:
        print("Unexpected error while uploading an image")
        raise

    print ("Image tweeted.\nURL: {}\nMessage: {}".format(image_url, message))

def check_mentions (since_id):

    api = twitter_api()

    new_since_id = since_id

    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)

        if tweet.in_reply_to_status_id is not None:
            continue

        print("Answering to {}".format(tweet.user.name))

        # if not tweet.user.following:
        #   tweet.user.follow()


        image_file = 'cat_image.jpg'

        # Get random cat image url link using get_random_car_url
        try:
            image_url = get_random_cat_url()
        except:
            print ("Unexpected error while getting url for cat image")
            raise

        get_image(image_file, image_url)

        # Tweet an image
        try:
            user = tweet.user
            message = "@{} Meow".format(user.screen_name)

            api.update_with_media(image_file,
                                  status = message,
                                  in_reply_to_status_id=tweet.id)
            os.remove(image_file)
        except:
            print("Unexpected error while uploading an image")
            raise

        print ("Replied.\nURL: {}\n".format(image_url))

    return new_since_id