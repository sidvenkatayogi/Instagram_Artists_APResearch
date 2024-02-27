import instaloader
import pandas as pd
import numpy
import sqlite3
import webbrowser as web

# # Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
# #bot.login(user="Your_username",passwd="Your_password") #Use this code to log-in to your account.

def read(path):
    # creating a data frame
    conn = sqlite3.connect("instagram_artists_apresearch.db")
    cursor = conn.cursor()
    df = pd.read_csv(path)
    # counter = 0
    past = False
    before = True
    past_post = False
    for i in df.index:
        for col in df.columns[1:]:
            curr_post = None
            try:
                if(pd.notna(df.loc[i,col])):
                    if(str(df.loc[i,col]) == "beksinski"):
                        past = True
                    # if(str(df.loc[i,col]) == "ahvero"):
                    #     before = False
                    #     break
                    if(past and before):
                        p = instaloader.Profile.from_username(bot.context, df.loc[i,col])
                        # input("Go?")
                        print(f"{p.userid}, {p.username}, {p.followers}, {p.mediacount}, human, {df.iloc[i,0]}")
                        # cmd = """INSERT INTO PROFILES(USER_ID, USERNAME, NUM_FOLLOWERS, NUM_POSTS, IS_HUMAN, GENRE) 
                        # VALUES ({}, "{}", {}, {}, {}, "{}");""".format(p.userid, p.username, p.followers, p.mediacount, True, df.iloc[i,0])
                        # cursor.execute(cmd)
                        for post in p.get_posts():
                            
                            # if(past_post):
                                curr_post = post.shortcode
                                cmd = """INSERT INTO POSTS(OWNER_USER_ID, OWNER_USERNAME, NUM_LIKES, NUM_COMMENTS, SHORTCODE, IMG_URL, POST_DATE, IS_REEL, IS_HUMAN, GENRE) 
                                VALUES ({}, "{}", {}, {}, "{}", "{}", "{}", {}, {}, "{}");""".format(post.owner_id, post.owner_username, post.likes, post.comments, post.shortcode, post.url, post.date_utc, False, True, df.iloc[i,0])
                                
                                cursor.execute(cmd)
                            # if (post.shortcode == "BgHhSMxBFpL"):
                            #     past_post = True

                        # for post in p.get_igtv_posts():
                        #     cmd = """INSERT INTO POSTS(OWNER_USER_ID, OWNER_USERNAME, NUM_LIKES, NUM_COMMENTS, SHORTCODE, IMG_URL, POST_DATE, IS_REEL, GENRE) 
                        #     VALUES ({}, "{}", {}, {}, "{}", "{}", {}, {}, "{}");""".format(post.owner_id, post.owner_username, post.likes, post.comments, post.shortcode, post.url, post.date_utc, False, df.iloc[i,0])
                        #     cursor.execute(cmd)
                        # web.open("https://www.instagram.com/" + p.username + "/")
                    
                    # counter += 1
            except Exception as e:
                conn.commit()
                conn.close()
                print(f"Error with {df.loc[i,col]}, after {curr_post} : {e}")
                return
    conn.commit()
    conn.close()
    # print(counter)

def sql():
    conn = sqlite3.connect("instagram_artists_apresearch.db")
    cursor = conn.cursor()

    # cmd = ""
    # cmd = """CREATE TABLE profiles(
    # user_id INT,
    # username VARCHAR(30),
    # num_followers INT,
    # num_posts INT,
    # is_human BOOLEAN,
    # PRIMARY KEY (user_id)
    # );"""

    # cmd = """ALTER TABLE Posts
    #          ADD COLUMN genre VRACHAR(255);"""
    # cursor.execute(cmd)

    # cmd = """CREATE TABLE posts(
    # owner_user_id INT,
    # owner_username VARCHAR(30),
    # num_likes INT,
    # num_comments INT,
    # shortcode VARCHAR(255),
    # img_url VARCHAR(255),
    # post_date DATE,
    # is_reel BOOLEAN,
    # FOREIGN KEY(owner_user_id) REFERENCES Profiles(user_id)
    # );"""

    # cursor.execute(cmd)


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
    # p = instaloader.Profile.from_username(bot.context,"kuzminanastya")
    # print(p.mediacount)
    # sql()
    # option = '0'
    # while option != '5':
    #     option = input('Select Your option\n1)Get Profile Info\n2)Download Profile Posts\n3)Read CSV\n4)Exit\n')
    #     if option == '1':
    #         sql()
    #     elif option == '2':
    #         downloadPost()
    #     elif option == '3':
    #         read("HA.csv")
    #     elif option == '4':
    #         exit
    #     else:
    #         print('Wrong input please try again\n')
    read("HA.csv")
    # conn = sqlite3.connect("instagram_artists_apresearch.db")
    # cursor = conn.cursor()
    # cursor.execute("""INSERT INTO PROFILES(USER_ID, USERNAME, NUM_FOLLOWERS, NUM_POSTS, IS_HUMAN, GENRE) 
    #                     VALUES (1, "a", 1, 1, True, "b");""")
    # p = instaloader.Profile.from_username(bot.context, "elphcomics")
    # for post in p.get_posts():
    #     print(post.likes)
