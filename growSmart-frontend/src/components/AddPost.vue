<template>
    <div class="backdrop" @click.self="closePopup">
      <div class="form-container">
        <h1>Add a New Post</h1>
        <div class="form">
          <form @submit.prevent="submitPost">
            <label class="titlelabel" for="title">Post Title:</label>
            <input type="text" id="title" v-model="title" placeholder="Enter title" required />
  
            <label class="contentlabel" for="content">Content:</label>
            <textarea id="content" v-model="content" placeholder="Write your post..." rows="4" required></textarea>
  
            <button type="submit">Post</button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        title: "",
        content: "",
        timestamp:"",
      };
    },
    methods: {
      closePopup() {
        this.$emit("close");
      },
      async submitPost() {
        if (!this.title || !this.content) {
            alert("Please fill in all fields!");
            return;
        }

        const formData = new FormData();
        formData.append("title", this.title);
        formData.append("content", this.content);
        formData.append("timestamp",new Date().toISOString().split("T")[0] + " " + new Date().toTimeString().split(" ")[0])




        try {
            const response = await fetch("http://127.0.0.1:5000/post", {
            method: "POST",
            body: formData
            });

            if (response.ok) {
                alert("Post added successfully!");
                this.closePopup();
                this.$emit("post-added")
            } else {
                alert(result.message); // Show error message if adding plant fails
            }
            
        } catch (error) {
            console.error("Error submitting post:", error);
            alert(error.message);
        }
}



    }
  };
  </script>
  
  <style scoped>
  /* Backdrop Overlay */
  .backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  /* Modal Box */
  .form-container {
    width: 500px;
    background: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  }
  
  .form-container h1 {
    font-size: 30px;
    font-family: "Poppins";
    font-weight: 700px;
  }
  
  .form {
    margin-top: 20px;
    text-align: left;
  }
  
  .titlelabel,
  .contentlabel {
    font-family: "Poppins";
  }
  
  /* Form Elements */
  input,
  textarea {
    width: 90%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 14px;
    font-family: "Poppins";
  }
  
  button {
    background: #28a745;
    color: white;
    border: none;
    padding: 10px;
    font-size: 18px;
    cursor: pointer;
    border-radius: 5px;
    transition: 0.3s;
  }
  
  button:hover {
    background: #218838;
  }
  </style>