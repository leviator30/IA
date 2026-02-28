import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



# Date easy_map1 - time - IDA*
data_easy1 = {
    'Solver': ['Euclidian', 'Manhattan', 'BFS Estimation'],
    'Time': [32.640740394592285, 0.85194993019104, 0.9210720062255859]
}
df = pd.DataFrame(data_easy1)
plt.figure(figsize=(10, 6))
sns.barplot(x='Solver', y='Time', data=df)
plt.title('Easy_map1 - IDA*')
plt.xlabel('Solver')
plt.ylabel('Time')
plt.savefig('easy1_times_IDA*.png')

# Date easy_map1 - steps - IDA*
data_easy1_steps = {
    'Solver': ['Euclidian', 'Manhattan', 'BFS Estimation'],
    'Steps': [2841495, 76378, 35928]
}
df = pd.DataFrame(data_easy1_steps)
plt.figure(figsize=(10, 6))
sns.barplot(x='Solver', y='Steps', data=df)
plt.title('Easy_map1 - IDA*')
plt.xlabel('Solver')
plt.ylabel('Steps')
plt.savefig('easy1_steps_IDA*.png')








# Date medium_map1 - time - IDA*
data_medium1 = {
    'Solver': ['Euclidian', 'Manhattan', 'BFS Estimation'],
    'Time': [5.872664213180542, 0.0033648014068603516, 0.009641408920288086]
}
df = pd.DataFrame(data_medium1)
plt.figure(figsize=(10, 6))
sns.barplot(x='Solver', y='Time', data=df)
plt.title('Medium_map1 - IDA*')
plt.xlabel('Solver')
plt.ylabel('Time')
plt.savefig('medium1_times_IDA*.png')

# Date medium_map1 - steps - IDA*
data_medium1_steps = {
    'Solver': ['Euclidian', 'Manhattan', 'BFS Estimation'],
    'Steps': [453328, 220, 220]
}
df = pd.DataFrame(data_medium1_steps)
plt.figure(figsize=(10, 6))
sns.barplot(x='Solver', y='Steps', data=df)
plt.title('Medium_map1 - IDA*')
plt.xlabel('Solver')
plt.ylabel('Steps')
plt.savefig('medium1_steps_IDA*.png')






# Date easy_map1 - time - Beam-Search
data_easy1_beam = {
    'Solver': ['Euclidian', 'Manhattan', 'BFS Estimation'],
    'Time': [0.0176236629486084, 0.017965078353881836, 0.030008554458618164]
}
df = pd.DataFrame(data_easy1_beam)
plt.figure(figsize=(10, 6))
sns.barplot(x='Solver', y='Time', data=df)
plt.title('Easy_map1 - Beam-Search')
plt.xlabel('Solver')
plt.ylabel('Time')
plt.savefig('easy1_times_beam.png')

# Date easy_map1 - steps - Beam-Search
data_easy1_steps_beam = {
    'Solver': ['Euclidian', 'Manhattan', 'BFS Estimation'],
    'Steps': [388, 388, 388]
}
df = pd.DataFrame(data_easy1_steps_beam)
plt.figure(figsize=(10, 6))
sns.barplot(x='Solver', y='Steps', data=df)
plt.title('Easy_map1 - Beam-Search')
plt.xlabel('Solver')
plt.ylabel('Steps')
plt.savefig('easy1_steps_beam.png')

# Data
# data2 = {
#     'Map': ['easy_map1', 'easy_map2', 'medium_map1', 'medium_map3', 'large_map1', 'medium_map2', 'hard_map1', 'large_map2'],
#     'Runtime': [0.05, 0.002, 0.8, 0.6, 10, 12, 15, 20]
# }

# df2 = pd.DataFrame(data2)

# Create barplot with logarithmic scale on the y-axis
# plt.figure(figsize=(10, 6))
# sns.barplot(x='Map', y='Runtime', data=df2, palette='viridis', legend=False)  # Added legend=False here
# plt.yscale('log')
# plt.title('Runtime IDA* - Manhattan')
# plt.xlabel('Map')
# plt.ylabel('Runtime (s)')

# # Rotate x-axis labels for better visibility
# plt.xticks(rotation=45, ha='right')

# plt.savefig('easy1_steps_beam.png')

