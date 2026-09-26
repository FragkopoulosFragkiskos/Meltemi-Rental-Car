from flask import Flask, request, jsonify

from Backend.pdf.booking_data import BookingData
from Backend.pdf.rental_agreement import create_rental_agreement


app = Flask(__name__)


@app.route("/booking", methods=["POST"])
def receive_booking():
    # Get the booking data sent to the API
    booking_data = request.json

    # Create a BookingData object
    booking = BookingData(booking_data)

    # Convert the booking data into a dictionary
    # that can be used by the PDF generator
    booking_dictionary = booking.to_dictionary()

    # Create the rental agreement PDF
    create_rental_agreement(booking_dictionary)

    # Send a response back to the client
    return jsonify({
        "success": True,
        "message": "Rental agreement created successfully",
        "booking_id": booking.booking_id
    })


if __name__ == "__main__":
    app.run(debug=True)