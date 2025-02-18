<template>
    <div class="container">
      <h1 class="title">Plant AI Dashboard</h1>
  
      <!-- First Table: User-Entered Plant Data -->
      <div class="table-container">
        <h2>Entered Values</h2>
        <table>
          <tr>
            <th>Parameter</th>
            <th>Value</th>
          </tr>
          <tr>
            <td><strong>Temperature</strong></td>
            <td>{{ plant.soil_moisture_content ? plant.soil_moisture_content + '°C' : 'Loading...' }}</td>
          </tr>
          <tr>
            <td><strong>Humidity</strong></td>
            <td>{{ plant.humidity_content ? plant.humidity_content + '%' : 'Loading...' }}</td>
          </tr>
        </table>
      </div>
  
      <!-- Second Table: Expected Weather Values -->
      <div class="table-container">
        <h2>Expected Values</h2>
        <table>
          <tr>
            <th>Parameter</th>
            <th>Value</th>
          </tr>
          <tr>
            <td><strong>Temperature</strong></td>
            <td>{{ temperature ? temperature + '°C' : 'Loading...' }}</td>
          </tr>
          <tr>
            <td><strong>Humidity</strong></td>
            <td>{{ humidity ? humidity + '%' : 'Loading...' }}</td>
          </tr>
        </table>
      </div>
  
      <!-- Recommendation Section -->
      <div v-if="recommendation" class="recommendation-container">
        <h2>Recommendations</h2>
        <p>{{ recommendation }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        plant: this.$route.query, // Get plant data from query params
        temperature: null,
        humidity: null,
        recommendation: "", // Holds recommendation message
      };
    },
    methods: {
      async fetchWeatherData() {
        try {
          const response = await fetch("http://localhost:5000/weather"); // Adjust URL if needed
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          const data = await response.json();
  
          console.log("Weather Data:", data);
  
          if (data.temperature && data.humidity) {
            this.temperature = data.temperature;
            this.humidity = data.humidity;
            this.generateRecommendation();
          } else {
            console.error("Missing data in the response:", data);
          }
        } catch (error) {
          console.error("Error fetching weather data:", error);
        }
      },
      generateRecommendation() {
        if (this.plant.soil_moisture_content && this.temperature && this.plant.humidity_content && this.humidity) {
          const actualTemp = parseFloat(this.plant.soil_moisture_content);
          const expectedTemp = parseFloat(this.temperature);
          const actualHumidity = parseFloat(this.plant.humidity_content);
          const expectedHumidity = parseFloat(this.humidity);
  
          let recommendations = [];
  
          if (actualTemp < expectedTemp) {
            recommendations.push(`The actual temperature (${actualTemp}°C) is lower than the expected temperature (${expectedTemp}°C). Consider using a greenhouse setup, adjusting lighting, or placing the plant in a warmer spot.`);
          }
  
          if (actualHumidity < expectedHumidity) {
            recommendations.push(`The actual humidity (${actualHumidity}%) is lower than the expected humidity (${expectedHumidity}%). Increase humidity by misting the plant, using a humidity tray, or placing a water source nearby.`);
          }
  
          this.recommendation = recommendations.length > 0 ? recommendations.join(" ") : "The environmental conditions are optimal. Keep monitoring for any changes.";
        }
      }
    },
    mounted() {
      this.fetchWeatherData();
    }
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
    margin: 20px auto;
    text-align: center;
    font-family: "Poppins", sans-serif;
  }
  
  .title {
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 20px;
  }
  
  .table-container {
    background: #ffffff;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  h2 {
    margin-bottom: 10px;
    color: #333;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 18px;
  }
  
  th, td {
    padding: 12px;
    border: 1px solid #ddd;
    text-align: left;
  }
  
  th {
    background: #f4f4f4;
    color: #333;
  }
  
  td {
    background: #fcfcfc;
  }
  
  /* Hover effect for better UI experience */
  tr:hover {
    background: #f9f9f9;
  }
  
  /* Recommendation Section */
  .recommendation-container {
    background: #E8F5E9;
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
    font-size: 18px;
    font-weight: bold;
    color: green;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  }
  </style>
