import requests
import csv
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # fetch and parse
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # 3. locate the main content
    content_div = soup.find('div', id='mw-content-text')

    if not content_div:
        print("Error: Could not find main content div.")
        exit()

    # Find the correct table (first one with >= 3 data rows)
    tables = content_div.find_all('table')
    target_table = None

    for table in tables:
        rows = table.find_all('tr')
        # specific check: Count rows that actually contain data cells (td)
        data_row_count = 0
        for row in rows:
            if row.find('td'):
                data_row_count += 1

        if data_row_count >= 3:
            target_table = table
            break

    if target_table:
        print("Table found. Extracting data...")

        # Process Headers
        rows = target_table.find_all('tr')
        first_row = rows[0]

        # Check for <th> tags in the first row (cuz that's how html does tables)
        header_cells = first_row.find_all('th')

        csv_headers = []
        start_index = 0  # row index to start scraping data from

        if header_cells:
            # Case A: Table has headers
            csv_headers = [th.get_text().strip() for th in header_cells]
            start_index = 1  # Skip the first row since it's the header
        else:
            # Case B: Table has no headers, generate col1, col2, etc.
            # We count cells in the first row to know how many columns we need
            first_row_cells = first_row.find_all('td')
            num_cols = len(first_row_cells)
            csv_headers = [f"col{i + 1}" for i in range(num_cols)]
            start_index = 0  # Don't skip the first row, it contains data

        # Process Data Rows
        table_data = []

        # Iterate through rows starting from our determined start_index
        for row in rows[start_index:]:
            cells = row.find_all(['td', 'th'])  # specific edge case: sometimes data rows use th for the first column

            # Extract text
            row_data = [cell.get_text().strip() for cell in cells]

            # Only process if the row is not empty
            if row_data:
                # Handle Padding (Missing values)
                # If row is shorter than header, fill with empty strings
                if len(row_data) < len(csv_headers):
                    missing_count = len(csv_headers) - len(row_data)
                    row_data.extend([""] * missing_count)

                # If row is longer (rare but possible), trigger truncation to match header
                # or technically, the CSV module handles variable lengths, but padding is requested.
                # We will strictly align to the header count for safety.
                final_row = row_data[:len(csv_headers)]

                table_data.append(final_row)

        # Save to CSV
        filename = "wiki_table.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(csv_headers)  # Write header
            writer.writerows(table_data)  # Write data

        print(f"Success! Data saved to {filename}")
        print(f"Headers: {csv_headers}")
        print(f"Rows extracted: {len(table_data)}")

    else:
        print("No table matching the criteria (>= 3 data rows) was found.")

except Exception as e:
    print(f"An error occurred: {e}")