import wordcloud
file = open(r"Ori.csv", encoding="utf-8")
text = file.read()
stopwords = {"一星", "二星", "三星", "四星", "五星", "world", "评论内容", "评论星数"}
wc = wordcloud.WordCloud(font_path=r"Hiragino Sans GB.ttc",
                            stopwords=stopwords)
wc.generate(text)
image = wc.to_image()
image.show()