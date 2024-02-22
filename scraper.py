import instaloader
import pandas as pd
import numpy
 
def read():
    # creating a data frame
    bot = instaloader.Instaloader()
    df = pd.read_csv("HA.csv")
    # print(df.head())

    # for col in df.columns[1:]:
    #     for 
    counter = 0

    for i in df.index:
        # st = str(df.iloc[i,0]) + ", "
        for col in df.columns[1:]:
            # st += str(df.loc[i,col]) + ", "
            # print(f"{df.loc[i,col]}, {df.iloc[i,0]}")
            try:
                p = instaloader.Profile.from_username(bot.context, str(df.loc[i,col]))
                print(f"{p.userid}, {p.username}, {p.followers}, {p.mediacount}, human, {df.iloc[i,0]}")
            except instaloader.ConnectionException:
                print(f"Error with user: {df.loc[i,col]}")
            counter += 1
        # st = st[:-2]
        # print(st)

    print(counter)
# # Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
# #bot.login(user="Your_username",passwd="Your_password") #Use this code to log-in to your account.


def getBasicInfo():
    profileid = input('Enter the userid of the profile\n')
    # Loading the profile from an Instagram handle
    profile = instaloader.Profile.from_username(bot.context, profileid)
    print("Username: ", profile.username)
    print("User ID: ", profile.userid)
    print("Number of Posts: ", profile.mediacount)
    print("Followers Count: ", profile.followers)
    print("Following Count: ", profile.followees)
    print("Bio: ", profile.biography)
    print("External URL: ", profile.external_url)   
    print('\n')

def downloadPost():
    useerid = input('Enter the userid of the profile\n')
    # Loading a profile from an Instagram handle
    profile = instaloader.Profile.from_username(bot.context, useerid)
    
    # Retrieving all posts in an object
    posts = profile.get_posts()
    count = 0
    # Iterating and downloading all the individual posts
    for index, post in enumerate(posts, 1):
        # if count < posts.:
        # bot.download_post(post, target=f"{profile.username}_{index}")
        # count+=1
        print(f"instagram.com/p/{post.shortcode}/")

        # else:
        #     break
    
if __name__ == '__main__':
    option = '0'
    while option != '5':
        option = input('Select Your option\n1)Get Profile Info\n2)Download Profile Posts\n3)Read CSV\n4)Exit\n')
        if option == '1':
            getBasicInfo()
        elif option == '2':
            downloadPost()
        elif option == '3':
            read()
        elif option == '4':
            exit
        else:
            print('Wrong input please try again\n')