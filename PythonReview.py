


def create_youtube_video(title, description): 
	youtubevideo = {"Title":title, "Description":description, "Likes":0, "Dislikes":0, "Comments":{}}
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

tit = "yeet"
desc = "Cool"
dic = create_youtube_video(tit, desc)
like(dic)
dislike(dic)
add_comment(dic, "AwesomeTuba682", "You're bad")