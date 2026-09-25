from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/booking", methods=["POST"])
def receive_booking():
    # Get the booking data sent by Make
    booking_data = request.json

    # Print the received data for now
    print("Booking received:")
    print(booking_data)

    # Send a response back to Make
    return jsonify({
        "success": True,
        "message": "Booking received successfully"
    })


if __name__ == "__main__":
    app.run(debug=True)