from datetime import datetime

import pandas as pd

filename = "data/Delhi_NCR_1990_2022_Safdarjung.csv"
dehli_df = pd.read_csv(filename)


def return_season(time: str):
    date = datetime.strptime(time, "%d-%m-%Y")
    month = date.month
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"
    else:
        return None


dehli_df["season"] = dehli_df["time"].apply(return_season)

print(f"Number of rows: {dehli_df.shape[0]}")
print(f"Number of columns: {dehli_df.shape[1]}")

dehli_df.head()
dehli_df.to_csv("data/Delhi_NCR_1990_2022_Safdarjung_seasons.csv", index=False)
