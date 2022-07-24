


def create_youtube_video(title, description, hashtags): 
	youtubevideo = {"Title":title, "Description":description, "Likes":0, "Dislikes":0, "Comments":{}, "Hashtag":hashtags}
	return youtubevideo

def like(dic):
	if "Likes" in dic:
		dic["Likes"]+=1
		print(dic)

def dislike(dic):
	if "Dislikes" in dic:
		dic["Dislikes"]+=1
		print(dic)

def add_comment(dic, username, text):
	dic["Comments"][username]=text
	print(dic)
	return dic

def similarity(dic, dic1):
	percnum = 0
	for a in dic1["Hashtag"]:
		for b in dic["Hashtag"]:
			if a==b:
				percnum += 20;
	return percnum

tit = "yeet"
desc = "Cool"
hasht = ["Cool", "yeet", "amazing", "asdasdas", "asd"]
dic = create_youtube_video(tit, desc, hasht)
dic1 = create_youtube_video("yeetus", "cooles", ["Cool", "yeet", "a", "b", "c"])
like(dic)
dislike(dic)
add_comment(dic, "AwesomeTuba682", "You're bad")
print(similarity(dic, dic1))
