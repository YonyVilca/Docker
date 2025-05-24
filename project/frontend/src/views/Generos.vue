<template>
  <div>
<h2 class="text-2xl font-bold text-primario mb-4">Gestión de Géneros</h2>

<form @submit.prevent="crearGenero" class="flex gap-4 mb-6">
  <input
    v-model="nuevoGenero"
    placeholder="Nuevo género"
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
    v-for="genero in generos"
    :key="genero.genero_id"
    class="flex justify-between items-center bg-white shadow px-4 py-3 rounded hover:shadow-md transition-all"
  >
    <!-- Modo lectura -->
    <div v-if="editandoId !== genero.genero_id" class="text-left w-full">
      <span class="font-semibold text-gray-800">{{ genero.nombre_genero }}</span>
    </div>

    <!-- Modo edición -->
    <div v-else class="w-full">
      <input
        v-model="nombreEditado"
        class="w-full px-3 py-1 border border-gray-300 rounded"
      />
    </div>

    <!-- Acciones -->
    <div class="flex gap-2 ml-4">
      <template v-if="editandoId !== genero.genero_id">
        <button @click="iniciarEdicion(genero)" class="text-blue-600 text-xl hover:text-blue-800">✏️</button>
        <button @click="eliminarGenero(genero.genero_id)" class="text-red-600 text-xl hover:text-red-800">🗑️</button>
      </template>
      <template v-else>
        <button @click="guardarEdicion(genero.genero_id)" class="text-green-600 text-xl hover:text-green-800">💾</button>
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

const nuevoGenero = ref('')
const nombreEditado = ref('')
const editandoId = ref(null)
const generos = ref([])

const cargarGeneros = async () => {
  try {
    const res = await axios.get('/generos')
    generos.value = res.data
  } catch {
    alert('Error al cargar géneros')
  }
}

const crearGenero = async () => {
  try {
    await axios.post('/genero', { nombre_genero: nuevoGenero.value })
    nuevoGenero.value = ''
    cargarGeneros()
  } catch {
    alert('Error al crear género')
  }
}

const eliminarGenero = async (id) => {
  if (confirm('¿Eliminar género?')) {
    try {
      await axios.delete('/genero', { data: { genero_id: id } })
      cargarGeneros()
    } catch {
      alert('Error al eliminar género')
    }
  }
}

const iniciarEdicion = (genero) => {
  editandoId.value = genero.genero_id
  nombreEditado.value = genero.nombre_genero
}

const cancelarEdicion = () => {
  editandoId.value = null
  nombreEditado.value = ''
}

const guardarEdicion = async (id) => {
  try {
    await axios.put('/genero', {
      genero_id: id,
      nuevo_nombre: nombreEditado.value
    })
    cancelarEdicion()
    cargarGeneros()
  } catch {
    alert('Error al actualizar género')
  }
}

onMounted(() => {
  cargarGeneros()
})
</script>
