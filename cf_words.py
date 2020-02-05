import enchant

file = open("words.txt", "r")
d = enchant.Dict('en_US')

words = file.read().split()
cnt = {}
for word in words:
    cnt[word.lower()] = 0

for wordd in words:
    word = wordd.lower()
    if not d.check(word):
        continue;
    if word[-1] == 's' and d.check(word[:-1]):
        cnt[word[:-1]] += 1
    else: 
        cnt[word] += 1

cnt = sorted(cnt.items(), key=lambda x: x[1], reverse = True)

ot = open('result2.txt', 'w')

for key, value in cnt:
    ot.write(key + '\t' + str(value) + '\n')

