#!/usr/bin/env python3
import pandas as pd
import argparse
import matplotlib.pyplot as plt


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Plot Logs from a csv file.")
    parser.add_argument("log_file", help="Input Log file.", type=str)

    args = parser.parse_args()

    ts_column_name = 'ts'

    df = pd.read_csv(args.log_file, header=0)

    df[ts_column_name] = (df[ts_column_name].astype(float) - df[ts_column_name][0]) / 1e9

    df_cols = df.columns.values.tolist()
    df_cols.remove(ts_column_name)
    col_input = ""
    col_list = []
    while col_input != "q":
        col_input = input("Available plots: {}\nWhich plot do you want? (press q to quit): ".format(", ".join(df_cols)))
        if col_input in df_cols:
            col_list.append(col_input)
        elif col_input == "q":
            for col in col_list:
                df.plot(kind='line', x=ts_column_name, y=col, ax=plt.gca())
            plt.show()
            plt.pause(0.0001)
