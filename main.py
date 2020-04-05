import time

from twitter import tweet_random_cat_image

while True:
    tweet_random_cat_image()
    time.sleep(60)