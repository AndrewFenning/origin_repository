import re
from collections import defaultdict

# 1. Use a dictionary to group duplicates
near_duplicates = defaultdict(list)

with open('sample-file.txt', 'r') as f:
    for i, line in enumerate(f, 1):
        original = line.strip()
        # 2. Normalize: lowercase and remove ALL non-alphanumeric chars
        cleaned = re.sub(r'[\W_]+', '', original.lower())

        if cleaned:  # Ignore empty lines
            near_duplicates[cleaned].append((i, original))

# 3. Filter for sets (where count > 1)
sets = {k: v for k, v in near_duplicates.items() if len(v) > 1}

# 4. Print total number of sets
print(f"Total number of near-duplicate sets: {len(sets)}")

# 5. Print the first two sets found
for i, (cleaned_key, occurrences) in enumerate(list(sets.items())[:2]):
    print(f"\nSet {i + 1}:")
    for line_number, original_text in occurrences:
        print(f"{line_number}: {original_text}")