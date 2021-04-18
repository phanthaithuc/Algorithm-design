from typing import List
import collections


def shortest_word_distance(words: List[str], word1: str, word2: str) -> int:
    hash_table = collections.defaultdict(list)
    for index, word in enumerate(words):
        hash_table[word].append(index)
        if word == word1:
            word1_index = index
        elif word == word2:
            word2_index = index

    #distance = abs(hash_table[word1][0] - hash_table[word2][0])
    distance = float('inf')
    for i in hash_table[word1]:
        for j in hash_table[word2]:
            distance = min(distance, abs(i-j))

    return hash_table, distance


#print(shortest_word_distance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))


print(shortest_word_distance(["this","is","a","long","sentence","is","fun","day","today","sunny","weather","is","a","day","tuesday","this","sentence","run","running","rainy"],
                             "this","rainy"))