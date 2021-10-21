from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers




# data = scrape(since="2021-10-07",  to_account = "@NetflixIndia", interval=1, 
# 	headless=False, display_type="Top", save_images=False, 
# 	resume=False, filter_replies=False, proximity=False)


# data = scrape(since="2021-10-06", from_account = "@NetflixIndia", interval=1, 
# 	headless=True, display_type="Top", save_images=False, 
# 	resume=False, filter_replies=False, proximity=False)


data = scrape(hashtag="covid", since="2021-10-14", until=None, from_account = None, interval=1, 
	headless=True, display_type="Top", save_images=False, 
	resume=False, filter_replies=True, proximity=False)

print(data)


# data = scrape(words="covid", since="2021-10-05", until=None, from_account = None, interval=1, 
# 	headless=True, display_type="Top", save_images=False, 
# 	resume=False, filter_replies=True, proximity=False)


users = ['@isaurabhpawar1']

# users_info = get_user_information(users, headless=True)

# following = get_users_following(users=users, verbose=0, headless=True, wait=2, limit=50, file_path=None)

# followers = get_users_followers(users=users, verbose=0, headless=True, wait=2, limit=50, file_path=None)
