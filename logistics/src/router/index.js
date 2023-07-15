import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'
import Data from '../views/DataView.vue'
import About from '../views/AboutView.vue'
import Analitics from '../views/AnaliticsView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/data',
    name: 'Data',
    component: Data,
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
  {
    path: '/analytics',
    name: 'Analitics',
    component: Analitics,
  }
]
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
export default router