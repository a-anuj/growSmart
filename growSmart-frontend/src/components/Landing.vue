<template>
    <div class="container">
      <div class="textfield">
        <h1><span ref="typedText" class="text-green-600"></span></h1>
        <p>
          AI-powered gardening made effortless for urban dwellers.<br />
          Get real-time insights, personalized guidance, and grow fresh,<br />
          organic produce right from your home—no experience needed!
        </p>
        <button>Register Now</button>
      </div>
      <div class="imagefield">
        <div class="img">
          <img :src="imageSrc" alt="Gardening Image" />
        </div>
      </div>
    </div>
  </template>




<script setup>
import { onMounted, ref } from "vue";
import Typed from "typed.js";

const typedText = ref(null);
const imageSrc = "/src/assets/images/freepik__the-style-is-candid-image-photography-with-natural__4038.png"; 

onMounted(() => {
  new Typed(typedText.value, {
    strings: ["Harvest Fresh,", "Right at Home! 🏡"],
    typeSpeed: 50,
    backSpeed: 30,
    backDelay: 1000,
    loop: true,
  });
});
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
.container{
    background-color: #F3F8F1; 
    display: flex;
    justify-content: center; /* Centers horizontally */
    align-items: center; /* Centers vertically */
    height: 100vh; /* Full viewport height */
    gap: 50px; /* Adds spacing between text and image */
}

.textfield{
    animation: fadeInUp 2s ease-out;
}

.imagefield {
    animation: fadeInRight 2s ease-out;
}

.textfield h1{
    font-family: "Poppins", serif;
    font-optical-sizing: auto;
    font-weight: Black (900);  /* Set to Black (900) */
    font-style: normal;
    font-size: 60px;
    margin-top: -170px;
    margin-left: 100px;
}

.textfield p{
    margin-left:100px ;
    margin-top: 30px;
    font-family: "Poppins", serif;
    font-optical-sizing: auto;
    font-weight: Black (100);  /* Set to Black (900) */
    font-style: normal;
    font-size: 20px;
}

.textfield button{
    margin-top: 25px;
    margin-left: 100px;
    padding: 15px;
    background-color: white;
    border:2px solid #86d345 ;
    border-radius: 10px;
    font-family: "Poppins", serif;
    font-optical-sizing: auto;
    font-weight: Black (100);
    font-size: 15px;
    cursor: pointer;
    transition: 500ms;
}

.textfield button:hover{
    transition: 500ms;
    background-color: #a9e22b;
}

.imagefield {
    display: flex;
    justify-content: center; /* Centers horizontally */
    align-items: center; /* Centers vertically */
    flex: 1; /* Takes equal space as textfield */
}

.imagefield img {
    height: 500px;
    width: 500px;
    object-fit: cover; /* Ensures the image fits well */
    border-radius: 50px;
}

</style>
