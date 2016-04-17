import Quandl as ql

def get_current_quandl_data(code, column_name):
    data = ql.get(code, rows = 1)[column_name]
    result = [code, data.index[0].date().strftime("%d/%m/%Y"), float(data)]
    return result

