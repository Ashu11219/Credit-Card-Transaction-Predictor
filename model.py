from exploratory_data_analysis import eda
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error as mape

def model():
    x_train, y_train, x_valid, y_valid, x_test, y_test = eda()

    lr = LinearRegression()
    rf = RandomForestRegressor(n_estimators=200, max_depth=5, random_state=42)

    lr.fit(x_train, y_train)
    rf.fit(x_train, y_train)

    y_pred1 = lr.predict(x_valid)
    y_pred2 = rf.predict(x_valid)

    error1 = mape(y_valid, y_pred1)
    error2 = mape(y_valid, y_pred2)

    if error1 > error2:
        print(f"Random Forest Regressor is better as it has {error2 * 100:.2f} % error")
        best_model = rf
    else:
        print(f"Linear Regression is better as it has {error1 * 100:.2f} %")
        best_model = lr

    return best_model, x_test, y_test