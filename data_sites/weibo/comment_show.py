import jieba
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.globals import ThemeType

stop_words = []
with open('stop_words.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        stop_words.append(line.strip())
content = open('comments.txt', 'rb').read()
# jieba 分词
word_list = jieba.cut(content)
words = []
for word in word_list:
    if word not in stop_words:
        words.append(word)

wordcount = {}
for word in words:
    if word != ' ':
        wordcount[word] = wordcount.get(word, 0)+1
wordtop = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)[:10]
wx = []
wy = []
for w in wordtop:
    wx.append(w[0])
    wy.append(w[1])

(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    .add_xaxis(wx)
    .add_yaxis('数量', wy)
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title='评论词 TOP10'),
        yaxis_opts=opts.AxisOpts(name='词语'),
        xaxis_opts=opts.AxisOpts(name='数量'),
        )
    .set_series_opts(label_opts=opts.LabelOpts(position='right'))
).render_notebook()