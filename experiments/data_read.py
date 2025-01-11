import pandas

data = pandas.read_csv("../data/french_words.csv")
print(data)
print(type(data))
data_dict = data.to_dict()
print(data_dict)
print(len(data_dict))

words = []
both_words = []

n = 0
index = 0

while index < 101:
    # This for loop will repeat 2 times as there are two keys french and english
    for lan in data_dict:
        words.append(data_dict[lan][index])
    both_words.append(words)
    words = []
    index += 1


print(words)
print(both_words)
# print(len(words))
# print(len(both_words))

i = 0
for word in both_words:
    print(both_words[i][0])
    print(both_words[i][1])
    i += 1
    # print(both_words[1])




