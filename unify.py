import pandas as pd
from datetime import datetime
from os import path


BASE_PATH = path.dirname(path.realpath(__file__))


def transform_input(csv_path):
    columns = ["dt", "obs"]
    return (
        pd.read_csv(csv_path, parse_dates=[0], date_format="%Y.%m")
        .iloc[:, 0:2]
        .set_axis(columns, axis=1)
    )


def main():
    # Gets 2 columns from df with correct column names
    csv_ocupa = transform_input(path.join(BASE_PATH, "csv", "ocupa.csv"))
    csv_fumo = transform_input(path.join(BASE_PATH, "csv", "fumo.csv"))

    # https://stackoverflow.com/questions/29464234/compare-python-pandas-dataframes-for-matching-rows
    # Like an SQL inner join
    columns = ["dt", "occ", "smk"]  # Date point, occupation, smoke products production
    csv_out = pd.merge(csv_ocupa, csv_fumo, on=["dt"], how="inner").set_axis(
        columns, axis=1
    )

    print(csv_out.to_csv(index=False))


if __name__ == "__main__":
    main()
