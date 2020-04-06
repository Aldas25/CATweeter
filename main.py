import sys
import io
import time
import emoji

from twitter import tweet_random_cat_image, check_mentions

'''
TODO:
* update READ-ME:
    * add link to twitter acc
    * write what the bot does
* organise the structure of the project (add 'src', etc.), also: add functions instead of everything in one
* make tweet message more interesting - "Good morning/evening/night", 
                                        "Meow", "Purr"
                                        some cat (or sun, or moon) emoji, 
                                        etc.
'''


# print(emoji.emojize(':smile:', use_aliases=True))
# message = unicode(message, 'utf-8')

# message = message.encode('unicode_escape')



# message += '\n\n(from "TheCatAPI")'

# print(message)

since_id = 1

with open('since_id.txt', 'rb') as f:
    since_id = int(next(f))

while True:

    '''
    cur_datetime = time.ctime()
    datetime_splitted = cur_datetime.split()

    cur_time = datetime_splitted[3].split(':')
    h = cur_time[0]
    m = cur_time[1]
    s = cur_time[2]
    '''

    try:
        # tweet_random_cat_image()

        # since_id = check_mentions(since_id)
        with open('since_id.txt', 'wb') as f:
            f.write(str(since_id))
    except:
        print("Unexpected error: {}".format(sys.exc_info()[0]))
    
    time.sleep(10)