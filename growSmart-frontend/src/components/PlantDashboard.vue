<template>
    <div>
        <h1>{{ greeting }}, {{ firstName }} 🌞 Your plants are thriving! Here are your heroes...</h1>
        <button @click="handleLogout">Log Out</button>
    </div>
</template>

<script>
export default {
    data(){
        return{
            greeting: new Date().getHours() < 12 ? "Good Morning" : 
                      new Date().getHours() < 18 ? "Good Afternoon" : 
                      "Good Evening"
        }
    },
    props: ["firstName"], // Receive firstName from login
    mounted() {
        console.log("User Name:", this.firstName);

    },

    methods:{
        handleLogout(){
            this.$router.push({name:'login'})
        }
    }
};

</script>

<style scoped>
</style>
