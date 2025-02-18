<template>
    <div class="container">
      <h1 class="title"><u>Plant Analysis</u></h1>
  
      <div class="content">
        <!-- Left Section: Tables -->
        <div class="tables-container">
          <!-- First Table: User-Entered Plant Data -->
          <div class="table-container">
            <h2>Entered Values for {{ plant.name }}</h2>
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
            <h2>Expected Values for {{ plant.name }}</h2>
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


        <!-- Right Section: Recommendation & Plant Identification -->
        <div class="right-section">
          <div v-if="recommendation" class="recommendation-container">
            <h2>Recommendations</h2>
            <p>{{ recommendation }}</p>
          </div>
  
          <!-- Image Upload for Plant ID -->
          
        </div>
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
        recommendation: "",
        identifiedPlant: null,
        loading: false,
        error: null,
      };
    },
    methods: {
      async handleFileUpload(event) {
        const file = event.target.files[0];
        if (!file) return;
  
        this.loading = true;
        this.error = null;
  
        const formData = new FormData();
        formData.append("image", file);
  
        try {
          const response = await fetch("http://localhost:5000/identify-plant", {
            method: "POST",
            body: formData,
          });
  
          if (!response.ok) throw new Error("Failed to identify plant");
  
          const data = await response.json();
          if (data.error) {
            this.error = data.error;
          } else {
            this.identifiedPlant = data;
          }
        } catch (error) {
          this.error = "Error identifying plant.";
          console.error(error);
        } finally {
          this.loading = false;
        }
      },
      async fetchWeatherData() {
        try {
          const response = await fetch("http://localhost:5000/weather");
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          const data = await response.json();
  
          if (data.temperature && data.humidity) {
            this.temperature = data.temperature;
            this.humidity = data.humidity;
            this.generateRecommendation();
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

          // Temperature Conditions
          if (actualTemp < expectedTemp - 5) {
              recommendations.push(`• The actual temperature (${actualTemp}°C) is significantly lower than the expected temperature (${expectedTemp}°C). Consider using heating lamps, insulating the plant area, or moving it to a warmer location.`);
          } else if (actualTemp < expectedTemp) {
              recommendations.push(`• The actual temperature (${actualTemp}°C) is slightly lower than the expected temperature (${expectedTemp}°C). Use mild heating sources or adjust sunlight exposure.`);
          } else if (actualTemp > expectedTemp + 5) {
              recommendations.push(`• The actual temperature (${actualTemp}°C) is significantly higher than the expected temperature (${expectedTemp}°C). Ensure proper ventilation, provide shade, and consider watering more frequently.`);
          } else if (actualTemp > expectedTemp) {
              recommendations.push(`• The actual temperature (${actualTemp}°C) is slightly higher than the expected temperature (${expectedTemp}°C). Monitor for heat stress and adjust watering schedules accordingly.`);
          }

          // Humidity Conditions
          if (actualHumidity < expectedHumidity - 10) {
              recommendations.push(`• The actual humidity (${actualHumidity}%) is significantly lower than the expected humidity (${expectedHumidity}%). Use a humidifier, misting, or place the plant near a water source to increase humidity.`);
          } else if (actualHumidity < expectedHumidity) {
              recommendations.push(`• The actual humidity (${actualHumidity}%) is slightly lower than the expected humidity (${expectedHumidity}%). Regular misting and grouping plants together can help maintain humidity levels.`);
          } else if (actualHumidity > expectedHumidity + 10) {
              recommendations.push(`• The actual humidity (${actualHumidity}%) is significantly higher than the expected humidity (${expectedHumidity}%). Ensure good air circulation and avoid overwatering to prevent fungal growth.`);
          } else if (actualHumidity > expectedHumidity) {
              recommendations.push(`• The actual humidity (${actualHumidity}%) is slightly higher than the expected humidity (${expectedHumidity}%). Consider reducing watering and increasing airflow.`);
          }

          // Combined Conditions for More Specific Guidance
          if (actualTemp > expectedTemp && actualHumidity < expectedHumidity) {
              recommendations.push(`• The plant is experiencing high temperatures and low humidity. Increase watering, provide shade, and mist regularly to balance conditions.`);
          } else if (actualTemp < expectedTemp && actualHumidity > expectedHumidity) {
              recommendations.push(`• The plant is in a cool and humid environment. Reduce excessive moisture and ensure proper drainage to prevent root rot.`);
          }

          this.recommendation = recommendations.length > 0 ? recommendations.join(" ") : "• The environmental conditions are optimal. Keep monitoring for any changes.";
    }
  }
    },
    
    mounted() {
      this.fetchWeatherData();
    },
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 90%;
    margin-left: 30px;
    margin-top: 20px;
    margin-right: 20px;
    text-align: center;
    font-family: "Poppins", sans-serif;
  }
  .title {
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 40px;
    margin-left:55px;
  }
  .content {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }
  .tables-container {
    width: 50%;
  }
  .right-section {
    flex-basis: 40%;
    width: 45%;
  }
  .table-container {
    margin-left: 45px;
    background: #ffffff;
    border-radius: 10px;
    width: 80%;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  }

  .error {
    color: red;
    font-weight: bold;
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
  color: gray;
}

tr:hover {
  background: #f9f9f9;
}

.recommendation-container {
  flex-basis: 50%;
  width: 100%;
  background: #E8F5E9;
  padding: 20px;
  margin-left: 15px;

  border-radius: 10px;
  font-size: 18px;
  font-weight: bold;
  color: green;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}
</style>