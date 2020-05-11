import pandas as pd

def Coletar_Fundamentos(Ticker):
    """
    Coleta Indicadores fundamentalistas por leitura das tabelas hmtl do site
    Fundamentus.
    
    Argumentos:
        Ticker = String
    """
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
    df["Valor"].loc[df["Valor"].str.contains("%")==False] =     df["Valor"].loc[df["Valor"].str.contains("%")==False].str[:-2] + "," +     df["Valor"].loc[df["Valor"].str.contains("%")==False].str[-2:]
    return df

def Coletar_Balanço(Ticker):
    """
    Coleta Balanço por leitura das tabelas hmtl do site
    Fundamentus.
    
    Argumentos:
        Ticker = String
    """
    df = pd.read_html(f"http://www.fundamentus.com.br/detalhes.php?papel={Ticker}")[3]
    df.columns = df.iloc[0,]
    df.drop(0, inplace=True)
    df.iloc[:,0] = df.iloc[:,0].str[1:]
    df.iloc[:,2] = df.iloc[:,2].str[1:]
    return df

