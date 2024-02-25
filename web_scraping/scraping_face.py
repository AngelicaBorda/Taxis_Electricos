
from facebook_scraper import get_posts
for post in get_posts('TeslaMotorsCorp', pages=7):
    print(post)
    #print(post['time'])
    #print(post['likes'])
