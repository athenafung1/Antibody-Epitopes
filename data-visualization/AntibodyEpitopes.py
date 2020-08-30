import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

bcell_filepath = "bcell.csv"
bcell_data = pd.read_csv(bcell_filepath, index_col = "parent_protein_id")

print(bcell_data.head())
#print(type(bcell_data['start_position'][0]))

difference_list = []

for row in bcell_data.itertuples():
	difference_list.append([row[3] - row[2]])

difference_data = pd.DataFrame.from_records(difference_list, columns = ['protein_length'])

sns.jointplot(x=bcell_data['isoelectric_point'], y=difference_data['protein_length'], kind="kde")
plt.show()
