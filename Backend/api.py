from flask import Flask, request, jsonify
from dotenv import load_dotenv
from datetime import datetime
import os

from Backend.pdf.booking_data import BookingData
from Backend.pdf.rental_agreement import create_rental_agreement


# Load the variables from the .env file
load_dotenv()


app = Flask(__name__)


# Get the API key from the environment
API_KEY = os.getenv("API_KEY")


def is_customer_adult(date_of_birth, pickup_date):
    # Convert the dates from text to date objects
    birth_date = datetime.strptime(date_of_birth, "%Y-%m-%d")
    pickup = datetime.strptime(pickup_date, "%Y-%m-%d")

    # Calculate the customer's age
    age = pickup.year - birth_date.year

    # Check if the birthday has already happened
    # during the pickup year
    if (
        pickup.month < birth_date.month
        or (
            pickup.month == birth_date.month
            and pickup.day < birth_date.day
        )
    ):
        age -= 1

    return age >= 18


@app.route("/booking", methods=["POST"])
def receive_booking():

    # Get the API key sent by the client
    request_api_key = request.headers.get("X-API-Key")

    # Check if the API key is correct
    if request_api_key != API_KEY:
        return jsonify({
            "success": False,
            "message": "Invalid API key"
        }), 401

    # Get the booking data sent to the API
    booking_data = request.json

    # Check if the customer is at least 18 years old
    if not is_customer_adult(
        booking_data["dateOfBirth"],
        booking_data["pickupDate"]
    ):
        return jsonify({
            "success": False,
            "message": "Customer must be at least 18 years old on the pickup date."
        }), 400

    # Create a BookingData object
    booking = BookingData(booking_data)

    # Convert the booking data into a dictionary
    # that can be used by the PDF generator
    booking_dictionary = booking.to_dictionary()

    # Create the rental agreement PDF
    create_rental_agreement(booking_dictionary)

    # Send a successful response
    return jsonify({
        "success": True,
        "message": "Rental agreement created successfully",
        "booking_id": booking.booking_id
    })


if __name__ == "__main__":
    app.run(debug=True)