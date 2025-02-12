<template>
    <nav class="navbar">
        <img class="logo" :src="logoIm" alt="">
        <ul class="navitems">
            <li class="nav-item">Features</li>
            <li class="nav-item">Community</li>
            <li class="nav-item">Learning Hub</li>
            <li class="nav-item">About Us</li>
            <li class="nav-item">Contact</li>
        </ul>
        <button>Sign-Up / Sign-In</button>
    </nav>
</template>

<script>
import logoimage from '/src/assets/images/Pasted_image.png'
export default{
    data(){
        return{
            logoIm:logoimage
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
  display: flex;
  align-items: center;
  padding: 15px 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Logo styles */
.logo {
  font-size: 24px;
  font-weight: bold;
  margin-right: 450px;
  margin-left: 80px;
  height: 50px;

}

/* Navigation list */
.navitems {
  list-style: none;
  display: inline-flex;
  gap: 25px; /* Space between items */
  margin: 0;
  padding: 0;
}

/* Individual nav items */
.nav-item {
  cursor: pointer;
  font-size: 16px;
  font-family: "Poppins", serif;
  font-optical-sizing: auto;
  font-weight: Black (100);
  font-size: 14px;
  padding: 8px;
  transition:500ms;

}

.nav-item:hover {
  padding: 8px;
  border-radius: 10px;
  background-color: #a9e22b;
  transition: 500ms;
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
    background-color: gray;
    transition: 500ms;
}
</style>