import pandas as pd

def preprocess_data():
    df = pd.read_csv("data/credit_card_data.csv")
    df.columns = df.columns.str.lower()
    df = df.drop(columns=['card type', 'gender', 'exp type'])
    df['date'] = pd.to_datetime(df['date'], format='%d-%b-%y')
    df['city'] = df['city'].str.replace(', India', '', regex=False)
    df['month'] = df['date'].dt.to_period('M')
    df['amount'] = df['amount'].astype(float)

    monthly = df.groupby('month')['amount'].sum().reset_index()
    monthly['month_num'] = range(len(monthly))

    return monthly
