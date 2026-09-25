class RentalPricing:
    # This class is responsible for rental prices.
    def __init__(self):
        self.prices = {
            "Economy": 30,
            "Compact": 45,
            "Comfortable": 60,
            "Luxury": 110
        }

    def get_daily_rate(self, vehicle_category):
        # Get the daily price for the selected vehicle category
        return self.prices[vehicle_category]