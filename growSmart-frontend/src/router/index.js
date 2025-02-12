import { createRouter, createWebHistory } from 'vue-router';
import RegisterView from '/home/anuj/Desktop/THIRAN/growSmart/growSmart-frontend/src/components/Register.vue'
import LandingView from '/src/components/Landing.vue'

const routes = [
    {
        path:'/',
        name:'home',
        component:LandingView
    },
    {
        path:'/register',
        name:'register',
        component:RegisterView
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
  })
  
  export default router