def find_lines_containing(filename, keyword):
    """
    Returns a list of (line_number, line_text) for lines that contain keyword
    (case-insensitive). Line numbers start at 1.
    """
    matches = []

    try:
        # Open the file in read mode
        # encoding='utf-8' is best practice to avoid errors with special characters
        with open(filename, 'r', encoding='utf-8') as f:

            # enumerate(f, start=1) gives us the line number automatically
            for line_num, line in enumerate(f, start=1):

                # Check for the keyword (convert both to lowercase for case-insensitivity)
                if keyword.lower() in line.lower():
                    # .strip() removes the newline character at the end of the line
                    matches.append((line_num, line.strip()))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the spelling.")
        return []

    return matches


# --- Main Execution ---

# Ensure this matches your actual file name (e.g. 'sample-file.txt' or 'sample_file.txt')
file_to_search = "sample-file.txt"
search_term = "data"

# Call the function
results = find_lines_containing(file_to_search, search_term)

# 1. Print how many matching lines were found
print(f"Total matching lines found: {len(results)}")

# 2. Print the first 3 matching lines (line number and text)
print("First 3 matching lines:")
# The syntax [:3] safely slices the list; it won't crash if there are fewer than 3 results.
for line_num, text in results[:3]:
    print(f"Line {line_num}: {text}")