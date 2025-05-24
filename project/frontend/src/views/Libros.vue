<template>
  <div>
<div class="flex items-center justify-between mb-6">
  <h2 class="text-2xl font-bold text-primario">Libros</h2>

  <router-link to="/libros/nuevo">
    <button
      class="bg-primario text-white px-4 py-2 rounded-full text-sm font-bold uppercase shadow hover:bg-blue-800 transition-all"
    >
      Nuevo Libro
    </button>
  </router-link>
</div>

<ul class="space-y-3">
  <li
    v-for="libro in libros"
    :key="libro.libro_id"
    class="flex justify-between items-center bg-white shadow px-4 py-2 rounded"
  >
    <span class="text-left">
      {{ libro.titulo_libro }} - {{ libro.nombre_genero }}
    </span>
    <div class="flex gap-2">
      <router-link :to="`/libros/editar/${libro.libro_id}`">
        <button class="hover:text-blue-600 text-xl">✏️</button>
      </router-link>
      <button
        @click="eliminarLibro(libro.libro_id)"
        class="hover:text-red-600 text-xl"
      >
        🗑️
      </button>
    </div>
  </li>
</ul>

  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import axios from '../api/axios'

const libros = ref([])

const cargarLibros = async () => {
  try {
    const response = await axios.get('/libros')
    libros.value = response.data
  } catch {
    alert('Error al cargar libros')
  }
}

const eliminarLibro = async (id) => {
  if (confirm('¿Seguro que deseas eliminar este libro?')) {
    try {
      await axios.delete('/libro', { data: { libro_id: id } })
      cargarLibros()
    } catch {
      alert('Error al eliminar libro')
    }
  }
}

onMounted(() => {
  cargarLibros()
})
</script>
