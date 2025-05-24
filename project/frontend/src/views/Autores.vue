<template>
  <div>
<h2 class="text-2xl font-bold text-primario mb-4">Gestión de Autores</h2>

<form @submit.prevent="crearAutor" class="flex gap-4 mb-6">
  <input
    v-model="nuevoAutor"
    placeholder="Nuevo autor"
    required
    class="flex-1 px-4 py-2 border border-gray-300 rounded shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
  />
  <button
    type="submit"
    class="bg-primario text-white px-4 py-2 rounded-full text-sm font-bold uppercase shadow hover:bg-blue-800"
  >
    Agregar
  </button>
</form>


<ul class="space-y-3">
  <li
    v-for="autor in autores"
    :key="autor.autor_id"
    class="flex justify-between items-center bg-white shadow px-4 py-3 rounded hover:shadow-md transition-all"
  >
 
    <div v-if="editandoId !== autor.autor_id" class="text-left w-full">
      <span class="font-semibold text-gray-800">{{ autor.nombre_autor }}</span>
    </div>

  
    <div v-else class="w-full">
      <input
        v-model="nombreEditado"
        class="w-full px-3 py-1 border border-gray-300 rounded"
      />
    </div>


    <div class="flex gap-2 ml-4">
      <template v-if="editandoId !== autor.autor_id">
        <button @click="iniciarEdicion(autor)" class="text-blue-600 text-xl hover:text-blue-800">✏️</button>
        <button @click="eliminarAutor(autor.autor_id)" class="text-red-600 text-xl hover:text-red-800">🗑️</button>
      </template>
      <template v-else>
        <button @click="guardarEdicion(autor.autor_id)" class="text-green-600 text-xl hover:text-green-800">💾</button>
        <button @click="cancelarEdicion" class="text-gray-600 text-xl hover:text-gray-800">❌</button>
      </template>
    </div>
  </li>
</ul>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../api/axios'

const nuevoAutor = ref('')
const nombreEditado = ref('')
const editandoId = ref(null)
const autores = ref([])

const cargarAutores = async () => {
  try {
    const res = await axios.get('/autores')
    autores.value = res.data
  } catch {
    alert('Error al cargar autores')
  }
}

const crearAutor = async () => {
  try {
    await axios.post('/autor', { nombre_autor: nuevoAutor.value })
    nuevoAutor.value = ''
    cargarAutores()
  } catch {
    alert('Error al crear autor')
  }
}

const eliminarAutor = async (id) => {
  if (confirm('¿Eliminar autor?')) {
    try {
      await axios.delete('/autor', { data: { autor_id: id } })
      cargarAutores()
    } catch {
      alert('Error al eliminar autor')
    }
  }
}

const iniciarEdicion = (autor) => {
  editandoId.value = autor.autor_id
  nombreEditado.value = autor.nombre_autor
}

const cancelarEdicion = () => {
  editandoId.value = null
  nombreEditado.value = ''
}

const guardarEdicion = async (id) => {
  try {
    await axios.put('/autor', {
      autor_id: id,
      nuevo_nombre: nombreEditado.value
    })
    cancelarEdicion()
    cargarAutores()
  } catch {
    alert('Error al actualizar autor')
  }
}

onMounted(() => {
  cargarAutores()
})
</script>
