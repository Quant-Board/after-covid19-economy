import pandas_datareader as pdr
from datetime import datetime
import pandas as pd
import json
from flask import jsonify, Response
from collections import defaultdict

alias = defaultdict(str)
alias["kospi"] = "069500.KS"
alias["qqq"] = "QQQ"
alias["gold"] = "IAU" 

start = datetime(2020,1,20)
end = datetime(2020,9,12)
def fetchData(code: str):
    # return (High + low) / 2
    if(code in alias):
        code = alias[code]
    print (code)
    try :
        df = pdr.get_data_yahoo(code, start, end)
    except :
        return Response("get yahoo finance data Error", status=500)
    df['middle'] = (df['High'] + df['Low'])/2
    print(df['middle'].isna().sum())
    jsonData = json.loads(df['middle'].to_json(orient='table'))
    return jsonData

if __name__ == "__main__":
    print(fetchData("gold"))