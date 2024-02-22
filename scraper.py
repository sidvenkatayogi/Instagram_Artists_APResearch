import instaloader
import pandas as pd
import numpy
 
def read(path):
    # creating a data frame
    bot = instaloader.Instaloader()
    df = pd.read_csv(path)
    counter = 0

    for i in df.index:
        for col in df.columns[1:]:
            try:
                if(pd.notna(df.loc[i,col])):
                    p = instaloader.Profile.from_username(bot.context, df.loc[i,col])
                    print(f"{p.userid}, {p.username}, {p.followers}, {p.mediacount}, human, {df.iloc[i,0]}")
                    counter += 1
            except instaloader.ConnectionException:
                print(f"Error with user: {df.loc[i,col]}")
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