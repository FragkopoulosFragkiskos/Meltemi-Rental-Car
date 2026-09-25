from datetime import datetime


class RentalCalculator:
    # This class is responsible only for rental calculations.
    def __init__(self, pickup_date, return_date, daily_rate):
        self.pickup_date = pickup_date
        self.return_date = return_date
        self.daily_rate = daily_rate

    def calculate_duration(self):
        # Convert the dates from text to date objects
        pickup = datetime.strptime(self.pickup_date, "%d/%m/%Y")
        return_date = datetime.strptime(self.return_date, "%d/%m/%Y")

        # Calculate the difference between the two dates
        duration = return_date - pickup

        return duration.days

    def calculate_total_price(self):
        # Get the number of rental days
        duration = self.calculate_duration()

        # Calculate the total price
        total_price = duration * self.daily_rate

        return total_price