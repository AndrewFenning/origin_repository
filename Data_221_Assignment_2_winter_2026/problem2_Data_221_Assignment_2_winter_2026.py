from collections import Counter

sample_file = open(file = 'sample-file.txt', mode = "r")
sf_content = sample_file.read()

word_list = sf_content.lower().split()
# print(word_list)
cleaned_token_list = []
for word in word_list:
    clean_token = word.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    if sum(1 for char in clean_token if char.isalpha()) >= 2:
        cleaned_token_list.append(clean_token)

bigrams = []
for i in range(len(cleaned_token_list) - 1):
    bigram = (cleaned_token_list[i], cleaned_token_list[i+1])
    bigrams.append(bigram)

# 6. Count the frequency of each bigram
bigram_counts = Counter(bigrams)

# 7. Print the 5 most frequent bigrams in descending order
most_common_bigrams = bigram_counts.most_common(5)

for (w1, w2), count in most_common_bigrams:
    print(f"{w1} {w2} -> {count}")
sample_file.close()