import pandas as pd

data = {
"A": [1, 2, 2, 1],
"B": [3.1, 4.2, 1.5, 6.3],
"C": [800, 150, 400, 210]
}

data_frame = pd.DataFrame(data)

data_frame['D'] = data_frame['A'] * data_frame['B']

print(data_frame)