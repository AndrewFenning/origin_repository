import pandas as pd

df = pd.read_csv('student.csv')

# print(df)

filtered_df = df[
    (df['studytime'] >= 3) &
    (df['internet'] == 1) &
    (df['absences'] <= 5)
]

# print(filtered_df)

filtered_df.to_csv('high_engagement.csv', index=False)

num_students = len(filtered_df)

avg_grade = filtered_df['grade'].mean()

print(f"Number of students saved: {num_students}")
print(f"Average grade of filtered students: {avg_grade:.2f}")