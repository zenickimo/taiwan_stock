import twse_crawler as crawler
import pandas as pd
import traceback

def drop_useless(dfs):
    return dfs[1:]

def query_specific(year, season):
    dfs = crawler.financial_statement(year, season)
    dfs = drop_useless(dfs)
    concatenated = pd.concat(dfs, axis=0, sort=False)\
             .set_index(['公司代號'])\
             .apply(lambda s: pd.to_numeric(s, errors='ignore'))
    print(concatenated)
    return concatenated

try:
    start_year=107
    end_year=109
    
    for year in range(start_year+1, end_year+1):
        for season in range(1,5):
            print(year, " ", season)
            query_specific(year, season)

except Exception as e:
    print(e)
    traceback.print_exc(file=sys.stdout)
    print('stop for exception')        
