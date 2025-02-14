<template>
    <p>Good morning, {{ this.firstName }} 🌞 Your plants are thriving! Here’s today’s care schedule.</p>
</template>

<script>
export default {
    props: ["firstName"], // Receive firstName from login
    mounted() {
        console.log("User Name:", this.firstName);
    }
};

</script>

<style scoped>
</style>
