import pandas
import random
#
# data = pandas.read_csv("./data/french_words.csv")
# print(data)
# print(type(data))
# data_dict = data.to_dict()
# print(data_dict)
# print(len(data_dict))
# print("-"*30)
#
# data_list = data.to_dict(orient="records")
# print(data_list)
# print(len(data_list))

# ===================================================================================

data = pandas.read_csv("../data/french_words.csv")
data_list = data.to_dict(orient="records")
# print(data_list)
ran_word = random.choice(data_list)
french_ran_word = ran_word["French"]
# canvas.itemconfig(word_t, text=french_ran_word)
# print(french_ran_word)

print(ran_word)

i = 0
for e in data_list:
    if ran_word == e:
        data_list.remove(e)


print(data_list)
print(len(data_list))