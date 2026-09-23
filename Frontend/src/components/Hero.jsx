import heroBackground from '../assets/herosuv.jpg'

function Hero() {
  return (
    <main
      style={{
        backgroundImage: `url(${heroBackground})`,
      }}
    >
      <section className="hero">

        <div className="hero-text">
          <h2>Explore Kos with freedom</h2>

          <p>
            Rent a car and discover the island at your own pace.
          </p>

          <button>
            Request a car
          </button>
        </div>

      </section>
    </main>
  )
}

export default Hero