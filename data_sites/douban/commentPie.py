with open('Ori.csv', 'r', encoding='utf-8') as f:
    file = csv.reader(f)
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    for line, comment in enumerate(file):
        if line != 0:
            # print(line, comment)
            if comment[1] == '一星':
                one += 1
            elif comment[1] == '二星':
                two += 1
            elif comment[1] == '三星':
                three += 1
            elif comment[1] == '四星':
                four += 1
            elif comment[1] == '五星':
                five += 1
    groups = ["1星", "2星", "3星", "4星", "5星"]
    offsets = [0, 0, 0, 0, 0]
    rng = np.random.RandomState(27)
    sj = [one, two, three, four, five]
    plt.pie(sj,
            labels=groups,
            explode=offsets,
            autopct='%1.1f%%',
            startangle=90,
            shadow=True)  
    plt.title(u"星级饼图")
    plt.show()