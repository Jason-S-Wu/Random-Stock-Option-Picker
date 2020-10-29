import requests, random
from bs4 import BeautifulSoup

def getMostVolume():
    ticketSymbols = [ ] #Might change to dict to also reflect price.  
    stockDataUrl = 'https://www.tradingview.com/markets/stocks-usa/market-movers-active/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    }
    stocks = requests.get(stockDataUrl, headers=headers).text
    stockData = BeautifulSoup(stocks, 'html.parser')
    stockDataParse = stockData.find_all("tr", attrs={"class":"tv-data-table__row tv-data-table__stroke tv-screener-table__result-row"})
    for stocks in stockDataParse:
        stockSymbol = stocks.find("a").text
        ticketSymbols.append(stockSymbol)
    return ticketSymbols

def pickStockOption(ticketSymbol):
    option = ["Call", "Put"]
    option = random.choice(option)
    stock = random.choice(ticketSymbol)
    result  = f'Your Random Stock Option: {stock} {option}'
    return result
    
def main():
    ticketSymbol = getMostVolume()
    stockOptionResult = pickStockOption(ticketSymbol)
    print(stockOptionResult)

if __name__ == '__main__':
    main()