<template>
  <div>
    <main>
      <div class="headbutton">
        <div class="head">
          <h1 class="heading">{{ greeting }}, {{ firstName }}! {{ emoji }}</h1>
          <p class="subheading">Your plants appear here! </p>
        </div>
      </div>
      
      <section class="plants">
        <div v-for="plant in plants" :key="plant.id" class="plant-card">
          <img :src="`http://localhost:5000/uploads/${plant.photo}`" alt="plant.name">
          <h3>{{ plant.name }}</h3>
          <p><strong>Birth Date :</strong> {{ plant.start_date }}</p>
          <p><strong>Scientific Name :</strong> {{ plant.scientific_name }}</p>
          <p><strong>Temperature:</strong> {{ plant.soil_moisture_content }}%</p>
          <p><strong>Humidity Content:</strong> {{ plant.humidity_content }}%</p>
          <router-link :to="{ name: 'plantdetails', query: plant }">
            <button class="viewmore">View More</button>
          </router-link>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
export default {
  data() {
    return {
      greeting: new Date().getHours() < 12 ? "Good Morning" :
                new Date().getHours() < 18 ? "Good Afternoon" :
                "Good Evening",
      plants: [],
      emoji:  new Date().getHours() < 12 ? "🌄" :
              new Date().getHours() < 18 ? "🌞" :
              "🌙",
      firstName: sessionStorage.getItem("firstName") || "Guest",
      // This will store the fetched plants data
    };
  }, // Receive firstName from the parent component (login)
  methods: {
    handleLogout() {
      sessionStorage.removeItem("user_id"); // Example of clearing session storage
      this.$router.push({ name: "login" }); // Redirect to login on logout
      alert("Logged out successfully!!") 
    },
    fetchPlants() {
      const userId = sessionStorage.getItem('user_id'); // Get user ID from session storage

      if (!userId) {
        return this.$router.push({ name: "login" }); // Redirect to login if user is not logged in
      }

      fetch('/api/plants', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'same-origin'  // Ensures session cookies are included
      })
      .then(response => response.json())
      .then(data => {
        this.plants = data; // Store the fetched plants data in the 'plants' array
      })
      .catch(error => {
        console.error("Error fetching plants:", error);
      });
    }
  },
  mounted() {
    this.fetchPlants(); // Fetch plants when the component is mounted
  }
};
</script>

<style scoped>
.headbutton {
  display: flex;
}

.logout {
  flex-basis: 10%;
}
.head {
  flex-basis: 90%;
}

.heading {
  text-align: left;
  font-size: 35px;
  font-family: "Poppins", serif;
  font-weight: 900px;
  margin-left: 25px;
}
.subheading {
  text-align: left;
  font-size: 20px;
  font-family: "Poppins", serif;
  font-weight: 300px;
  margin-left: 25px;
}
.viewmore{
  margin-top: 20px;
  background: green;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
  border-radius: 5px; 
  font-family: "Poppins";
}
button {
  margin-top: 20px;
  background: #ff4d4d;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
  border-radius: 5px;
}

main {
  text-align: center;
  margin: 2rem;
}

.plants {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  margin-top: 2rem;
  font-family: "Poppins", serif;
  font-weight: 500px;
  margin-left: 25px;
}

.plant-card {
  background: #ffffff;
  padding: 1.5rem;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.plant-card:hover {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 3.5);
}

.plant-card img {
  width: 300px;
  height: 400px;
}

.plant-card h3 {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}

.plant-card p {
  font-size: 1rem;
  color: #555;
}
</style>
