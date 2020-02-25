import pandas as pd
from pandas_datareader import DataReader
from datetime import datetime
from datetime import date


class coleta:
    def Sidra(tabela):
        """ Coleta dados da API do sidra e os retorna como DataFrame
        Args:
        tabela: Código da tabela a ser coletada
            EX: 656 = IPCA
        """
        df = pd.read_json(
            f"http://api.sidra.ibge.gov.br/values/t/{tabela}/p/all/n1/all"
        )
        return df

    def AgregadosIBGE():
        """ Retorna DataFrame com principais agregados disponíveis na API do IBGE  """
        df = pd.read_json("https://servicodados.ibge.gov.br/api/v3/agregados")
        df = df["agregados"]
        return df

    def Ibovespa(
        url="https://en.wikipedia.org/wiki/List_of_companies_listed_on_Ibovespa",
        inicio=datetime(2010, 1, 1),
        fim=date.today(),
        source="yahoo",
    ):
        """ Retorna dicionário com informações das empresas presentes no índice IBOVESPA """

        tabelas_html = pd.read_html(url)
        df = tabelas_html[0]
        tickers = df["Ticket"]
        IBOV = {}

        for ticker in tickers:
            print(ticker)
            IBOV[f"{ticker}"] = DataReader(ticker, source, inicio, fim)
        return IBOV

