from instabot import Bot

iam_bot=Bot()

#login id
iam_bot.login(username="iam_waste_no2__007",password="9965179759")

#follow one person
iam_bot.follow("iam_waste_007")

#follow multiple usres
iam_bot.follow_users(["undercut_trends","avantika_sahu","_.tharx.__"])

#unfollow the non followers
iam_bot.unfollow_non_followers()

#upload a photo
iam_bot.upload_photo("nature_1.jpg",caption=" natur_1 | This is a nature snap I took")

#send a message
iam_bot.send_message("hello waste uh nalla irukkiya da","iam_waste_007")


try:
    #like a user
    iam_bot.like_user("iam_waste_007",amount=2,filtration=False)
except Exception:
    print(Exception)


#comment
user_id=iam_bot.get_user_id_from_username("iam_waste_007")
media_id=iam_bot.get_last_user_medias(user_id,1)
iam_bot.comment(media_id[0],"This picture is very nice")

#get list of followers
followers_list=iam_bot.get_user_followers("iam_waste_007")
following_list=iam_bot.get_user_following("iam_waste_007")










