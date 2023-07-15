import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import KNNImputer
import warnings
# pd.options.mode.chained_assignment = None
# warnings.simplefilter(action='ignore')
# data_arr1 = pd.read_csv("СВОД 2022.csv",index_col=False,delimiter=";")
# data_arr2 = pd.read_csv("СВОД 2023 6 мес.csv",index_col=False,delimiter=";")

# data = pd.concat([data_arr1,data_arr2],axis=0)
# data = data.fillna(data.mode().iloc[0])
# i = 0
# for k in data['Поезд/']:
#     data['Поезд/'][i] = 0
#     data['Станция отп.'][i] = 0
#     data['Станция назн.'][i] = 1
#     i += 1
# imputed = KNNImputer(missing_values=0).fit_transform([data['Сервис'],data['Месяц операции'],data['Итог']])
# data['Сервис'] = imputed[0]
# data['Месяц операции'] = imputed[1]
# data['Итог'] = imputed[2]
# print(data['Тип/'].unique())
# data['Тип/'] = LabelEncoder().fit_transform(data['Тип/'])
# train,val = train_test_split(data,test_size=0.2)
# train,val = train.to_numpy(),val.to_numpy()
# train_y = train[:,9]
# train_x = train[:,:6]
# train_x[:,-1] = train[:,8]
# train_x[:,-1] = train[:,10]
# del train
# val_y = val[:,9]
# val_x = val[:,:6]
# val_x[:,-1] = val[:,8]
# val_x[:,-1] = val[:,10]
# del val
# train_x = train_x.astype(dtype=np.float32)
# train_y = train_y.astype(dtype=np.float32)
# from sklearn import tree
# from sklearn.feature_selection import RFECV
# reg1 = tree.DecisionTreeRegressor()
# reg2 = RFECV(reg1,min_features_to_select=1)
# reg2.fit(train_x,train_y)
# print(reg2.score(val_x,val_y))
from joblib import dump


def mypredict(arrofdata):

    reg = joblib.load("/home/frizik/projects/Aquarium_logistics/neuralnetworks/RFECV[DecisionTrees].joblib")
    # номер поезда (0)x, месяц(1)v, станция(0 адлер)v, станция(1 москва)v, класс обслуживания(0)v, кол-во билетов(1)v, цена(v), цена(v), цена(v), расстояние
    # np_vector = np.array([1, 0, 1, 0, 1, 1591.4, 868.1, 0.0]).reshape(1, -1)
    
    np_vector = np.array(arrofdata).reshape(1, -1)
    return reg.predict(np_vector)