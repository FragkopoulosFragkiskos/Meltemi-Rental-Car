import { useState } from 'react'

function RequestForm() {
  // Stores all the information entered by the user
  const [formData, setFormData] = useState({
    name: '',
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

  // Runs when the user submits the form
  const handleSubmit = async (event) => {
    // Prevents the page from refreshing
    event.preventDefault()

    // Clears the previous message
    setStatusMessage('')

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
            name: '',
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
      <div className="form-row">

        {/* Customer name */}
        <div className="form-group">
          <label>Full Name</label>

          <input
            type="text"
            name="name"
            placeholder="Full Name"
            value={formData.name}
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