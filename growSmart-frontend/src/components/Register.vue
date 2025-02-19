<template>
    <div class="background-overlay">
        <div class="container">
            <!-- Slideshow Container -->
            <div class="imagefield">
                <div class="slideshow">
                    <transition name="slide-fade" mode="out-in">
                        <img :src="currentImage" :key="currentIndex" alt="image_plant" class="slide" />
                    </transition>
                </div>            
            </div>
            
            <!-- Registration Form -->
            <div class="formfield">
                <h1>Register Here 📝</h1>
                <form @submit.prevent="handleSubmit">
                    <label class="name">Name</label>
                    <input class="firstname" type="text" required v-model="firstName" placeholder="Hari" id="firstname">
                    <input class="secondname" type="text" required v-model="lastName" placeholder="Prasath" id="secondname">
                    <label class="email">Email</label>
                    <input class="emailfield" type="text" required v-model="email" placeholder="abc@gmail.com" id="email">
                    <label class="password">Password</label>
                    <input class="passwordfield" type="password" required v-model="password" placeholder="*****" id="password">
                        <button type="submit" class="register-btn">Register</button>
                    
                <router-link to="/login">
                    <p class="already">Already have an account?</p>
                </router-link>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
  import image1 from '/src/assets/images/sg.jpeg';
  import image2 from '/src/assets/images/hp.jpg';
  import image3 from '/src/assets/images/Real-Time Montioring1.jpeg';
  import image4 from '/src/assets/images/uf.jpeg';

export default {
    data() {
        return {
            images: [image1, image2, image3, image4],
            currentIndex: 0,
            firstName: "",
            lastName: "",
            email: "",
            password: "",
        };
    },
    computed: {
        currentImage() {
            return this.images[this.currentIndex];
        }
    },
    mounted() {
        setInterval(this.nextImage, 3000); // Change image every 3 seconds
    },
    methods: {
        nextImage() {
            this.currentIndex = (this.currentIndex + 1) % this.images.length;
        },
        async handleSubmit() {
    const formData = {
        firstName: this.firstName,
        lastName: this.lastName,
        email: this.email,
        password: this.password,
    };

    try {
        const response = await fetch("http://127.0.0.1:5000/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(formData),
        });

        const result = await response.json();
        console.log(result.message); // Debugging message

        if (response.ok) {
            alert("Registration successful! Redirecting to login...");
            this.$router.push("/login"); // Redirect to login page
        } else {
            alert(result.message); // Show error message if registration fails
        }

    } catch (error) {
        console.error("Error submitting form:", error);
        alert("Something went wrong. Please try again.");
    }
}

    }
};
</script>

<style scoped>

.container {
    display: flex;
    margin-left: 16%;
    margin-top: 80px;
    max-width: 1000px;
    height: 500px;
    padding: 20px;
    font-family: "Poppins", sans-serif;
    font-weight: 400;
    background: #E8F5E9;
    backdrop-filter: blur(20px);
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
}

/* Slideshow */
.imagefield {
    flex-basis: 45%;
}

.slideshow {
    position: relative;
    width: 390px;
    height: auto;
    overflow: hidden;
    border-radius: 10px;
}

.slide {
    width: 100%;
    border-radius: 10px;
}

/* Smooth right-to-left scrolling animation */
.slide-fade-enter-active, .slide-fade-leave-active {
    transition: transform 1s ease-in-out, opacity 1s ease-in-out;
}

.slide-fade-enter-from {
    transform: translateX(100%);
    opacity: 0;
}

.slide-fade-leave-to {
    transform: translateX(-100%);
    opacity: 0;
}

/* Form Styling */
.formfield {
    flex-basis: 50%;
    padding-left: 10px;
    padding-top: 30px;
}

.formfield form .name {
    display: block;
}

.formfield form .email {
    display: block;
    margin-top: 10px;
}

.formfield form .password {
    display: block;
    margin-top: 10px;
}

.formfield h1 {
    margin-bottom: 35px;
}

.firstname, .secondname {
    padding: 10px 15px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 10px;
}

.firstname {
    margin-right: 10px;
    width: 130px;
}

.emailfield, .passwordfield {
    padding: 10px 15px;
    font-size: 16px;
    width: 350px;
    border: 1px solid #ccc;
    border-radius: 8px;
    transition: border 0.3s ease-in-out;
    margin-bottom: 5px;
}

.register-btn {
    width: 100px;
    padding: 10px;
    font-size: 16px;
    margin-top: 20px;
    margin-left: 25%;
    color: black;
    border: gray 1px solid;
    border-radius: 8px;
    cursor: pointer;
    transition: 0.3s ease-in-out;
    background: white;
}

.register-btn:hover {
    background-color: #218838;
    color: white;
}

.already {
    color: blue;
    text-decoration: underline;
    margin-left: 90px;
    margin-top: 10px;
    font-size: 13px;
}

</style>