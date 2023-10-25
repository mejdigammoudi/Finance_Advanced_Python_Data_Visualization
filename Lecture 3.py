# Stock & Dividend yield
class Stock:
    def __init__(self,name,price, dividend):
        self.name = name
        self.price = price
        self.dividend = dividend
    def yield_dividend(self):
        return self.dividend / self.price

apple_stock = Stock('Apple',150,0.82)
print(apple_stock.yield_dividend())

# Portfolio & Add_instrument & Total_Value
class Portfolio:
    def __init__(self):
        self.instruments = {} #Empty dict
    def add_instrument(self,name,current_price):
        self.instruments[name] = current_price # associate a key & a value in a dict
    def total_value(self):
        total = sum(self.instruments.values())
        return total

ex1 = Portfolio ()
ex1.add_instrument('Apple', 150)
ex1.add_instrument('Google', 200)
print(ex1.total_value())

# CurrencyConverter & convert
class CurrencyConverter:
    def __init__(self,amount,source_currency,target_currency,rate ):
        self.amount = amount
        self.source_currency = source_currency
        self.target_currency = target_currency
        self.rate = rate
    def convert(self):
        return self.amount * self.rate

ex2 = CurrencyConverter(100, 'EUR', 'USD', 1.25)
print(ex2.convert())

# Simulate the stock price movements using simple random walk
import numpy as np

np.random.seed ( 0 )
daily_returns = np.random.normal(0.001,0.02,1000)
stock_prices = [100]
for r in daily_returns :
    stock_prices.append(stock_prices[-1]*(1+r))
print(stock_prices[-1])

# Portfolio Variance
s1 = 0.1
s2 = 0.2
w1 = 0.6
w2 = 0.4
rho = 0.5
portfolio_variance = (w1**2 * s1**2) + (w2**2 * s2**2) + 2 * w1 * w2 * rho * s1 * s2
print(portfolio_variance)

# Efficient Frontier (really difficult)
returns = np.array([0.10, 0.15])
volatilities = np.array([0.20, 0.30])
weights = np.linspace(0, 1, 10) # various weight

portfolio_returns = []
portfolio_volatilities = []
for w in weights:
    weight_vector = np.array([w, 1 - w])  # Weight vector for the two assets
    portfolio_return = np.dot(returns, weight_vector)  # Weighted sum of individual returns
    portfolio_volatility = np.sqrt(np.dot(weight_vector, np.dot(np.diag(volatilities), weight_vector)))
    portfolio_returns.append(portfolio_return)
    portfolio_volatilities.append(portfolio_volatility)

print (portfolio_returns,portfolio_volatility)

# Plotting Stock prices using Matplotlib
import matplotlib.pyplot as plt
stock_prices1 = [100, 102, 104, 103, 105, 107, 108]
dates = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
stock_prices2 = [107, 108, 107, 107, 106, 108, 109]
plt.figure(figsize=(10, 6))
plt.plot(dates, stock_prices1, label="Stock 1", color='blue')
plt.plot(dates, stock_prices2, label="Stock 2", color='red')
plt.title("Stock Price Over a Week")
plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.grid(True)
plt.legend()
plt.show()

#Visualizing Distributions using Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
returns = [0.05, -0.02, 0.03, -0.01, 0.02, 0.03, -0.03, 0.01, 0.04, -0.01]
sns.histplot(returns, bins=5, kde=True)
plt.title("Distribution of Stock Returns")
plt.show()