import Vue from 'vue'
import VueRouter from 'vue-router'
import UserVue from '@/components/user/User.vue'
import HomeVue from '@/components/Home.vue'
import RegisterVue from '@/views/RegisterVue.vue'
import HelloWorldVue from '@/components/HelloWorld.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: HomeVue,
  },
  {
    path: '/register',
    component: RegisterVue,
  },
  {
    path: `/user`,
    component: UserVue
  },
  {
    path: '/hello',
    component: HelloWorldVue,
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
