import { useState } from 'react'

function RequestForm() {
  // Stores all the information entered by the user
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    dateOfBirth: '',
    email: '',
    pickupDate: '',
    returnDate: '',
    car: '',
    message: '',
  })

  // Stores the message returned by Make
  const [statusMessage, setStatusMessage] = useState('')

  // Updates the corresponding field when the user types
  const handleChange = (event) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value,
    })
  }

  // Checks if the customer is at least 18 years old on the pickup date
  const isCustomerAdult = () => {
    const birthDate = new Date(formData.dateOfBirth)
    const pickupDate = new Date(formData.pickupDate)

    let age = pickupDate.getFullYear() - birthDate.getFullYear()

    const monthDifference = pickupDate.getMonth() - birthDate.getMonth()

    // If the birthday has not happened yet in the pickup year,
    // subtract one year from the age
    if (
      monthDifference < 0 ||
      (monthDifference === 0 &&
      pickupDate.getDate() < birthDate.getDate())
    ) {
      age--
    }

    return age >= 18
  }

  // Runs when the user submits the form
  const handleSubmit = async (event) => {
    // Prevents the page from refreshing
    event.preventDefault()

    // Clears the previous message
    setStatusMessage('')

    // Checks if the customer is at least 18 years old
    if (!isCustomerAdult()) {
      setStatusMessage(
        'You must be at least 18 years old on the pickup date.'
      )
      return
    }

    try {
      // Sends the form data to the Make webhook
      const response = await fetch(
        import.meta.env.VITE_MAKE_WEBHOOK_URL,
        {
          method: 'POST',

          // Tells Make that we are sending JSON data
          headers: {
            'Content-Type': 'application/json',
          },

          // Converts the form data into JSON
          body: JSON.stringify(formData),
        }
      )

      // Checks if Make returned a successful HTTP response
      if (response.ok) {
        // Reads the JSON response sent by Make
        const result = await response.json()

        // Shows the message returned by Make
        setStatusMessage(result.message)

        // If the booking was successful, clear the form
        if (result.success) {
          setFormData({
            firstName: '',
            lastName: '',
            dateOfBirth: '',
            email: '',
            pickupDate: '',
            returnDate: '',
            car: '',
            message: '',
          })
        }
      } else {
        // Shows an error if the server returned an error
        setStatusMessage('Something went wrong. Please try again.')
      }
    } catch (error) {
      // Handles connection or network errors
      console.error('Error sending rental request:', error)
      setStatusMessage('Unable to contact the server. Please try again.')
    }
  }

  return (
    // Main form container
    <form className="request-form" onSubmit={handleSubmit}>
      <h2>Rental Request Form</h2>

      {/* Customer information */}

      {/* First name and last name */}
      <div className="form-row">

      {/* Customer first name */}
      <div className="form-group">
        <label>First Name</label>

        <input
          type="text"
          name="firstName"
          placeholder="First Name"
          value={formData.firstName}
          onChange={handleChange}
        />
      </div>

      {/* Customer last name */}
      <div className="form-group">
        <label>Last Name</label>

        <input
          type="text"
          name="lastName"
          placeholder="Last Name"
          value={formData.lastName}
          onChange={handleChange}
        />
      </div>

    </div>

      {/* Date of birth and email */}
      <div className="form-row">

      {/* Customer date of birth */}
      <div className="form-group">
        <label>Date of Birth</label>

        <input
          type="date"
          name="dateOfBirth"
          value={formData.dateOfBirth}
          onChange={handleChange}
        />
      </div>

      {/* Customer email */}
      <div className="form-group">
        <label>Email</label>

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
        />
      </div>

    </div>

      {/* Rental dates */}
      <div className="form-row">

        {/* Pickup date */}
        <div className="form-group">
          <label>Pickup Date</label>

          <input
            type="date"
            name="pickupDate"
            value={formData.pickupDate}
            onChange={handleChange}
          />
        </div>

        {/* Return date */}
        <div className="form-group">
          <label>Return Date</label>

          <input
            type="date"
            name="returnDate"
            value={formData.returnDate}
            onChange={handleChange}
          />
        </div>

      </div>

      {/* Car category */}
      <div className="form-group">
        <label>Car Category</label>

        <select
          name="car"
          value={formData.car}
          onChange={handleChange}
        >
          {/* Default option */}
          <option value="">Select a car category</option>

          {/* Available car categories */}
          <option value="Economy">Economy</option>
          <option value="Compact">Compact</option>
          <option value="Comfortable">Comfortable</option>
          <option value="Premium">Premium</option>
        </select>
      </div>

      {/* Additional message */}
      <div className="form-group">
        <label>Message</label>

        <textarea
          name="message"
          placeholder="Message"
          value={formData.message}
          onChange={handleChange}
        />
      </div>

      {/* Submit button */}
      <button type="submit">
        Request Booking
      </button>

      {/* Message returned by Make */}
      {statusMessage && (
        <p className="status-message">
          {statusMessage}
        </p>
      )}
    </form>
  )
}

export default RequestForm