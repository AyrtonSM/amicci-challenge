import React from 'react';

const TableComponent = ({ data }) => {

    if (!data || !Array.isArray(data)) {
        return <p>No data available</p>;
    }

    return (
        <table>
        <thead>
            <tr>
            <th>Country</th>
            <th>Latitude</th>
            <th>Longitude</th>
            <th>Name</th>
            <th>Visibility</th>
            <th>Humidity</th>
            <th>Temperature</th>
            <th>Min Temperature</th>
            <th>Max Temperature</th>
            <th>Wind Speed</th>
            <th>Weather Description</th>
            </tr>
        </thead>
        <tbody>
            {data.map((item) => (
            <tr key={item.id}>
                <td>{item.sys.country}</td>
                <td>{item.coord.lat}</td>
                <td>{item.coord.lon}</td>
                <td>{item.name}</td>
                <td>{item.weather[0].main}</td>
                <td>{item.main.humidity}</td>
                <td>{item.main.temp}°C</td>
                <td>{item.main.temp_min}°C</td>
                <td>{item.main.temp_max}°C</td>
                <td>{item.wind.speed}km/h</td>
                <td>{item.weather[0].description}</td>
            </tr>
            ))}
        </tbody>
        </table>
    );
};

export default TableComponent;