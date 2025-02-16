<template>
    <div class="about-us">
        <div class="textSection">
            <h1 class="h1">Empowering Urban Dwellers to Grow 
                <span style="color:green">Fresh</span> Food Anytime, Anywhere!
            </h1>

            <!-- Mission and Vision Cards -->
            <div class="mission-vision">
                <div class="card mission">
                    <h2>🌱 Mission</h2>
                    <p>Empower urban dwellers to grow their own food in small spaces by providing smart, accessible, and sustainable urban farming solutions.</p>
                </div>
                <div class="card vision">
                    <h2>🌍 Vision</h2>
                    <p>A future where every city dweller has the knowledge, tools, and community support to cultivate fresh, healthy food right at home, fostering a greener and more self-sufficient world.</p>
                </div>
            </div>
        </div>

        <!-- What We Offer -->
        <section class="features">
            <h2 class="whatweoffer">What We Offer...</h2>
            <div class="feature-cards">
                <div class="card">
                    <img src="/src/assets/images/plantpic.png" alt="AI Plant Care">
                    <h3>AI-powered Plant Care</h3>
                    <p>Smart recommendations to keep your plants thriving.</p>
                </div>
                <div class="card">
                    <img src="/src/assets/images/photo1.jpeg" alt="Real-time Monitoring">
                    <h3>Real-time Monitoring</h3>
                    <p>Track plant health with IoT-ready features.</p>
                </div>
                <div class="card">
                    <img src="/src/assets/images/photo2.jpeg" alt="Community Market">
                    <h3>Community</h3>
                    <p>Discussion forum where users can share their experience.</p>
                </div>
                <div class="card">
                    <img src="/src/assets/images/photo3.jpeg" alt="Learning Hub">
                    <h3>Learning Hub</h3>
                    <p>Step-by-step guides for urban farming success.</p>
                </div>
            </div>
        </section>

        <!-- Meet the Team -->
        <section class="team">
            <h2>Meet the Team</h2>
            <div class="team-members">
                <div class="member" v-for="member in team" :key="member.name">
                    <img :src="member.image" :alt="member.name">
                    <h3>{{ member.name }}</h3>
                    <p>{{ member.role }}</p>
                </div>
            </div>
        </section>

        <!-- Call to Action -->
        <section class="cta">
            <h2>Join the Urban Farming Revolution!</h2>
            <p>Be a part of a growing community that supports smart and sustainable food production.</p>
            <router-link to="/register" class="cta-button">Get Started</router-link>
        </section>
    </div>
</template>

<script>
export default {
    data() {
        return {
            team: [
                { name: "Hari Prasath", role: "Backend Developer", image: "/src/assets/images/backgr.jpg" },
                { name: "Anuj", role: "Frontend Developer", image: "/src/assets/images/backgr.jpg" },
                { name: "Harinie ", role: "AI Specialist", image: "/src/assets/images/backgr.jpg" },
                { name: "Kissik", role: "UI/UX Designer", image: "/src/assets/images/backgr.jpg" }
            ]
        };
    }
};
</script>

<style scoped>
/* General Styles */
.whatweoffer{
    margin-bottom: 15px;
}
.about-us {
    font-family: "Poppins", sans-serif;
    color: #333;
    padding: 20px;
}

/* Heading */
.h1 {
    font-size: 35px;
    margin-top: 35px;
    text-align: center;
}

/* Mission & Vision Section */
.mission-vision {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin: 40px 0;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
    flex: 1;
    max-width: 400px;
    transition: transform 0.3s ease-in-out;
    background: #f4f4f4;
}

.card:hover {
    transform: scale(1.05);
}

.mission {
    border-top: 5px solid #4CAF50;
    background: #f4f4f4;
}

.vision {
    border-top: 5px solid #2E7D32;
    background: #f4f4f4;
}

/* Features Section */
.features {
    text-align: center;
    padding: 40px;
}

.feature-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    
}

.card img {
    width: 60px;
    margin-bottom: 10px;
}

/* Team Section */
.team {
    text-align: center;
    padding: 40px;
    background: #f4f4f4;
}

.team-members {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 25px;
}
.member{
    margin-right: 40px;
}

.member img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    object-fit: cover;
}

/* CTA Section */
.cta {
    text-align: center;
    padding: 40px;
}

.cta-button {
    display: inline-block;
    padding: 10px 20px;
    background: #218838;
    color: white;
    border-radius: 5px;
    text-decoration: none;
    transition: 0.3s;
    margin-top: 25px;
}

.cta-button:hover {
    background: #166534;
}

/* Responsive */
@media (max-width: 768px) {
    .mission-vision {
        flex-direction: column;
        align-items: center;
    }
}
</style>
