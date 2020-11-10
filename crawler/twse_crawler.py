import requests
import pandas as pd
import numpy as np

# '綜合損益彙總表'
TYPE_INCOME_STATEMENT='income statement'
# '資產負債彙總表'
TYPE_BALANCE_SHEET='balance sheet'
# '營益分析彙總表'
TYPE_PROFIT_ANALYSIS='profit analysis'

# input greater than 1000 would be consider to be common era
# else it is considered to be roc year
def to_roc_year(year):
    
    if year >= 1000:
        year -= 1911

    return year

def financial_statement_chinense(year, season, type=TYPE_INCOME_STATEMENT):

    year = to_roc_year(year)

    if type == TYPE_INCOME_STATEMENT:
        url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb04'
    elif type == TYPE_BALANCE_SHEET:
        url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb05'
    elif type == TYPE_PROFIT_ANALYSIS:
        url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb06'
    else:
        print('type does not match')

    r = requests.post(url, {
        'encodeURIComponent':1,
        'step':1,
        'firstin':1,
        'off':1,
        'TYPEK':'sii',
        'year':str(year),
        'season':str(season),
    }, timeout = 10)


    err_msg = "[twse crawler] failed to get %s" %(type)
    assert(r.status_code == 200), err_msg
    r.encoding = 'utf8'
    
    err_msg = "[twse crawler] no data for year: %s, season: %s type: %s"  %(str(year), str(season), type)
    assert('無資料' not in r.text), err_msg


    dfs = pd.read_html(r.text, header=None)

    return dfs

def financial_statement_english(year, season, type=TYPE_INCOME_STATEMENT):

    year_season_str = "year=%d&season=%d" % (year, season)

    if type == TYPE_INCOME_STATEMENT:
        url = 'https://emops.twse.com.tw/server-java/t163sb04_e?step=show&' + year_season_str
    elif type == TYPE_BALANCE_SHEET:
        url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb05'
    elif type == TYPE_PROFIT_ANALYSIS:
        url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb06'
    else:
        print('type does not match')

    for i in range(3) :
        try:
            r = requests.get(url, timeout = 10)
        except Exception as e:
            print(e)
            if i == 2:
                raise e
        break

    err_msg = "[twse crawler] failed to get %s" % (type)
    assert(r.status_code == 200), err_msg
    r.encoding = 'utf8'
    
    err_msg = "[twse crawler] no data for year: %s, season: %s type: %s"  %(str(year), str(season), type)
    assert('No match was found' not in r.text), err_msg


    dfs = pd.read_html(r.text, header=None)

    return dfs