import twse_crawler as crawler
import pandas as pd
import traceback


try:
    dfs = crawler.financial_statement(109, 2)
    concatenated = pd.concat(dfs[1:], axis=0, sort=False)\
             .set_index(['公司代號'])\
             .apply(lambda s: pd.to_numeric(s, errors='ignore'))
    print(concatenated)

except Exception as e:
    print(e)
    traceback.print_exc(file=sys.stdout)
    print('stop for exception')        
