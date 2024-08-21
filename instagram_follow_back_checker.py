# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 01:47:57 2024

@author: neelc
"""

import instaloader
from instaloader import Profile

def get_followers(profile_name, loader):
    profile = Profile.from_username(loader.context, profile_name)
    return set(follower.username for follower in profile.get_followers())

def get_following(profile_name, loader):
    profile = Profile.from_username(loader.context, profile_name)
    return set(following.username for following in profile.get_followees())

def get_user_followers_count(username, loader):
    profile = Profile.from_username(loader.context, username)
    return profile.followers

def non_follow_backs(username, password, threshold):
    
    loader = instaloader.Instaloader()
    
    loader.login(username, password)
    
    profile = Profile.from_username(loader.context, username)
    
    followers = get_followers(username, loader)
    following = get_following(username, loader)
    
    not_following_back = following - followers
    
    print(f"Users not following you back with fewer than {threshold} followers:")
    for user in not_following_back:
        if get_user_followers_count(user, loader) <= threshold:
            print(user)
            
#Enter username and password
#Users who do not follow you back will only show if they have a follower count that is less than or equal to the threshold
non_follow_backs(username = 'neelchopra90', password = 'gunshot123!!!', threshold = 2500)  