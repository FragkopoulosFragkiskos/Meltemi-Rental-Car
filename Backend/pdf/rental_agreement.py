from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def create_rental_agreement():
    # Name of the PDF file that will be created
    file_name = "test_rental_agreement.pdf"

    # Create a PDF using A4 page size
    pdf = canvas.Canvas(file_name, pagesize=A4)

    # Get the width and height of the A4 page
    width, height = A4

    # Title
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(50, height - 60, "MELTEMI RENTALS")

    # Document title
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, height - 100, "Rental Agreement")

    # Test booking information
    pdf.setFont("Helvetica", 11)

    pdf.drawString(50, height - 150, "Booking ID: MR-2026-0001")
    pdf.drawString(50, height - 175, "Customer: Fragkiskos Fragkopoulos")
    pdf.drawString(50, height - 200, "Vehicle Category: Economy")
    pdf.drawString(50, height - 225, "Pickup Date: 27/09/2026")
    pdf.drawString(50, height - 250, "Return Date: 30/09/2026")
    pdf.drawString(50, height - 275, "Daily Rate: €30")
    pdf.drawString(50, height - 300, "Total Price: €90")

    # Create the PDF file
    pdf.save()


# Run the function when this file is executed directly
if __name__ == "__main__":
    create_rental_agreement()