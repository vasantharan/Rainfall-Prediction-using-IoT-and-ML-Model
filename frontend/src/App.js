import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [temperature, setTemperature] = useState(null);
  const [humidity, setHumidity] = useState(null);
  const [precipitation, setPrecipitation] = useState(null);

  const fetchSensorData = async () => {
    try {
      const response = await fetch('http://192.168.43.162/');
      const data = await response.json();
      setTemperature(data.temperature);
      setHumidity(data.humidity);
      const predictionResponse = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          features: [data.temperature, data.humidity],  
        }),
      });

      const predictionData = await predictionResponse.json();
      setPrecipitation(predictionData.prediction);

    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  useEffect(() => {
    fetchSensorData(); 
    const interval = setInterval(fetchSensorData, 15000); 
    return () => clearInterval(interval); 
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Sensor Data</h1>
        <p>Temperature: {temperature !== null ? `${temperature} °C` : 'Loading...'}</p>
        <p>Humidity: {humidity !== null ? `${humidity} %` : 'Loading...'}</p>
        <p>Predicted Precipitation: {precipitation !== null ? `${precipitation} %` : 'Loading...'}</p>
      </header>
    </div>
  );
}

export default App;
