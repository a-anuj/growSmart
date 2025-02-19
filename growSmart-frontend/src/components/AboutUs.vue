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
                    <img src="/src/assets/images/AI-POWERED PLANT.jpeg" alt="AI Plant Care">
                    <h3>AI-powered Plant Care</h3>
                    <p>Smart recommendations to keep your plants thriving.</p>
                </div>
                <div class="card">
                    <img src="/src/assets/images/Real-Time Montioring1.jpeg" alt="Real-time Monitoring">
                    <h3>Real-time Monitoring</h3>
                    <p>Track plant health with IoT-ready features.</p>
                </div>
                <div class="card">
                    <img src="/src/assets/images/Community_cleanup 2.png" alt="Community Market">
                    <h3>Community</h3>
                    <p>Discussion forum where users can share their experience.</p>
                </div>
                <div class="card">
                    <img src="/src/assets/images/learningh.jpeg" alt="Learning Hub">
                    <h3>Learning Hub</h3>
                    <p>Step-by-step guides for urban farming success.</p>
                </div>
            </div>
        </section>

        <!-- Reviews Section -->
        <section class="reviews-section">
            <h2>User Reviews</h2>
            <div class="reviews-container">
                <div class="review-card">
                    <img src="/src/assets/images/male.png" class="avatar" />
                    <h3>Roshan</h3>
                    <p class="location">Kochin, Kerala</p>
                    <p class="stars">⭐️⭐️⭐️⭐️⭐️</p>
                    <p class="review-text">"Amazing app! My home garden has never been healthier!"</p>
                </div>
                <div class="review-card">
                    <img src="/src/assets/images/female.jpg" class="avatar" />
                    <h3>Anjali</h3>
                    <p class="location">Ramabadhrapuram, Andhra Pradesh</p>
                    <p class="stars">⭐️⭐️⭐️⭐️⭐️</p>
                    <p class="review-text">"Super easy to use and very informative!"</p>
                </div>
                <div class="review-card">
                    <img src="/src/assets/images/male.png" class="avatar" />
                    <h3>Sanjay Kumaran</h3>
                    <p class="location">Madurai, Tamil Nadu</p>
                    <p class="stars">⭐️⭐️⭐️⭐️⭐️</p>
                    <p class="review-text">"A must-have for urban dwellers who love gardening."</p>
                </div>
            </div>
        </section>

        <!-- Meet the Team -->
        <section class="team">
            <h2>Meet the Team</h2>
            <div class="team-members">
                <div class="member">
                    <img src="/src/assets/images/hariphoto.jpeg" alt="Hari Prasath">
                    <h3>Hari Prasath</h3>
                    <p>Backend Developer</p>
                </div>
                <div class="member">
                    <img src="/src/assets/images/anujphoto.jpeg" alt="Anuj">
                    <h3>Anuj</h3>
                    <p>Frontend Developer</p>
                </div>
                <div class="member">
                    <img src="/src/assets/images/hariniephoto.jpeg" alt="Harinie">
                    <h3>Harinie</h3>
                    <p>AI Specialist</p>
                </div>
                <div class="member">
                    <img src="/src/assets/images/karthikphoto.jpeg" alt="Siva Sai Karthik">
                    <h3>Siva Sai Karthik</h3>
                    <p>UI/UX Designer</p>
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
        return {};
    }
};
</script>

<style scoped>
/* General Styles */
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
}

.vision {
    border-top: 5px solid #2E7D32;
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
    width: 70px;
    margin-bottom: 10px;
    border-radius: 10%;
}

/* Reviews Section */
.reviews-section {
    background-color: #f3f8f1;
    padding: 50px 20px;
    text-align: center;
}

.reviews-section h2 {
    font-size: 32px;
    font-family: "Poppins", serif;
    font-weight: 700;
    color: #333;
    margin-bottom: 20px;
}

.reviews-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
}

.review-card {
    background: white;
    border-radius: 15px;
    padding: 20px;
    max-width: 300px;
    text-align: center;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
}

.review-card:hover {
    transform: translateY(-5px);
}

.avatar {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 10px;
}

.review-card h3 {
    font-size: 20px;
    font-weight: 600;
    color: #333;
}

.location {
    font-size: 14px;
    color: #777;
    margin-bottom: 10px;
}

.stars {
    font-size: 18px;
    color: #f4c150;
    margin-bottom: 10px;
}

.review-text {
    font-size: 16px;
    color: #555;
    font-style: italic;
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
    flex-wrap: wrap;
    gap: 20px;
    margin-top: 20px;
}

.member {
    background: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    max-width: 200px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
}

.member:hover {
    transform: scale(1.05);
}

.member img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 10px;
}

.member h3 {
    font-size: 18px;
    color: #333;
    margin: 5px 0;
}

.member p {
    font-size: 14px;
    color: #777;
}

/* Responsive */
@media (max-width: 768px) {
    .team-members {
        flex-direction: column;
        align-items: center;
    }
}

/* Call to Action Section */
.cta {
    text-align: center;
    background: #E8F5E9; /* Green background */
    color: black;
    padding: 50px 20px;
    border-radius: 10px;
    margin: 40px auto;
    max-width: 800px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
}

.cta:hover {
    transform: scale(1.05);
}

.cta h2 {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 10px;
}

.cta p {
    font-size: 18px;
    margin-bottom: 20px;
}

.cta-button {
    display: inline-block;
    background: white;
    color: #4CAF50;
    padding: 12px 24px;
    font-size: 18px;
    font-weight: bold;
    text-decoration: none;
    border-radius: 5px;
    transition: background 0.3s, transform 0.2s;
}

.cta-button:hover {
    background: #f4f4f4;
    transform: translateY(-3px);
}

/* Responsive */
@media (max-width: 768px) {
    .cta {
        padding: 30px 15px;
    }
    
    .cta h2 {
        font-size: 24px;
    }

    .cta p {
        font-size: 16px;
    }

    .cta-button {
        font-size: 16px;
        padding: 10px 20px;
    }
}
</style>
