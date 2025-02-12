<template>
  <Header />  
  <router-view></router-view>
</template>

<script>
import Header from './components/Header.vue';
import Landing from './components/Landing.vue'

export default{
  components:{
    Header,Landing
  },
}
</script>