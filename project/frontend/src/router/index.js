import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Libros from '../views/Libros.vue'
import AppLayout from '../layouts/AppLayout.vue'
import CrearLibro from '../views/CrearLibro.vue'
import Autores from '../views/Autores.vue'
import Generos from '../views/Generos.vue'
import EditarLibro from '../views/EditarLibro.vue'


const protectedRoutes = [
  { path: '/libros', component: Libros },
  { path: '/libros/nuevo', component: CrearLibro },
  { path: '/libros/editar/:id', component: EditarLibro },
  { path: '/autores', component: Autores },
    { path: '/generos', component: Generos }

]

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  {
    path: '/',
    component: AppLayout,
    children: protectedRoutes,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})


router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if (to.meta.requiresAuth && !token) {
    next('/login')
  } else {
    next()
  }
})

export default router
