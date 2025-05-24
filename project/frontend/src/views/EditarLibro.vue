<template>
  <div class="max-w-2xl mx-auto mt-8 p-6 bg-white rounded-xl shadow space-y-6">
    <h2 class="text-2xl font-bold text-primario text-center">✏️ Editar Libro</h2>

    <form @submit.prevent="guardarCambios" class="space-y-4">
      <!-- Título -->
      <div>
        <label class="block mb-1 font-medium text-gray-700">Título</label>
        <input
          v-model="titulo"
          required
          class="w-full px-4 py-2 border border-gray-300 rounded shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
        />
      </div>

      <!-- Género -->
      <div>
        <label class="block mb-1 font-medium text-gray-700">Género</label>
        <select
          v-model="generoSeleccionado"
          required
          class="w-full px-4 py-2 border border-gray-300 rounded shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
        >
          <option disabled value="">Selecciona un género</option>
          <option
            v-for="genero in generos"
            :key="genero.genero_id"
            :value="genero.genero_id"
          >
            {{ genero.nombre_genero }}
          </option>
        </select>
      </div>

      <!-- Botón -->
      <div class="text-right">
        <button
          type="submit"
          class="bg-primario text-white px-6 py-2 rounded-full text-sm font-bold uppercase shadow hover:bg-blue-800 transition-all"
        >
          Guardar Cambios
        </button>
      </div>
    </form>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import axios from '../api/axios'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const libro_id = route.params.id
const titulo = ref('')
const generoSeleccionado = ref('')
const generos = ref([])

onMounted(async () => {
  try {
    const [libroResp, generosResp] = await Promise.all([
        axios.get(`/libro?libro_id=${libro_id}`),
        axios.get('/generos')
    ])

    titulo.value = libroResp.data.titulo_libro
    generoSeleccionado.value = libroResp.data.genero_id
    generos.value = generosResp.data
  } catch {
    alert('Error al cargar datos del libro')
  }
})

const guardarCambios = async () => {
  try {
    await axios.put('/libro', {
      libro_id: libro_id,
      nuevo_titulo: titulo.value,
      nuevo_genero_id: generoSeleccionado.value
    })
    alert('Libro actualizado correctamente')
    router.push('/libros')
  } catch {
    alert('Error al actualizar libro')
  }
}
</script>
