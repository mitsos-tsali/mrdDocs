import pandas as pd
import os
import glob


def run():
    if len(os.listdir('Docs')) == 0:
        print("Directory is empty! Please add excel files first!")
    else:
        df_list = []
        for filename in glob.glob("Docs/*.xlsx"):
            temp_df = pd.read_excel(filename)
            df_list.append(temp_df)
        df = pd.concat(df_list, axis=1)
        df.to_excel("Final.xlsx")


if __name__ == '__main__':
    run()
