import os
import urllib

import praw

path = os.getcwd()
print ("The current working directory is", path)
path = "/Users/sosa/WallpaperFinder/images"
#if pathe exist, dont need. If it doesnt, you need it
try:
    os.mkdir(path)
except OSError as e:
    print("Creation of the directory failed", path, e)
    raise e
else:
    print("successfully created the directory", path)
os.chdir("/Users/sosa/WallpaperFinder/images")
def getimg(submission):
    accepted_file_format = ['.jpg', '.jpeg', '.png']
    for format in accepted_file_format:

        if str(submission.url).endswith(format):
            response = urllib.request.urlopen(submission.url)

            img = response.read()
            with open(str(submission.id) + format, 'wb') as f:
                f.write(img)


reddit = praw.Reddit(client_id ='*********',
                     client_secret ='**********',
                     username ='**********',
                     password ='**********',
                     user_agent ='**********')

subreddit = reddit.subreddit('wallpaper')

top_wallpaper = subreddit.top(time_filter='year',limit=5)

for submission in top_wallpaper:

    if not submission.stickied:
        print('Title: {}, ups: {}'.format(submission.title,
                                          submission.ups))
    getimg(submission)


