from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def create_rental_agreement():
    # Name of the PDF file that will be created
    file_name = "test_rental_agreement.pdf"

    # Create a PDF using A4 page size
    pdf = canvas.Canvas(file_name, pagesize=A4)

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

    pdf.drawString(50, height - 165, "Booking ID: MR-2026-0001")
    pdf.drawString(50, height - 185, "Issue Date: 24/09/2026")

    # --------------------------------------------------
    # CUSTOMER INFORMATION
    # --------------------------------------------------

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, height - 225, "Customer Information")

    pdf.setFont("Helvetica", 11)

    pdf.drawString(50, height - 250, "Customer Name: Fragkiskos Fragkopoulos")
    pdf.drawString(50, height - 270, "Email: customer@example.com")

    # --------------------------------------------------
    # RENTAL INFORMATION
    # --------------------------------------------------

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, height - 310, "Rental Information")

    pdf.setFont("Helvetica", 11)

    pdf.drawString(50, height - 335, "Vehicle Category: Economy")
    pdf.drawString(50, height - 355, "Pickup Date: 27/09/2026")
    pdf.drawString(50, height - 375, "Return Date: 30/09/2026")
    pdf.drawString(50, height - 395, "Rental Duration: 3 days")

    # --------------------------------------------------
    # PRICING
    # --------------------------------------------------

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, height - 435, "Pricing")

    pdf.setFont("Helvetica", 11)

    pdf.drawString(50, height - 460, "Daily Rate: €30")
    pdf.drawString(50, height - 480, "Total Price: €90")

    # --------------------------------------------------
    # RENTAL TERMS
    # --------------------------------------------------

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, height - 520, "Rental Terms")

    pdf.setFont("Helvetica", 11)

    pdf.drawString(50, height - 545, "Insurance: Full insurance included")
    pdf.drawString(50, height - 565, "Fuel Policy: Full-to-full")
    pdf.drawString(50, height - 585, "Additional Driver: Included")

    # --------------------------------------------------
    # SIGNATURES
    # --------------------------------------------------

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, height - 625, "Signatures")

    pdf.setFont("Helvetica", 11)

    pdf.line(50, height - 670, 250, height - 670)
    pdf.drawString(50, height - 690, "Customer Signature")

    pdf.line(330, height - 670, 530, height - 670)
    pdf.drawString(330, height - 690, "Meltemi Rentals")

    # Create the PDF file
    pdf.save()


# Run the function when this file is executed directly
if __name__ == "__main__":
    create_rental_agreement()