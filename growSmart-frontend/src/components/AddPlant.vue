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
                <h1>Add Plant 🌾</h1>
                <form @submit.prevent="handleSubmit">
                    <label class="name">Plant Name</label>
                    <input class="firstname" type="text" required v-model="name" placeholder="Carrot" id="firstname">
                    
                    <label class="password">Temperature</label>
                    <input class="passwordfield" type="text" required v-model="soilMoisture" placeholder="Testing purpose only" id="password">
                    
                    <label class="password">Humidity Content</label>
                    <input class="passwordfield" type="text" required v-model="humidityContent" placeholder="Testing purpose only" id="password">

                    <!-- Inside your form, add an input for image upload -->
                    <label class="password">Plant Image</label>
                    <input class="imageupload" type="file" @change="handleImageUpload" accept="image/*" />

                    <button type="submit" class="register-btn">Add</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import image1 from '/src/assets/images/plantpic.png'
import image2 from '/src/assets/images/photo1.jpeg'
import image3 from '/src/assets/images/photo2.jpeg'
import image4 from '/src/assets/images/photo3.jpeg'

export default {
    data() {
        return {
            images: [image1, image2, image3, image4],
            currentIndex: 0,
            name: "",
            soilMoisture: "",
            humidityContent: "",
            userId: 9,  // Replace with the actual user ID, can be fetched from user authentication
            selectedImage: null, // This will hold the selected image file
            scientificName: "", // To store the scientific name of the plant
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
        handleImageUpload(event) {
            this.selectedImage = event.target.files[0]; // Store the selected image file
        },
        async identifyPlant() {
            if (this.selectedImage) {
                const formData = new FormData();
                formData.append('image', this.selectedImage); // Attach image file

                try {
                    const response = await fetch("http://127.0.0.1:5000/identify-plant", {
                        method: "POST",
                        body: formData, // Send image as FormData
                    });

                    const result = await response.json();
                    if (response.ok && result.scientific_name) {
                        this.scientificName = result.scientific_name; // Extract scientific name from response
                        sessionStorage.setItem('scientificName', this.scientificName);  // Store it in sessionStorage
                    } else {
                        alert('Plant not identified');
                    }

                } catch (error) {
                    console.error('Error identifying plant:', error);
                    alert('Error identifying plant');
                }
            }
        },
        async handleSubmit() {
            await this.identifyPlant(); // Call the identifyPlant method to get the scientific name first

            // If scientific name was retrieved, submit the form
            if (this.scientificName) {
                const formData = new FormData();
                formData.append('name', this.name);
                formData.append('startDate', new Date().toUTCString().split(' ')[0] + ' ' + new Date().toUTCString().split(' ')[1] + ' ' + new Date().toUTCString().split(' ')[2] + ' ' + new Date().toUTCString().split(' ')[3]); // Current date
                formData.append('soilMoisture', this.soilMoisture);
                formData.append('humidityContent', this.humidityContent);
                formData.append('userId', this.userId);
                formData.append('scientificName', this.scientificName);

                if (this.selectedImage) {
                    formData.append('image', this.selectedImage); // Attach image file
                }


                try {
                    const response = await fetch("http://127.0.0.1:5000/add_plant", {
                        method: "POST",
                        body: formData, // Use FormData for sending file along with other fields
                    });

                    const result = await response.json();
                    if (response.ok) {
                        alert("Plant added successfully!");
                        this.$router.push({ name: "PlantDashboard" });
                        this.resetForm(); // Optionally reset the form after submission
                    } else {
                        alert(result.message); // Show error message if adding plant fails
                    }

                } catch (error) {
                    console.error("Error submitting form:", error);
                }
            } else {
                alert('Please upload a valid plant image.');
            }
        },
    },
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
    margin-bottom: 15px;
}

.firstname {
    padding: 10px 15px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 10px;
}

.firstname {
    margin-right: 10px;
    width: 350px;
}

.emailfield, .passwordfield {
    padding: 10px 15px;
    font-size: 16px;
    width: 350px;
    border: 1px solid #ccc;
    border-radius: 8px;
    transition: border 0.3s ease-in-out;
    margin-bottom: 5px;
    display: block;
    margin-bottom: 20px;

}

.imageupload{
    padding: 10px 15px;
    font-size: 16px;
    width: 350px;
    display: block;
}

.register-btn {
    width: 100px;
    padding: 8px;
    font-size: 16px;
    margin-top: 20px;
    color: black;
    border: gray 1px solid;
    border-radius: 8px;
    cursor: pointer;
    transition: 0.3s ease-in-out;
    background: white;
    margin-right: 30px;
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