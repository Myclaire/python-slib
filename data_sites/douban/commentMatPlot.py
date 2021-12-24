file = csv.reader(f)
sum_start_12 = 0
sum_start_13 = 0
sum_start_14 = 0
sum_start_15 = 0
sum_start_16 = 0
count_12 = 0
count_13 = 0
count_14 = 0
count_15 = 0
count_16 = 0
date_list = []
for line, comment in enumerate(file):
    if line != 0:
        date_list.append(comment[2])
        # print(line,comment)
        if comment[2] == '2021-02-12':
            sum_start_12 += movie_start_dict[comment[1]]
            count_12 += 1
        elif comment[2] == '2021-02-13':
            sum_start_13 += movie_start_dict[comment[1]]
            count_13 += 1
        elif comment[2] == '2021-02-14':
            sum_start_14 += movie_start_dict[comment[1]]
            count_14 += 1
        elif comment[2] == '2021-02-15':
            sum_start_15 += movie_start_dict[comment[1]]
            count_15 += 1
        elif comment[2] == '2021-02-16':
            sum_start_16 += movie_start_dict[comment[1]]
            count_16 += 1
star_list = [
    sum_start_12 / count_12, sum_start_13 / count_13,
    sum_start_14 / count_14, sum_start_15 / count_15,
    sum_start_16 / count_16
]