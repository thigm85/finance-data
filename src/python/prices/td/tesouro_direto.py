import pandas as pd

def get_current_tesouro_direto_quotes_from_xls(url, sheet_name):
    """ Return [sheet_name, date, price] of the last available price."""
    excel = pd.ExcelFile(url)
    df = excel.parse(sheet_name)

    df_list = df.iloc[0,:].tolist()

    date_index = df_list.index('Dia')
    venda_index = [i for i, s in enumerate(df_list) if 'PU Venda' in s][0]
    column_indexes = [date_index, venda_index] 

    result = [sheet_name]
    for i in column_indexes:
        result.append(df.iloc[-1,i])
    
    return result

