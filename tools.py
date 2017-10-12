from random import random

import pandas as pd


def make_df(cols, n):
    return pd.DataFrame({col: [random() for i in range(n)] for col in cols})

