import './App.css'
import Header from './components/Header'
import Hero from './components/Hero'
import Cars from './components/Cars'
import WhyUs from './components/WhyUs'
import RequestForm from './components/RequestForm'
import Footer from './components/Footer'


function App() {
  return (
    <>
      <Header />

      <Hero />

      <Cars />

      <WhyUs />

      <section className="request-form-section">
        <RequestForm />
      </section>

      <Footer />


    </>
  )
}

export default App