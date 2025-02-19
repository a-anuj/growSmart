<template>
  <div> 
    <div v-if="loading" class="loader-container">
      <div class="loader">🌱🌲🌾</div>
    </div>

    <div v-else class="container">
      <div class="textfield">
        <h1><span ref="typedText" class="text-green-600"></span></h1>
        <p>
          AI-powered gardening made effortless for urban dwellers.<br />
          Get real-time insights, personalized guidance, and grow fresh,<br />
          organic produce right from your home—no experience needed!
        </p>
        <router-link to="/register">
          <button>Start Growing</button>
        </router-link>
      </div>
      <div class="imagefield">
        <div class="img">
          <img src="/finalgif.gif" />
        </div>
      </div>
    </div>

    
  </div>
</template>

<script setup>
import { onMounted, ref, nextTick } from "vue";
import Typed from "typed.js";

const typedText = ref(null);
const loading = ref(true);



onMounted(() => {
  setTimeout(async () => {
    loading.value = false;
    await nextTick();
    new Typed(typedText.value, {
      strings: ["Harvest Fresh,", "Right at Home! 🏡"],
      typeSpeed: 50,
      backSpeed: 30,
      backDelay: 1000,
      loop: true,
    });
  }, 2000);
});
</script>
  
  <style scoped>
  /* LOADER STYLES */
  .loader-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #F3F8F1;
  }
  
  .loader {
    font-size: 30px;
    font-weight: bold;
    color: #86d345;
    animation: growFade 2s ease-in-out infinite;
  }
  
  @keyframes growFade {
    0% { transform: scale(0.8); opacity: 0.5; }
    50% { transform: scale(1.2); opacity: 1; }
    100% { transform: scale(0.8); opacity: 0.5; }
  }
  
  /* EXISTING PAGE STYLES */
  @keyframes fadeInUp {
    from { opacity: 0; transform: translateY(50px); }
    to { opacity: 1; transform: translateY(0); }
  }
  
  @keyframes fadeInRight {
    from { opacity: 0; transform: translateX(50px); }
    to { opacity: 1; transform: translateX(0); }
  }
  
  .container {
    background-color: #F3F8F1; 
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    gap: 50px;
  }
  
  .textfield {
    animation: fadeInUp 2s ease-out;
  }
  
  .imagefield {
    animation: fadeInRight 2s ease-out;
  }
  
  .textfield h1 {
    font-family: "Poppins", serif;
    font-weight: 900;
    font-size: 60px;
    margin-top: -170px;
    margin-left: 100px;
  }
  
  .textfield p {
    margin-left: 100px;
    margin-top: 30px;
    font-family: "Poppins", serif;
    font-size: 20px;
  }
  
  .textfield button {
    margin-top: 25px;
    margin-left: 100px;
    padding: 15px;
    background-color: white;
    border: 2px solid #86d345;
    border-radius: 10px;
    font-family: "Poppins", serif;
    font-size: 15px;
    cursor: pointer;
    transition: 500ms;
  }
  
  .textfield button:hover {
    background-color: #a9e22b;
  }
  
  .imagefield {
    display: flex;
    justify-content: center;
    align-items: center;
    flex: 1;
  }
  
  .imagefield img {
    height: 500px;
    width: 500px;
    object-fit: cover;
    border-radius: 50px;
  }



</style>

  