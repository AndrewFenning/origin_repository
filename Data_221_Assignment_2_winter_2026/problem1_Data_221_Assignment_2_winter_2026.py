import string
from collections import Counter
sample_file = open(file = 'sample-file.txt', mode = "r")
sf_content = sample_file.read()

word_list = sf_content.lower().split()
# print(word_list)
cleaned_token_list = []
for word in word_list:
    clean_token = word.strip(string.punctuation)
    if sum(1 for char in clean_token if char.isalpha()) >= 2:
        cleaned_token_list.append(clean_token)

word_counts = Counter(cleaned_token_list)
most_common = word_counts.most_common(10)

for word, count in most_common:
    print(f"{word} -> {count}")
sample_file.close()
# print(cleaned_token_list)

