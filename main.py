import instaloader
from instaloader import Profile, Post

def instastory_download(usrname):

    username="Your username"
    password="Your password"
    instance = instaloader.Instaloader()
    instance.login(user=username,passwd=password)
    profile = Profile.from_username(instance.context, username=usrname)    
    instance.download_stories(userids=[profile.userid],filename_target='{}/stories'.format(profile.username))

instastory_download(usrname)
