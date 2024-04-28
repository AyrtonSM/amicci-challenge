"use client"

// import styles from "./page.module.css";
import FormComponent from './components/main-form';

export default function Home() {

  return (<>
    <video autoPlay muted loop id="planetVideo">
      <source src="/videos/planet_video.mp4" type="video/mp4" />
    </video>

    <div className="container">
      
      <div className="content">
        <h1 className='title'>Amicci Weather</h1>
        <FormComponent /> 
      </div>
    </div>
  </>
    

    
  );
}