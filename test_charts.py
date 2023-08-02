import pandas as pd
import matplotlib.pyplot as plt
import API_connect

currencies_all = API_connect.get_currencies_all()

# Wykres dla walut
fig, ax = plt.subplots()
for currency in currencies_all['Currency'].unique():
    curr_df = currencies_all[currencies_all['Currency'] == currency]
    ax.plot(curr_df['effectiveDate'], curr_df['mid'], label=currency)
ax.set(xlabel='Data', ylabel='Kurs średni', title='Wykres walut USD EUR GBP')
ax.legend()
plt.xticks(rotation=45)
plt.show()

# Wykres dla złota
gold_rates = ['cena']
rates_number = 100
data = API_connect.get_rates_gold(gold_rates, rates_number)
gold = pd.DataFrame(data[0])

# Tworzenie wykresu dla ceny złota
figure, bx = plt.subplots()
bx.plot(gold['data'], gold['cena'], label='Cena złota')
bx.set(xlabel='Data', ylabel='Cena', title='Wykres ceny złota (za gram)')
bx.legend()
plt.xticks(rotation=45)
plt.show()