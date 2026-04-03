from model import predictor
from sklearn.metrics import mean_absolute_percentage_error as mape, mean_absolute_error as mae

model, x_test, y_test = predictor()

y_pred = model.predict(x_test)

error = mae(y_test, y_pred)
percent_error = mape(y_test, y_pred)

print(f"The final mean absolute error of our model is {error:.2f}")
print(f"The final % error of our model is {percent_error * 100:.2f} %")