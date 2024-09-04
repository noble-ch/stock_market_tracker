import yfinance as yf
import threading
import time
import random

# The Publisher (Subject)
class StockMarket:
    def __init__(self, stock_name):
        self.stock_name = stock_name
        self.price = 0
        self.subscribers = []
        self.running = True
        self.update_count = 0

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update(self.stock_name, self.price)

    def fetch_price(self):
        # Simulate price changes for testing
        return self.price + random.uniform(-1, 1)

    def track_stock(self, interval=10):
        start_time = time.time()
        while self.running:
            new_price = self.fetch_price()
            print(f"Fetched price: {new_price}")  # Debugging line
            if new_price != self.price:
                self.price = new_price
                self.notify_subscribers()
                self.update_count += 1
            # Check if 60 seconds have passed or 3 updates have been sent
            elapsed_time = time.time() - start_time
            if elapsed_time >= 60 or self.update_count >= 3:
                self.running = False
            time.sleep(interval)

    def stop_tracking(self):
        self.running = False

# The Subscriber (Observer) Interface
class Investor:
    def update(self, stock_name, price):
        raise NotImplementedError("Subclasses should implement this!")

# Concrete Subscribers
class SMSInvestor(Investor):
    def __init__(self, name):
        self.name = name

    def update(self, stock_name, price):
        print(f"[SMS] {self.name} notified: {stock_name} price is now {price}")

class EmailInvestor(Investor):
    def __init__(self, email):
        self.email = email

    def update(self, stock_name, price):
        print(f"[Email] Notification sent to {self.email}: {stock_name} price is now {price}")

# Main Program
if __name__ == "__main__": 
    print("Welcome to the Real-Time Stock Market Tracker!") 
    print("This program demonstrates the Observer pattern by notifying investors when the stock price changes.") 
    print("1. Email Input:The program asks the user to enter their email address. \n This email is then used in the EmailInvestor class to simulate email notifications.")
    print("2 .User Feedback: After entering the email, the program acknowledges the input and \n informs the user that notifications will be sent to the provided email.") 
    print("CREATED BY NOBLE BIRU")
    input("Press Enter to continue...")

    user_email = input("Please enter your email to receive Tesla's notifications: ")
    print(f" \n Thank you! Notifications will be sent to: {user_email}")

    # Create a stock market for a particular stock
    tesla_market = StockMarket("TSLA")

    # Create investors
    investor1 = SMSInvestor("Noble")
    investor2 = EmailInvestor(user_email)

    # Subscribe investors to the Tesla stock market
    tesla_market.subscribe(investor1)
    tesla_market.subscribe(investor2)

    print("Tracking Tesla stock price. Notifications will be sent for next 60 seconds.")

    # Start tracking the stock in a separate thread
    tracker_thread = threading.Thread(target=tesla_market.track_stock, args=(10,))
    tracker_thread.start()

    # Wait for tracking to complete
    tracker_thread.join()

    print("Stock tracking stopped. Thank you for using the Real-Time Stock Market Tracker!")
