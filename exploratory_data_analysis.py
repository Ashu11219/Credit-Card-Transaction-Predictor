import numpy as np
import matplotlib.pyplot as plt
from preprocess import preprocess_data

def eda():
    df = preprocess_data()
    train = df[:int(0.6 * len(df))]
    valid = df[int(0.6 * len(df)):int(0.8 * len(df))]
    test = df[int(0.8 * len(df)):]

    x_train = train[['month_num']]
    y_train = train['amount']

    x_valid = valid[['month_num']]
    y_valid = valid['amount']

    x_test = test[['month_num']]
    y_test = test['amount']

    return x_train, y_train, x_valid, y_valid, x_test, y_test
