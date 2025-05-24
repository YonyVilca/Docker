<template>
  <div class="min-h-screen flex flex-col">
    <!-- Header -->
    <header class="bg-primario text-white p-4 flex justify-between items-center shadow">
      <h1 class="text-xl font-bold">Sistema de Libros</h1>
      <button
        class="bg-red-600 hover:bg-red-700 px-3 py-1 rounded"
        @click="logout"
      >
        Cerrar sesión
      </button>
    </header>

    <!-- Navigation -->
    <nav class="bg-gray-100 text-gray-700 px-4 py-2 flex gap-4">
      <router-link to="/libros" class="hover:underline">Libros</router-link>
      <router-link to="/autores" class="hover:underline">Autores</router-link>
      <router-link to="/generos" class="hover:underline">Géneros</router-link>
    </nav>

    <!-- Main content -->
    <main class="flex-1 bg-white p-6">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

const logout = () => {
  localStorage.removeItem('token')
  router.push('/login')
}
</script>
