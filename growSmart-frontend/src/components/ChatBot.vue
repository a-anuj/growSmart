<template>
    <div class="chat-container">
      <div class="chat-box">
        <div v-for="(message, index) in messages" :key="index" :class="['message', message.from]">
          <p>{{ message.text }}</p>
        </div>
      </div>
      
      <div class="input-area">
        <input 
          v-model="userMessage" 
          @keyup.enter="sendMessage"
          type="text" 
          placeholder="Type a message..." 
          :disabled="loading" 
          class="message-input"
        />
        <button @click="sendMessage" :disabled="loading" class="send-button">
          Send
        </button>
      </div>
      
      <div v-if="loading" class="loading-indicator">
        <span>...</span> <!-- Simple loading indicator -->
      </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
data() {
    return {
    userMessage: '',
    messages: [],
    loading: false,
    };
},
methods: {
    async sendMessage() {
    if (this.userMessage.trim() === '') return;

    // Add user message to the chat
    this.messages.push({ text: this.userMessage, from: 'user' });

    // Show loading indicator
    this.loading = true;

    try {
        const sessionId = localStorage.getItem('sessionId') || this.generateSessionId();
        if (!localStorage.getItem('sessionId')) {
        localStorage.setItem('sessionId', sessionId);
        }

        // Send message to the backend (Flask API)
        const response = await axios.post('http://localhost:5000/dialogflow-query', {
        sessionId: sessionId,
        text: this.userMessage,
        });

        // Add bot's reply to the chat
        this.messages.push({ text: response.data.fulfillmentText, from: 'bot' });
    } catch (error) {
        console.error('Error communicating with Dialogflow:', error);
        this.messages.push({ text: 'Sorry, something went wrong. Please try again.', from: 'bot' });
    } finally {
        this.loading = false;
    }

    // Clear the input field
    this.userMessage = '';
    },
    
    generateSessionId() {
    return 'session-' + Date.now(); // Generates a session ID based on current time
    },
},
};
</script>

<style scoped>
.chat-container {
width: 100%;
max-width: 500px;
margin-top: 100px;
margin-left: 550px;
background-color: #ffffff;
border-radius: 10px;
padding: 20px;
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
font-family: 'Arial', sans-serif;
}

.chat-box {
max-height: 350px;
overflow-y: auto;
margin-bottom: 20px;
padding-right: 10px;
}

.message {
margin-bottom: 15px;
padding: 10px;
border-radius: 12px;
max-width: 80%;
}

.message.user {
background-color: #d4f8e8;
text-align: right;
margin-left: auto;
}

.message.bot {
background-color: #f1f1f1;
text-align: left;
margin-right: auto;
}

.input-area {
display: flex;
gap: 10px;
}

.message-input {
flex-grow: 1;
padding: 10px;
font-size: 16px;
border: 1px solid #ddd;
border-radius: 8px;
outline: none;
transition: all 0.3s ease;
}

.message-input:focus {
border-color: #4CAF50;
}

.send-button {
background-color: #4CAF50;
color: white;
padding: 10px 16px;
border: none;
border-radius: 8px;
cursor: pointer;
font-size: 16px;
transition: all 0.3s ease;
}

.send-button:disabled {
background-color: #ccc;
cursor: not-allowed;
}

.send-button:hover:not(:disabled) {
background-color: #45a049;
}

.loading-indicator {
text-align: center;
font-size: 18px;
color: #888;
margin-top: 15px;
}
</style>
