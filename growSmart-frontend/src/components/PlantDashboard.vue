<template>
    <div>
        <main>
          <div class="headbutton">
            <div class="head"><h1 class="heading">{{ greeting }}, {{ firstName }}! 🌞</h1>
            <p class="subheading">Your plants are thriving! </p></div>
            <div class="logout"><button>Logout</button></div>
            
          </div>
            <section class="plants">
                <div v-for="plant in plants" :key="plant.id" class="plant-card">
                    <img :src="plant.photo" alt="plant.name">
                    <h3>{{ plant.name }}</h3>
                    <p><strong>Start Date:</strong> {{ plant.start_date }}</p>
                    <p><strong>Soil Moisture Content:</strong> {{ plant.soil_moisture_content }}%</p>
                    <p><strong>Humidity Content:</strong> {{ plant.humidity_content }}%</p>
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
            plants: [
                        {
                            "id": 1,
                            "name": "Tomato",
                            "start_date": "2025-01-01",
                            "soil_moisture_content": 45,
                            "humidity_content": 60,
                            "photo": "/plants/p1.jpeg"
                        },
                        {
                            "id": 2,
                            "name": "Lettuce",
                            "start_date": "2025-02-01",
                            "soil_moisture_content": 35,
                            "humidity_content": 70,
                            "photo": "/plants/p2.jpeg"
                        },
                        {
                            "id": 3,
                            "name": "Cucumber",
                            "start_date": "2025-01-15",
                            "soil_moisture_content": 40,
                            "humidity_content": 65,
                            "photo": "/plants/p3.jpeg"
                        },
                        {
                            "id": 4,
                            "name": "Mint",
                            "start_date": "2025-01-25",
                            "soil_moisture_content": 50,
                            "humidity_content": 80,
                            "photo": "/plants/p4.jpeg"
                        },
                        {
                            "id": 5,
                            "name": "Cabbage",
                            "start_date": "2025-01-25",
                            "soil_moisture_content": 50,
                            "humidity_content": 80,
                            "photo": "/plants/p1.jpeg"
                        }
                    ]// Holds fetched plant data
        };
    },
    props: ["firstName"], // Receive firstName from login
    methods: {
        handleLogout() {
            this.$router.push({ name: "login" }); // Redirect to login on logout
        }
    }
};
</script>

<style scoped>
.headbutton{
  display: flex;
}

.logout{
  flex-basis: 10%;
}
.head{
  flex-basis: 90%;
}

.heading{
    text-align: left;
    font-size: 35px;
    font-family: "Poppins", serif;
    font-weight: 900px;
    margin-left:25px;
}
.subheading{
    text-align: left;
    font-size: 20px;
    font-family: "Poppins", serif;
    font-weight: 300px;
    margin-left:25px;
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
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

.plant-card img{
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
