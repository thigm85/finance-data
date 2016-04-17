#! /Users/tmartins/anaconda/bin/python

# Script responsible for sending [asset name, DDMMYYYY, price] to stdout in tab-separated format.

import prices.td.tesouro_direto as td
import prices.quandl.quandl as ql

if __name__ == "__main__":

    # tesouro direto
    url = ["http://www.tesouro.fazenda.gov.br/documents/10180/137713/NTN-B_Principal_2016.xls", "http://www.tesouro.fazenda.gov.br/documents/10180/137713/LFT_2016.xls"]
    
    sheets = [['NTN-B Principal 150535'],['LFT 070317', 'LFT 010321']]
                
    for i in range(len(url)):
        current_url = url[i]
        current_sheets = sheets[i]
        for j in range(len(current_sheets)):
            current_sheet = current_sheets[j]
            try:
                current_price_list = td.get_current_tesouro_direto_quotes_from_xls(url=current_url, sheet_name=current_sheet)
            except:
                current_price_list = [current_sheet, "", "Error"]    
            print('\t'.join(map(str,current_price_list)))

    # quandl

    quandl_codes = [["CURRFX/USDBRL", "Rate"],
                    ["CURRFX/USDNOK", "Rate"],
                    ["GOOG/BVMF_BOVA11", "Close"],
                    ["LBMA/GOLD", "USD (PM)"]]

    for i in quandl_codes:
        try:
            current_price_list = ql.get_current_quandl_data(i[0], i[1])
        except:
            current_price_list = [i[0], "", "Error"]
        print('\t'.join(map(str,current_price_list)))    

