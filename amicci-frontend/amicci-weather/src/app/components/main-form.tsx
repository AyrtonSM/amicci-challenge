import React, { useState } from 'react';

const FormComponent = () => {
  // Define state variables for form inputs
  const [location, setLocation] = useState('');

  // Function to handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Form submitted:', { location});
    setLocation('');

  };

  return (
    <form onSubmit={handleSubmit}>
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
      <button type="submit">Search</button>
    </form>
  );
};

export default FormComponent;
