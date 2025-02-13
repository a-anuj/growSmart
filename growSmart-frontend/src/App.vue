<template>
  <div>
      <Header />  
    <router-view></router-view>
  </div>
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