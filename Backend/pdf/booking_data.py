from datetime import datetime


class BookingData:
    # This class prepares the booking data
    # that will be used to create the rental agreement.
    def __init__(self, data):

        # Get the booking information received from Make
        self.customer_name = data["name"]
        self.email = data["email"]
        self.vehicle_category = data["car"]
        self.pickup_date = data["pickupDate"]
        self.return_date = data["returnDate"]

        # The issue date is the date when the booking was created
        self.issue_date = datetime.now().strftime("%d/%m/%Y")

        # Generate the booking ID
        self.booking_id = self.create_booking_id()

        # These rental terms are currently fixed
        self.insurance = "Full insurance with no excess"
        self.fuel_policy = "Full to full"
        self.additional_driver = "Included"

    def create_booking_id(self):
        # Get the first letter of the customer's name
        customer_initial = self.customer_name[0].upper()

        # Get the first digit of the issue date
        issue_digit = self.issue_date[0]

        # Get the first digit of the pickup date
        pickup_digit = self.pickup_date[0]

        # Get the first digit of the return date
        return_digit = self.return_date[0]

        # Get the first letter of the vehicle category
        category_initial = self.vehicle_category[0].upper()

        # Create the booking ID
        booking_id = (
            f"MR"
            f"{customer_initial}"
            f"{issue_digit}"
            f"{pickup_digit}"
            f"{return_digit}"
            f"{category_initial}"
        )

        return booking_id

    def to_dictionary(self):
        # Convert the booking data into a dictionary
        # that can be used by the rental agreement generator.
        return {
            "booking_id": self.booking_id,
            "customer_name": self.customer_name,
            "email": self.email,
            "vehicle_category": self.vehicle_category,
            "pickup_date": self.pickup_date,
            "return_date": self.return_date,
            "issue_date": self.issue_date,
            "insurance": self.insurance,
            "fuel_policy": self.fuel_policy,
            "additional_driver": self.additional_driver
        }