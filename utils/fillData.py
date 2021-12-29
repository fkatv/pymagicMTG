import pandas as pd
import time

def getFirstToken(string, char):
    t = string.index(char,0)
    return string[0:t]

def searchByToken(df, token):
    i = 0
    R = []
    for i in range(len(df)):
        if (df[i] == token):
            R.append(i)
            return R
    return R

def get_uuid_from_nan_values(LIST, data):
    type_nan_uuid = []
    type_nan_id = []
    for i in range(len(LIST)):
        if (type(LIST[i]) == float):
            type_nan_id.append(i)
            _token = getFirstToken(data.iloc[i].uuid,'-')
            type_nan_uuid.append(_token)
    
    return type_nan_id, type_nan_uuid
