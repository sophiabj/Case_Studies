from src.xecd_client import XecdClient
from src.config import ACCOUNT_ID, API_KEY, CURRENCIES, OUTPUT_DIRECTORY
import pandas as pd
import datetime
import os
import schedule
import time





#Get exchange rates for given list of currencies
def get_rates(currencies): 

    xecd = XecdClient(ACCOUNT_ID, API_KEY)

    rates = []

    for currency in currencies:
        
        convert_from = xecd.convert_from("USD", currency, 1)
        print(f"Converting from USD to {currency}..")

        convert_to = xecd.convert_from(currency, "USD", 1)
        print(f"Converting from {currency} to USD..")

        timestamp = convert_from['timestamp']
        currency_from = convert_from['from']
        USD_to_currency_rate = convert_to['to'][0]['mid']
        currency_to_USD_rate = convert_from['to'][0]['mid']
        currency_to = convert_from['to'][0]['quotecurrency']

        rows = [timestamp, 
                currency_from, 
                USD_to_currency_rate, 
                currency_to_USD_rate, 
                currency_to]
        
        rates.append(rows)

    return rates
    
def main():
    rates = get_rates(CURRENCIES)
    df = pd.DataFrame(rates, columns=['timestamp', 
                                        'currency_from', 
                                        'USD_to_currency_rate', 
                                        'currency_to_USD_rate', 
                                        'currency_to'])
        
    filename = f"exchange_rates_{datetime.datetime.now().strftime('%Y%m%d')}.csv"
    output_path = os.path.join(OUTPUT_DIRECTORY, filename)

    df.to_csv(output_path)
    print(f"{filename} saved to directory at {datetime.datetime.now().strftime('%Y%m%d %H:%M')}!")


schedule.every().day.at("03:50").do(main)
schedule.every().day.at("23:00").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)