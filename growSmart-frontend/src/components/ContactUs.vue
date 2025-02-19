<template>
    <div class="mainone">
    <div class="contact-us">
        <!-- Header -->
        <h1 class="header">Get in Touch with Us! 🌱</h1>
        <p class="sub-header">Have questions or suggestions? We're here to help!</p>

        <!-- Contact Form -->
        <div class="contact-form">
            <form @submit.prevent="submitForm">
                <div class="input-group">
                    <label for="name">Name</label>
                    <input type="text" id="name" v-model="form.name" required placeholder="Enter your name">
                </div>

                <div class="input-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" v-model="form.email" required placeholder="Enter your email">
                </div>

                <div class="input-group">
                    <label for="subject">Subject</label>
                    <input type="text" id="subject" v-model="form.subject" required placeholder="Enter subject">
                </div>

                <div class="input-group">
                    <label for="message">Message</label>
                    <textarea id="message" v-model="form.message" required placeholder="Write your message here"></textarea>
                </div>

                <button type="submit" @click="submitForm" class="submit-btn  ">Send Message</button>
            </form>
        </div>

        <!-- Contact Info in Card -->
        
    </div>

    <div class="contact-card">
            <h2>📍 Contact Information</h2>
            <p><strong>Email:</strong> emailsfromapp@gmail.com</p>
            <p><strong>Phone:</strong> +91 6382072995 • +91 8074646289</p>
            <p><strong>Address:</strong> Coimbatore,Tamil Nadu</p>

            <!-- Social Media Links -->
            <div class="social-links">
                <a href="#"><img src="/src/assets/images/facebook.png" alt="Facebook"></a>
                <a href="#"><img src="/src/assets/images/twitter.png" alt="Twitter"></a>
                <a href="#"><img src="/src/assets/images/instagram.png" alt="Instagram"></a>
            </div>
    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            form: {
                name: '',
                email: '',
                subject: '',
                message: ''
            }
        };
    },
    methods: {
            async submitForm() {
                try {
                    let response = await fetch("http://127.0.0.1:5000/contact", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify(this.form),
                    });

                    let result = await response.json();
                    alert(result.success || result.error);
                } catch (error) {
                    alert("Failed to send message. Try again later.");
                }
            }

    }
};
</script>

<style scoped>
.contact-us {
    font-family: "Poppins", sans-serif;
    text-align: center;
    padding: 40px;
    max-width: 800px;
    margin: auto;
}

.header {
    font-size: 32px;
    margin-bottom: 10px;
}

.sub-header {
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
}

/* Contact Form */
.contact-form {
    background: #E8F5E9;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 40px;
}

.input-group {
    text-align: left;
    margin-bottom: 15px;
}

label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
}

textarea {
    height: 100px;
    resize: none;
}
#email,#name,#subject,#message{
    width: 700px;
}

.submit-btn {
    background: #218838;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
    transition: 0.3s;
}

.submit-btn:hover {
    background: #166534;
}

/* Contact Card */
.contact-card {
    background: #f4f4f4;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
    margin-top: 40px;
    text-align: center;
    font-family: "Poppins";

}

.contact-card h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

.contact-card p {
    font-size: 16px;
    color: #444;
    margin: 5px 0;
}

.social-links {
    margin-top: 15px;
}

.social-links a {
    margin: 0 10px;
}

.social-links img {
    width: 30px;
}
</style>
