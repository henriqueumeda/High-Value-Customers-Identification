import pickle

class Insiders(object):
    def __init__(self):
        self.standard_scaler = pickle.load(open('model/standard_scaler.pkl', 'rb'))

    def data_preparation(self, df):
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        df1 = df.select_dtypes(include=numerics).copy()
        df1[df1.columns] = self.standard_scaler.transform(df1[df1.columns].values)

        columns = ['Revenue', 'Purchases', 'AOV', 'CLV']
        df = df1[columns]

        return df