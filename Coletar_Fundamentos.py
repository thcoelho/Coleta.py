import pandas as pd
import yfinance as yf

def Coletar_Fundamentos(Tickers):
    """
    Coleta Indicadores fundamentalistas por leitura das tabelas hmtl do site
    Fundamentus.
    
    Argumentos:
        Tickers = String ou lista de Tickers
    """

    df3 = pd.DataFrame(index=['P/L', 'P/VP', 'P/EBIT', 'PSR', 'P/Ativos', 'P/Cap. Giro',
    'P/Ativ Circ Liq', 'Div. Yield', 'EV / EBITDA', 'EV / EBIT',
    'Cres. Rec (5a)', 'LPA', 'VPA', 'Marg. Bruta', 'Marg. EBIT',
    'Marg. Líquida', 'EBIT / Ativo', 'ROIC', 'ROE', 'Liquidez Corr',
    'Div Br/ Patrim', 'Giro Ativos'])

    if type(Tickers) is str:
        Tickers = [Tickers]

    for Ticker in Tickers:
        df = pd.read_html(f"http://www.fundamentus.com.br/detalhes.php?papel={Ticker}")[2]
        df.columns = df.iloc[0,]
        df.drop(0, inplace=True)
        df.iloc[:,2] = df.iloc[:,2].str[1:]
        df.iloc[:,4] = df.iloc[:,4].str[1:]
        df = df.iloc[:,2:]   
        df2 = df.iloc[:,2:]
        df2.columns = ["Indicador", "Valor"]
        df = df.iloc[:,:2]
        df.columns = ["Indicador", "Valor"]
        df = df.append(df2)
        df["Valor"].loc[df["Valor"].str.contains("%") == False] = \
        df["Valor"].loc[df["Valor"].str.contains("%") == False].str[:-2] \
        + "," + df["Valor"].loc[df["Valor"].str.contains("%")==False].str[-2:]
        df.set_index("Indicador", inplace=True)
        df3[f"{Ticker}"] = df["Valor"]
    return df3

def Coletar_Balanço(Ticker):
    """
    Coleta Balanço por leitura das tabelas hmtl do site
    Fundamentus.
    
    Argumentos:
        Ticker = String com ticker
    """
    df = pd.read_html(f"http://www.fundamentus.com.br/detalhes.php?papel={Ticker}")[3]
    df.columns = df.iloc[0,]
    df.drop(0, inplace=True)
    df = pd.concat([df.iloc[:,:2], df.iloc[:,2:]])
    df.iloc[:,0] = df.iloc[:,0].str[1:]
    return df

def Risco(tickers):
    df = pd.DataFrame()
    for ticker in tickers:
        ticker = ticker + ".SA"
        df[f"{ticker}"] = yf.Ticker(f"{ticker}").history()["Close"]
    print(" Os desvios padrão são:")
    print(df.std())
    print("\n A correlação entre os Tickers é:")
    print(df.corr())
