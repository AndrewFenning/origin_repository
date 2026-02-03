import pandas as pd

# 1. Load the data
df = pd.read_csv('student.csv')

# 2. Create the 'grade_band' column
# Logic: Low <= 9, Medium 10-14, High >= 15
def define_band(grade):
    if grade <= 9:
        return 'Low'
    elif 10 <= grade <= 14:
        return 'Medium'
    else:
        return 'High'

df['grade_band'] = df['grade'].apply(define_band)

# OPTIONAL: Define the sort order for the bands (Low -> Medium -> High)
band_order = ['Low', 'Medium', 'High']
df['grade_band'] = pd.Categorical(df['grade_band'], categories=band_order, ordered=True)

# 3. Create the grouped summary table
# UPDATED LOGIC: Since 'internet' is 0 or 1, the mean gives us the decimal percentage directly.
summary_table = df.groupby('grade_band', observed=False).agg(
    number_of_students=('grade', 'count'),
    average_absences=('absences', 'mean'),
    internet_access_pct=('internet', lambda x: x.mean() * 100)
)

# 4. Cleanup and Formatting
# Rounding values to 2 decimal places for better readability
summary_table['average_absences'] = summary_table['average_absences'].round(2)
summary_table['internet_access_pct'] = summary_table['internet_access_pct'].round(2)

print("Generated Summary Table:")
print(summary_table)

# 5. Save the table
summary_table.to_csv('student_bands.csv')
print("\nFile saved as 'student_bands.csv'")