#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression


def split_date():
    # Read the data from CSV
    df_cyclist = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df_cyclist_cleared = df_cyclist["Päivämäärä"].str.split(expand=True)

    # Drop empty rows and columns
    df_cyclist_cleared.dropna(inplace=True)
    df_cyclist_cleared.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    df_cyclist_cleared["Hour"] = df_cyclist_cleared["Hour"].str.split(":", expand=True)[0]

    # Translate
    days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
    months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(),range(1, 13),))

    # Insert the English data into a dataframe
    df_cyclist_cleared["Weekday"] = df_cyclist_cleared["Weekday"].map(days)
    df_cyclist_cleared["Month"] = df_cyclist_cleared["Month"].map(months)

    # Define the data types present in each column
    df_cyclist_cleared = df_cyclist_cleared.astype(
        {"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int}
    )

    # Dropping unecessary rows and columns in df_cyclist
    df_cyclist.drop("Päivämäärä", axis=1, inplace=True)
    df_cyclist.dropna(axis=0, how="all", inplace=True)
    df_cyclist.dropna(axis=1, how="all", inplace=True)
    df_cyclist = pd.concat([df_cyclist_cleared, df_cyclist], axis=1)

    return df_cyclist


def cycling_weather_continues(station):
    df_cyclist = split_date()

    # create indexed df
    df_index = pd.merge(
        df_cyclist.loc[:, "Weekday":"Hour"],
        df_cyclist.loc[:, station],
        left_index=True,
        right_index=True,)

    df_index = df_index[df_index.Year == 2017]

    # read weather
    df_weather = pd.read_csv("src/kumpula-weather-2017.csv")

    # merge weather and cycling by day
    df_merge = pd.merge(
        df_weather,
        df_index.groupby(["Month", "Day"])[station].sum(),
        right_on=["Day", "Month"],
        left_on=["d", "m"],)

    # fill NA
    df_merge = df_merge.fillna(method="ffill")

    model = LinearRegression(fit_intercept=True)

    x = df_merge.loc[:, ["Precipitation amount (mm)", "Snow depth (cm)", "Air temperature (degC)"]]
    y = df_merge.loc[:, station]

    model.fit(x, y)
    score = model.score(x, y)

    return model.coef_, score


def main():
    station = "Kuusisaarentie"
    coef, score = cycling_weather_continues(station)
    
    #Measuring station: x
    #Regression coefficient for variable 'precipitation': x.x
    #Regression coefficient for variable 'snow depth': x.x
    #Regression coefficient for variable 'temperature': x.x
    #Score: x.xx
    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {coef[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coef[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coef[2]:.1f}")
    print(f"Score: {score:.2f}")


if __name__ == "__main__":
    main()