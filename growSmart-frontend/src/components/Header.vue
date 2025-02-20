<template>
    <nav class="navbar">
        <router-link to="/"><img class="logo" :src="logoIm" alt=""></router-link>
        <ul class="navitems">

            <router-link to="/plant-dashboard">
                <li class="nav-item">Home</li>
            </router-link>

            

            <router-link to="/learning-hub" v-if="showLearningHub">
                <li class="nav-item">Learning Hub</li>
            </router-link>

            <router-link to="/plant-dashboard" v-if="showBack">
                <li class="nav-item">Back</li>
            </router-link>

            <router-link v-if="showAboutUs" to="/about-us">
                <li class="nav-item">About Us</li>
            </router-link>

            <router-link v-if="showContact" to="/contact-us">
                <li class="nav-item">Contact</li>
            </router-link>

            <router-link v-if="showLogin" to="/login">
                <li class="nav-item">Login</li>
            </router-link>

            <router-link v-if="showRegister" to="/register">
                <li class="nav-item">Register</li>
            </router-link>

            <router-link v-if="showDashboard" to="/plant-dashboard">
                <li class="nav-item">View Plants</li>
            </router-link>
            
            <router-link v-if="showAddPlant" to="/add-plant">
                <li class="nav-item">Add Plant</li>
            </router-link>

            <router-link v-if="showCommunity" to="/community">
                <li class="nav-item">Community</li>
            </router-link>

            <router-link v-if="showChatBot" to="/chatbot">
                <li class="nav-item">Chatbot</li>
            </router-link>

            <router-link to="/upgrade">
                <li class="nav-item">Upgrade</li>
            </router-link>


            <router-link v-if="showLogout" to="/" @click="handleLogout">
                <li class="nav-itemb">Logout</li>
            </router-link>

            
            
        </ul>   
    </nav>
</template>

<script>
import logoimage from '/src/assets/images/image-removebg-preview.png'
export default{
    data(){
        return{
            logoIm:logoimage
        }
    },
    methods:{
        handleLogout() {
        sessionStorage.removeItem("user_id"); // Example of clearing session storage
        this.$router.push({ name: "login" }); // Redirect to login on logout
        alert("Logged out successfully!!") 
      }
    },
    computed:{
        showAddPlant(){
            return this.$route.name === "PlantDashboard"; // Show Add Plant only on dashboard
        },
        showDashboard(){
            return this.$route.name === "AddPlant" || this.$route.name === "community";
        },
        showCommunity(){
            return this.$route.name === "PlantDashboard" || this.$route.name === "AddPlant";
        },
        showAboutUs(){
            return this.$route.name === "home" || this.$route.name === "register" || this.$route.name === "login" || this.$route.name === "upgrade";
        },
        showContact(){
            return this.$route.name === "home" || this.$route.name === "register" || this.$route.name === "login"  || this.$route.name=== "aboutus" || this.$route.name === "learningub" || this.$route.name === "upgrade";
        },
        showLogin(){
            return this.$route.name === "home" || this.$route.name === "register" || this.$route.name=== "aboutus" || this.$route.name=== "contactus" || this.$route.name === "learninghub" || this.$route.name === "upgrade";
        },
        showRegister(){
            return this.$route.name === "home" || this.$route.name === "login" || this.$route.name=== "aboutus" || this.$route.name=== "contactus"  || this.$route.name === "learninghub" || this.$route.name === "upgrade";
        },
        showLogout(){
            return this.$route.name !== "home" && this.$route.name !== "login" && this.$route.name !== "register" && this.$route.name !== "aboutus" && this.$route.name !== "contactus" && this.$route.name !== "learninghub";
        },
        showChatBot(){
            return this.$route.name === "PlantDashboard" || this.$route.name === "AddPlant" || this.$route.name === "plantdetails" || this.$route.name === "community";
        },
        showBack(){
            return this.$route.name === "plantdetails"
        },
        showLearningHub(){
            return this.$route.name === "login" || this.$route.name === "register" || this.$route.name === "home" || this.$route.name === "upgrade";
        }
    }
}
</script>

<style scoped>
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInRight {
    from {
        opacity: 0;
        transform: translateX(50px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}
/* Navbar container */
.navbar {
    background: #E8F5E9;
  display: flex;
  align-items: center;
  padding: 15px 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease-in-out;
}

/* Logo styles */
.logo {
  font-size: 24px;
  font-weight: bold;
  margin-right: 400px;
  margin-left: 80px;
  height: 50px;

}

/* Navigation list */
.navitems {
  list-style: none;
  display: inline-flex;
  gap: 30px; /* Space between items */
  margin: 0;
  padding: 0;
}

.navitems a{
    text-decoration: none;
    color: inherit;
}

/* Individual nav items */
.nav-item {
  cursor: pointer;
  font-size: 16px;
  text-decoration: none;
  color: black;
  font-family: "Poppins", serif;
  font-optical-sizing: auto;
  font-weight: Black (100);
  font-size: 14px;
  padding: 8px;
  transition:500ms;
  border-radius: 10px;
}

.nav-itemb{
    font-family: "Poppins", serif;
    font-optical-sizing: auto;
    font-weight: Black (100);
    font-size: 14px;
    background: #ff4d4d;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    cursor: pointer;
    border-radius: 5px;
}

router-link{
    text-decoration: none;
}


.nav-item:hover {
  padding: 8px;
  background: #218838; /* Darker green */
  transform: scale(1.05); /* Slight pop effect */
  transition: all 0.3s ease-in-out;
  color: white;
}

.navbar button{
    margin-left: 20px;
    padding: 10px;
    border-radius: 10px;
    border: none;
    transition: 500ms;
    cursor: pointer;
}
.navbar button:hover{    
    background: #218838; /* Darker green */
    color: white;
    transform: scale(1.05); /* Slight pop effect */
    transition: all 0.3s ease-in-out;

}
</style>