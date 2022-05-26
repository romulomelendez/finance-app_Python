import yfinance as yf
import pandas as pd
from datetime import datetime
import numpy as np

list_symbols = ['BBDC3.SA', 'NUBR33.SA', 'ITSA4.SA', 'BBAS3.SA', 'DASA3.SA']

melhor = []
list_relacao_mm = []
precos = []

for ativo in list_symbols:
    soma_fundamentos = 0
    dyield = 0

    api = yf.Ticker(ativo)

    hist = api.history(period='6mo')

    precos = hist['Close'].values
    dividendos = pd.DataFrame(hist['Dividends'].values)
    dividendos_meses = dividendos.loc[datetime(2021, 12, 1):datetime(2022, 5, 1)]

    # calculo de dividendos
    dyield = (dividendos_meses.sum() / 2) / precos[0] if precos[0] > 0 else 0

    # analise de algoritmo de fundamentos
    if dyield > 0.05:  # se o dividendo for maior que 5% ou seja, se o dividendo for maior que 5% do preco de fechamento
        try:
            anual = api.balance_sheet
            trimestral = api.quarterly_balance_sheet

            financials_anual = api.financials
            cash_anual = api.cashflow

            financials_trimestral = api.quarterly_financials
            cash_trimestral = api.quarterly_cashflow

            if financials_anual.keys()[0].year >= financials_trimestral.keys()[0].year and len(anual) > 0:
                balanco = anual
                dre = financials_anual
                dfc = cash_anual

                receita = int(dre.loc['Total Revenue'][0] > dre.loc['Total Revenue'][1])
                ebitida = int(dre.loc['Ebit'][0] > dre.loc['Ebit'][1])
                caixa = int(dfc.loc['Change In Cash'][0] > dfc.loc['Change In Cash'][1])
                divida = int(balanco.loc['Total Current Liabilities'][0] < balanco.loc['Total Current Liabilities'][1])

                soma_fundamentos = caixa + ebitida + receita + divida

                if soma_fundamentos >= 2:
                    print(ativo, divida, caixa, ebitida, receita, financials_anual.keys()[0])
                    melhor.append(ativo)
                    list_relacao_mm.append(abs(precos[0] / np.mean(precos[-40:]) - 1))
                    precos.append(round(precos[0], 2))
            else:
                continue
        except:
            print(ativo)
            continue


