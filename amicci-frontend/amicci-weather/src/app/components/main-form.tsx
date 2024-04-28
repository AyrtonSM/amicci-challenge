import React, { useState } from 'react';
import TableComponent from './weather-display-table';

const apiKey = '63d85afdf9688171850ff898b5c85122'
const openWeatherUrl = 'https://api.openweathermap.org/data/2.5'

const FormComponent = () => {
  const [location, setLocation] = useState('');
  const [res, setResponse] = useState('');
  const [error, setError] = useState('');
  const [citiesWeathers, setCitiesWeathers] = useState(null);

  const handleSubmit = (event) => {

    event.preventDefault();
    console.log('Form submitted:', { location});

    
    var url = openWeatherUrl + '/weather?q='+location+'&appid='+ apiKey + '&units=metric&lang=pt-br&limit=20'

    const response = fetch(url).then((response) => {
        if (!response.ok) {
            throw new Error('Failed to retrieve the location weather data');
            }
      
            return response.clone().json();
        }).then((responseData) => {
          
            setCitiesWeathers([])

            let weatherList = []
                
            let url = openWeatherUrl + '/weather?lat='+responseData.coord.lat+'&lon='+responseData.coord.lon+'&appid='+ apiKey + '&units=metric&lang=pt-br&limit=20'
            
            fetch(url).then((response) => {

                if (!response.ok) {
                    throw new Error('Failed to retrieve the location weather data');
                    }
            
                    return response.clone().json();
                }).then((weatherData) => {
                    console.log(weatherData)
                    weatherList.push(weatherData)
                    if(weatherList.length == 0)
                        setCitiesWeathers(weatherList)
                    else
                        setCitiesWeathers((prevWeathers) => [...prevWeathers, weatherData]);
                    console.log(weatherList)
                }).catch((error) => {
                    console.log('Was not able to fetch the city weather')
                    setResponse(error.message);
                });

          }).catch((error) => {
            console.log('Error Log ::',error.message )
            setResponse(error.message);
        });
 
    setLocation('')
  };

  const handleUserPosition = (event) => {
    event.preventDefault();

    navigator.geolocation.getCurrentPosition((position) => {
         
          const { latitude, longitude } = position.coords;
          console.log("Latitude:", latitude);
          console.log("Longitude:", longitude);

          let url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+latitude+','+longitude+'&sensor=true&key=AIzaSyBQpKehupn5bCtqn0v-iHpCEWAhuiOlZaQ'

        const response = fetch(url).then((response) => {
            if (!response.ok) {
                throw new Error('Failed to retrieve the location weather data');
                }
        
                return response.clone().json();
            }).then((googleData) => {
                let city_details = googleData.plus_code['compound_code'].split(',');
                let city_code_name = city_details[0].split(' ');
                let city_name = city_code_name.slice(1, city_code_name.length).join(' ');

                setLocation(city_name)

                // Adding a setTimeout of a minimum time to ensure the framework update the city name in the field.
                setTimeout(() => { document.getElementById('search-button').click()},1);
                

            }).catch((error) => {
                console.log('Was not able to fetch the city weather')
                console.log(error.message)
                setResponse(error.message);
            });
    
          // You can now use the latitude and longitude to fetch weather data or perform other actions
        },
        (error) => {
          console.error("Error getting user location:", error.message);
          alert("Error getting user location:" +  error.message)
        }
      );
  }

  return (<>
  <form onSubmit={handleUserPosition}>
                <button id="user-location" > My Place's Weather </button>
            </form>

        <form id="location-form" className="table-weather" onSubmit={handleSubmit}>
            <div>
                <label htmlFor="location">Location:</label>
                <input
                type="text"
                id="location"
                value={location}
                onChange={(e) => setLocation(e.target.value)}
                required
                />
                
            </div>
            <button id="search-button" type="submit">Search</button>
            </form>
            <div className="clear"></div>
        
            {citiesWeathers && <TableComponent data={citiesWeathers} />}

  </>
    
  );
};

export default FormComponent;
