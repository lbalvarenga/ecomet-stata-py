import pandas as pd
from datetime import datetime
from os import path

BASE_PATH = path.dirname(path.realpath(__file__))


def rn(a):
    return [i for i in a if i is not None]


def getbranch(df):
    branches = ["kfc", "bk", "roys", "wendys"]
    df["branch"] = df.apply(
        lambda row: rn([branch if row[branch] == 1 else None for branch in branches])[
            0
        ],
        axis=1,
    )

    return df["branch"]


def main():
    # NJ +++
    cols = [
        "rest",
        "wagelaw",
        "after",
        "branch",
        "pmeal",
        "wage_st",
        "emptot",
        "co_owned",
    ]
    csv_in = pd.read_csv(path.join(BASE_PATH, "data", "csv", "m_wage.csv"))
    csv_in["obs"] = range(len(csv_in))
    before = csv_in.copy()
    before["rest"] = csv_in["obs"].astype("int")
    before["branch"] = getbranch(before)
    before["after"] = 0
    before["wagelaw"] = before["nj"].astype("int", errors="ignore")
    before["pmeal"] = before["pmeal"]
    before["wage_st"] = before["wage_st"]
    before["emptot"] = before["emptot"].astype("int", errors="ignore")

    # after = pd.DataFrame.copy(csv_in["pmeal2"])
    # after["after"] = "hello"
    after = csv_in.copy()
    after["rest"] = csv_in["obs"].astype("int")
    after["branch"] = getbranch(after)
    after["after"] = 1
    after["wagelaw"] = before["nj"].astype("int", errors="ignore")
    after["pmeal"] = after["pmeal2"]
    after["wage_st"] = after["wage_st2"]
    after["emptot"] = after["emptot2"].astype("int", errors="ignore")

    csv_out = pd.concat([before, after])
    print(csv_out[cols].to_csv(index=False))


if __name__ == "__main__":
    main()
