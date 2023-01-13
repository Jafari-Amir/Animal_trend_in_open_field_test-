import os
import pandas as pd
import matplotlib.pyplot as plt

path = '/Users/your directory/'
plt.figure(figsize=(6,4), dpi=200)

# read all csv files
dfs = []
for file in os.listdir(path):
    if file.endswith('.csv'):
        df_true_false = pd.read_csv(path+file)
        df_true_false['accum_value'] = 0   
        accum_value = 0

# make a new column in the dataframe to store the accumulative value that it has been designed deliberately 
        df_true_false['accum_value'] = 0
        # need to iterate over the rows of the dataframe
        for i, row in df_true_false.iterrows():
            # cheking  all value in the c1, c2, c3, or c4 columns is true
            if row[['c1', 'c2', 'c3', 'c4']].any():
                accum_value -= 1
            # cheking  allvalue in the b1, b2, b3, or b4 columns is true
            elif row[['b1', 'b2', 'b3', 'b4']].any():
                accum_value += 0
            # cheking  all values in center column is true
            elif row['center']:
                accum_value += 1
            # save the accumulative value in the dataframe
            df_true_false.loc[i, 'accum_value'] = accum_value

        # we need to connect the previous values to the accumulative values from one row to the next
        df_true_false['accum_value'] = df_true_false['accum_value'].shift(1) + df_true_false['accum_value']
        dfs.append(df_true_false)

df_final = pd.concat(dfs)
for i, df in enumerate(dfs):
    plt.plot(df['Frame'], df['accum_value'], label=os.path.splitext(os.listdir(path)[i])[0])
plt.grid(visible=True, linestyle='--', color='gray')
plt.legend()
plt.title("accumulative value over time")
plt.xlabel("Frame")
plt.ylabel("accum_value")
plt.savefig("picture.png", dpi=600)
plt.legend(loc="upper left", bbox_to_anchor=(1,1.034))
ax = plt.gca()
ax.autoscale()
plt.show()


