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
            <td><strong>Soil Moisture</strong></td>
            <td>{{ plant.soil_moisture_content ? plant.soil_moisture_content + '%' : 'Loading...' }}</td>
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
    </div>
</template>

<script>
export default {
data() {
    return {
    plant: this.$route.query, // Get plant data from query params
    temperature: null,
    humidity: null,
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
        } else {
        console.error("Missing data in the response:", data);
        }
    } catch (error) {
        console.error("Error fetching weather data:", error);
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
</style>
