import matplotlib.pyplot as plt
from preprocess import preprocess_data

df = preprocess_data()
plt.plot(df['month_num'], df['amount'])
plt.show()