from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

from Backend.pdf.booking_data import BookingData
from Backend.pdf.rental_agreement import create_rental_agreement


# Load the variables from the .env file
load_dotenv()


app = Flask(__name__)


# Get the API key from the environment
API_KEY = os.getenv("API_KEY")


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