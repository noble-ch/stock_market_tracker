# stock_market_tracker

This project is a Real-Time Stock Market Tracker that demonstrates the Observer design pattern. It fetches live Tesla stock prices, notifying investors via SMS and email whenever the price changes. The program asks for the user's email, simulating stock notifications being sent at least three times within 60 seconds. This interaction illustrates how the Observer pattern allows objects (like SMS and Email notifications) to subscribe to events (stock price changes) and react accordingly. The project is Dockerized, enabling easy deployment and execution in isolated environments, making it ideal for learning and practical demonstrations of design patterns.


How It Works
StockMarket (Publisher): This class now includes a fetch_price method that uses yfinance to get the latest stock price. The track_stock method runs in a loop, fetching the price at a specified interval and notifying subscribers if the price changes.

Investor (Subscriber Interface): This remains the same, where subscribers implement an update method.

SMSInvestor and EmailInvestor (Concrete Subscribers): These classes also remain the same, reacting to stock price updates.

Real-Time Tracking: The track_stock method runs in a separate thread and fetches the latest stock price every few seconds . If the price changes, it notifies all subscribers.

Main Program: The program starts tracking Tesla stock in real-time. It runs for 60 seconds, notifying subscribers of any price changes before stopping.
