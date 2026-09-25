from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from pathlib import Path

from Backend.pdf.rental_pricing import RentalPricing
from Backend.pdf.rental_calculator import RentalCalculator


def create_rental_agreement(booking):
    # Get the daily price based on the vehicle category
    pricing = RentalPricing()
    daily_rate = pricing.get_daily_rate(booking["vehicle_category"])

    # Calculate rental duration and total price
    calculator = RentalCalculator(
        booking["pickup_date"],
        booking["return_date"],
        daily_rate
    )

    rental_duration = calculator.calculate_duration()
    total_price = calculator.calculate_total_price()

    # --------------------------------------------------
    # FILE NAME
    # --------------------------------------------------

    # Get the folder where this Python file is located
    pdf_folder = Path(__file__).parent

    # Create the PDF file name using the booking ID
    file_name = pdf_folder / (
        f"Meltemi_Rental_Agreement_{booking['booking_id']}.pdf"
    )

    # Create the PDF using A4 page size
    pdf = canvas.Canvas(str(file_name), pagesize=A4)

    # Get the width and height of the A4 page
    width, height = A4

    # --------------------------------------------------
    # HEADER
    # --------------------------------------------------

    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawString(50, height - 60, "MELTEMI RENTALS")

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, height - 90, "Rental Agreement")

    # Draw a line below the header
    pdf.line(50, height - 105, width - 50, height - 105)

    # --------------------------------------------------
    # BOOKING INFORMATION
    # --------------------------------------------------

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, height - 140, "Booking Information")

    pdf.setFont("Helvetica", 11)

    # Display the booking ID
    pdf.drawString(
        50,
        height - 165,
        f"Booking ID: {booking['booking_id']}"
    )

    # Display the issue date
    pdf.drawString(
        50,
        height - 185,
        f"Issue Date: {booking['issue_date']}"
    )

    # --------------------------------------------------
    # CUSTOMER INFORMATION
    # --------------------------------------------------

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, height - 225, "Customer Information")

    pdf.setFont("Helvetica", 11)

    # Display the customer's name
    pdf.drawString(
        50,
        height - 250,
        f"Customer Name: {booking['customer_name']}"
    )

    # Display the customer's email
    pdf.drawString(
        50,
        height - 270,
        f"Email: {booking['email']}"
    )

    # --------------------------------------------------
    # RENTAL INFORMATION
    # --------------------------------------------------

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, height - 310, "Rental Information")

    pdf.setFont("Helvetica", 11)

    # Display the vehicle category
    pdf.drawString(
        50,
        height - 335,
        f"Vehicle Category: {booking['vehicle_category']}"
    )

    # Display the pickup date
    pdf.drawString(
        50,
        height - 355,
        f"Pickup Date: {booking['pickup_date']}"
    )

    # Display the return date
    pdf.drawString(
        50,
        height - 375,
        f"Return Date: {booking['return_date']}"
    )

    # Display the calculated rental duration
    pdf.drawString(
        50,
        height - 395,
        f"Rental Duration: {rental_duration} days"
    )

    # --------------------------------------------------
    # PRICING
    # --------------------------------------------------

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, height - 435, "Pricing")

    pdf.setFont("Helvetica", 11)

    # Display the daily rental price
    pdf.drawString(
        50,
        height - 460,
        f"Daily Rate: EUR {daily_rate}"
    )

    # Display the calculated total price
    pdf.drawString(
        50,
        height - 480,
        f"Total Price: EUR {total_price}"
    )

    # --------------------------------------------------
    # RENTAL TERMS
    # --------------------------------------------------

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, height - 520, "Rental Terms")

    pdf.setFont("Helvetica", 11)

    # Display insurance information
    pdf.drawString(
        50,
        height - 545,
        f"Insurance: {booking['insurance']}"
    )

    # Display fuel policy
    pdf.drawString(
        50,
        height - 565,
        f"Fuel Policy: {booking['fuel_policy']}"
    )

    # Display additional driver information
    pdf.drawString(
        50,
        height - 585,
        f"Additional Driver: {booking['additional_driver']}"
    )

    # --------------------------------------------------
    # SIGNATURES
    # --------------------------------------------------

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, height - 625, "Signatures")

    pdf.setFont("Helvetica", 11)

    # Customer signature
    pdf.line(
        50,
        height - 670,
        250,
        height - 670
    )

    pdf.drawString(
        50,
        height - 690,
        "Customer Signature"
    )

    # Rental company signature
    pdf.line(
        330,
        height - 670,
        530,
        height - 670
    )

    pdf.drawString(
        330,
        height - 690,
        "Meltemi Rentals"
    )

    # --------------------------------------------------
    # SAVE PDF
    # --------------------------------------------------

    # Save the PDF file
    pdf.save()