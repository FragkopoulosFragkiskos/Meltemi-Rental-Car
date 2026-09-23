// Import the car images from the assets folder
import yaris from '../assets/yaris.jpg'
import civic from '../assets/honda.jpg'
import tucson from '../assets/hyundai.jpg'
import tesla from '../assets/porsche.jpg'

function Cars() {
  return (
    <section id="cars">
      <h2>Choose the right car based on your needs</h2>

      <div className="cars-container">

        {/* Toyota Yaris */}
        <div className="car">
          <img src={yaris} alt="Toyota Yaris" />
          <h3>Economy</h3>
          <p>Small and practical car for exploring Kos.</p>
          <p>€35 / day</p>
        </div>

        {/* Honda Civic */}
        <div className="car">
          <img src={civic} alt="Honda Civic" />
          <h3>Compact</h3>
          <p>Comfortable car for couples and small families.</p>
          <p>€45 / day</p>
        </div>

        {/* Hyundai Tucson */}
        <div className="car">
          <img src={tucson} alt="Hyundai Tucson" />
          <h3>Comfortable</h3>
          <p>Spacious and comfortable for longer trips.</p>
          <p>€60 / day</p>
        </div>

        {/* Tesla Model 3 */}
        <div className="car">
          <img src={tesla} alt="Tesla Model 3" />
          <h3>Premium</h3>
          <p>Enjoy extra comfort and a premium driving experience.</p>
          <p>€110 / day</p>
        </div>

      </div>
    </section>
  )
}

export default Cars