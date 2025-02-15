<template>
  <div>
      <Header />  
      
    <router-view></router-view>
  </div>
</template>

<script>
import Header from './components/Header.vue';
import Landing from './components/Landing.vue';
import PlantDashboard from './components/PlantDashboard.vue';
import Community from './components/Community.vue';


export default{
  components:{
    Header,Landing,PlantDashboard,Community
  },
}
</script>