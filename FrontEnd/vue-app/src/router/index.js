import Vue from 'vue'
import VueRouter from 'vue-router'
import UserVue from '@/components/user/User.vue'
import HomeVue from '@/components/Home.vue'
import LoginView from '@/views/LoginView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: HomeVue,
  },
  {
    path: '/login',
    component: LoginView,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
