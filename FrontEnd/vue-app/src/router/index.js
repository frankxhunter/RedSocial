import Vue from 'vue'
import VueRouter from 'vue-router'
import UserVue from '@/components/user/User.vue'
import HomeVue from '@/components/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: HomeVue,
  },
  {
    path: '/user',
    component: UserVue,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
