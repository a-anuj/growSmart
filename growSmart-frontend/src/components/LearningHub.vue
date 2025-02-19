<template>
    <div class="learning-hub">
        <h1>📚 Learning Hub</h1>
        <p>Explore a variety of urban farming tutorials and tips.</p>

        <div class="videos-container">
            <div class="video-card" @click="openVideo('https://www.youtube.com/watch?v=o_RZhQVN1s4')">
                <img src="/src/assets/images/uf.jpeg" alt="Urban Farming">
                <h3>Urban Farming</h3>
            </div>
            <div class="video-card" @click="openVideo('https://www.youtube.com/watch?v=tWgDqBryR30')">
                <img src="/src/assets/images/hp.jpg" alt="Hydroponics for Beginners">
                <h3>Hydroponics for Beginners</h3>
            </div>
            <div class="video-card" @click="openVideo('https://www.youtube.com/watch?v=ANLKNoZ_b4c')">
                <img src="/src/assets/images/sg.jpeg" alt="Smart Gardening Tips">
                <h3>Smart Gardening Tips</h3>
            </div>
            <div class="video-card" @click="openVideo('https://www.youtube.com/watch?v=egyNJ7xPyoQ')">
                <img src="/src/assets/images/cp.jpg" alt="Composting Basics">
                <h3>Composting Basics</h3>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    methods: {
        openVideo(link) {
            window.open(link, "_blank");
        }
    }
};
</script>

<style scoped>
.learning-hub {
    text-align: center;
    padding: 40px;
    font-family: "Poppins", sans-serif;
}

h1 {
    font-size: 32px;
    color: #4CAF50;
    margin-bottom: 10px;
}

p {
    font-size: 18px;
    color: #666;
    margin-bottom: 20px;
}

.videos-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    justify-items: center;
    max-width: 1200px;
    margin: 0 auto;
}

.video-card {
    background: white;
    border-radius: 10px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    padding: 15px;
    max-width: 250px;
    text-align: center;
    transition: transform 0.3s ease;
    cursor: pointer;
}

.video-card:hover {
    transform: scale(1.05);
}

.video-card img {
    width: 100%;
    border-radius: 10px;
    margin-bottom: 10px;
}

h3 {
    font-size: 18px;
    color: #333;
}

/* Responsive */
@media (max-width: 1024px) {
    .videos-container {
        grid-template-columns: repeat(2, minmax(250px, 1fr));
    }
}

@media (max-width: 768px) {
    .videos-container {
        grid-template-columns: repeat(1, minmax(250px, 1fr));
    }
}
</style>
