<template>
  <div>
    <div class="feed-container">
      <div class="header-container">
        <h1 class="heading">Community for growSmart users :)</h1>
        <button type="button" class="buttonadd" @click="toggleAddPost">Add Post</button>
      </div>
      
      <!-- Popup AddPost Form (only visible when isOpen is true) -->
      <AddPostView v-if="isOpen" @close="toggleAddPost" @post-added="fetchPosts" />
      
      <!-- Posts Feed -->
      <div v-for="post in posts" :key="post.id" class="post-card">
        <h2>{{ post.title }}</h2>
        <p class="author">By {{ post.username }} • {{ formatDate(post.timestamp) }}</p>
        <p class="content">{{ post.content }}</p>
      </div>
    </div>
  </div>
</template>

  
  <script>
  import AddPostView from './AddPost.vue';
  
  export default {
    components: {
      AddPostView
    },
    data() {
      return {
        isOpen: false,
        posts: []
      };
    },
    methods: {
      formatDate(date) {
        return new Date(date).toDateString();
      },
      toggleAddPost() {
        this.isOpen = !this.isOpen;
      },
      async fetchPosts() {
        try {
            const response = await fetch("http://127.0.0.1:5000/posts", {
                method: "GET",
                credentials: "include", // Include session cookies
                headers: {
                    "Content-Type": "application/json"
                }
            });

            if (!response.ok) {
                throw new Error("Failed to fetch posts");
            }

            this.posts = await response.json(); // Store the posts in Vue state
        } catch (error) {
            console.error("Error fetching posts:", error);
        }
}



    },
    mounted() {
      this.fetchPosts();
    }
  };
  </script>
  
  <style scoped>
.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 25px;
  margin-bottom:30px;
}

.buttonadd {
  padding: 12px;
  background-color: #218838;
  border: 2px solid #218838;
  border-radius: 30px;
  font-family: "Poppins", serif;
  font-size: 15px;
  color:white;
  cursor: pointer;
  transition: 500ms;
}

.buttonadd:hover {
  background: #218838;
  transform: scale(1.05);
  transition: all 0.3s ease-in-out;
  color: white;
}

.heading {
  font-family: "Poppins", serif;
  font-size: 35px;
  font-weight: 700;
}

.feed-container {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.post-card {
  background: #fff;
  padding: 15px;
  margin: 10px 0;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  text-align: left;
  font-family: "Poppins", serif;
  font-size: 15px;
}

h2 {
  margin: 0;
  font-size: 20px;
}

.author {
  font-size: 14px;
  color: gray;
  margin-bottom: 8px;
}

.content {
  font-size: 16px;
}
</style>
