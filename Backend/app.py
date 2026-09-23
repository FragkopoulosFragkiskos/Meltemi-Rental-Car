from flask import Flask, request, jsonify

# Create the Flask application
app = Flask(__name__)


# Test route
@app.route("/")
def home():
    return "Meltemi Rentals Backend is running!"


# Rental request endpoint
@app.route("/api/rental-request", methods=["POST"])
def rental_request():

    # Get the data sent by the frontend
    data = request.get_json()

    # Print the received data in the terminal
    print("Rental request received:")
    print(data)

    # Send a response back to the frontend
    return jsonify({
        "message": "Rental request received successfully!"
    }), 200


# Start the Flask server
if __name__ == "__main__":
    app.run(debug=True)