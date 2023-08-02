import requests
import pandas as pd
from requests.exceptions import HTTPError

def get_rates_of_currency(currencies, rates_number):
    results = []
    try:
        # Korzystamy z API NBP
        url_base = 'http://api.nbp.pl/api/exchangerates/rates/a/'
        for currency in currencies:
            url = f'{url_base}{currency}/last/{rates_number}/?format=json'
            response = requests.get(url)
            response.raise_for_status()
            if response.status_code == 200:
                results.append(response.json())
    except HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')
    except Exception as e:
        print(f'Other exception occurred: {e}')
    else:
        return results

def get_currencies_all():
    currencies = ['gbp']
    rates_number = 100
    data = get_rates_of_currency(currencies, rates_number)

    if data:
        dfs = []
        for currency_data in data:
            currency = currency_data['code']
            rates = currency_data['rates']
            df = pd.DataFrame(rates)
            df['Currency'] = currency
            dfs.append(df)

        combined_df = pd.concat(dfs, ignore_index=True)

        # Dodajemy kursy walut USD i EUR
        usd_data = get_rates_of_currency(['USD'], rates_number)
        if usd_data:
            usd_rates = usd_data[0]['rates']
            usd_df = pd.DataFrame(usd_rates)
            usd_df['Currency'] = 'USD'
            combined_df = pd.concat([combined_df, usd_df], ignore_index=True)

        eur_data = get_rates_of_currency(['EUR'], rates_number)
        if eur_data:
            eur_rates = eur_data[0]['rates']
            eur_df = pd.DataFrame(eur_rates)
            eur_df['Currency'] = 'EUR'
            combined_df = pd.concat([combined_df, eur_df], ignore_index=True)

        print(combined_df)
        return combined_df

get_currencies_all()



def get_rates_gold(gold_rates, rates_number):
    results = []
    try:
        url_base = 'http://api.nbp.pl/api/cenyzlota/last/30/?format=json'
        for gold_rate in gold_rates:
            url = f'{url_base}{gold_rate}/last/{rates_number}/?format=json'
            response = requests.get(url)
            response.raise_for_status()
            if response.status_code == 200:
                results.append(response.json())
    except requests.HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')
    except Exception as e:
        print(f'Other exception occurred: {e}')
    else:
        return results


if __name__ == '__main__':
    gold_rates = ['cena']
    rates_number = 100
    data = get_rates_gold(gold_rates, rates_number)
    gold = pd.DataFrame(data[0])
    print(gold)


