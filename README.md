# stock_market_tracker

How It Works
StockMarket (Publisher): This class now includes a fetch_price method that uses yfinance to get the latest stock price. The track_stock method runs in a loop, fetching the price at a specified interval and notifying subscribers if the price changes.

Investor (Subscriber Interface): This remains the same, where subscribers implement an update method.

SMSInvestor and EmailInvestor (Concrete Subscribers): These classes also remain the same, reacting to stock price updates.

Real-Time Tracking: The track_stock method runs in a separate thread and fetches the latest stock price every few seconds (you can adjust the interval). If the price changes, it notifies all subscribers.

Main Program: The program starts tracking Tesla stock in real-time. It runs for 30 seconds, notifying subscribers of any price changes before stopping.
