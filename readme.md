# covid19-economy-server

Economy chart after covid19

### Installation

``` bash
git clone https://github.com/ytype/covid19-economy-server.git
pip install -r requirements.txt
python flask_app.py
```

### Usage

```
GET https://covid19economy.pythonanywhere.com/finance/<code>
```

`code` : https://finance.yahoo.com/quote/:code

This items below may use aliases

+ qqq: QQQ ETF (nasdaq)
+ kospi: KODEX 200 (kospi)
+ gold: iShares Gold Trust (gold)

example : 

```
GET https://covid19economy.pythonanywhere.com/finance/qqq
```

### Test

``` bash
python3 -m pytest ./test/*
```



