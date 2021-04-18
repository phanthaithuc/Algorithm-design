import collections

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC", "Pho"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun", "Saigon"]

d = collections.defaultdict(int)
# for words1 in list1:
#     d[words1] += 1
# for words2 in list2:
#     d[words2] += 1
res = []

for w1, w2 in zip(list1, list2):
    d[w1] += 1
    d[w2] += 1

for key, value in d.items():
    if value >= 2:
        res.append(key)

print(res)
print(d)