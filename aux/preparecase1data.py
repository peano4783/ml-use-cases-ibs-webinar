import pandas as pd
import numpy as np

def init_data():
    return pd.DataFrame({
        'x': [10, 4, 15, 20, 9],
        'y': [10, 16, 9, 10, 4],
        'r': [0.5, 0.2, 0.1, 0.1, 0.1],
        'n': [40, 20, 10, 10, 15]
    })

def gen_point_cloud(df):
    result_x, result_y = [], []
    for row in df.iterrows():
        x, y, max_r, n = row[1]
        for i in range(int(n)):
            r = np.random.uniform(0, max_r)
            print(r)
            angle = np.random.uniform(0, 2 * np.pi)
            result_x.append(x + r * np.sin(angle))
            result_y.append(y + r * np.cos(angle))
    return pd.DataFrame({'x': result_x, 'y': result_y})

def main(output_csv='../data/case1data.csv'):
    init_df = init_data()
    df = gen_point_cloud(init_df)
    df.to_csv(output_csv, float_format='%.2f', index=False)

if __name__=='__main__':
    main()