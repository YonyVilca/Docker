<template>
  <div class="max-w-2xl mx-auto mt-8 p-6 bg-white rounded shadow space-y-6">
    <h2 class="text-2xl font-bold text-primario">Nuevo Libro</h2>

    <form @submit.prevent="crearLibro" class="space-y-4">
   
      <BaseInput
        v-model="titulo"
        label="Título del libro"
        placeholder="Ej: Cien años de soledad"
      />

  
      <BaseSelect
        v-model="generoSeleccionado"
        :opciones="generos"
        claveId="genero_id"
        claveTexto="nombre_genero"
        label="Género"
        placeholder="Selecciona un género"
      />

    
      <BaseCheckboxGroup
        v-model="autoresSeleccionados"
        :opciones="autores"
        claveId="autor_id"
        claveTexto="nombre_autor"
        label="Autores"
      />


      <BaseButton type="submit">Guardar Libro</BaseButton>
      
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../api/axios'
import { useRouter } from 'vue-router'


import BaseInput from '@/components/ui/BaseInput.vue'
import BaseSelect from '@/components/ui/BaseSelect.vue'
import BaseCheckboxGroup from '@/components/ui/BaseCheckboxGroup.vue'
import BaseButton from '@/components/ui/BaseButton.vue'


const titulo = ref('')
const generoSeleccionado = ref('')
const autoresSeleccionados = ref([])

const generos = ref([])
const autores = ref([])

const router = useRouter()

onMounted(async () => {
  try {
    const [respGeneros, respAutores] = await Promise.all([
      axios.get('/generos'),
      axios.get('/autores')
    ])
    generos.value = respGeneros.data
    autores.value = respAutores.data
  } catch (e) {
    alert('Error al cargar autores o géneros')
  }
})

const crearLibro = async () => {
  try {
    await axios.post('/libro', {
      titulo_libro: titulo.value,
      genero_id: generoSeleccionado.value,
      autor_ids: autoresSeleccionados.value
    })
    alert('Libro creado exitosamente')
    router.push('/libros')
  } catch (e) {
    alert('Error al crear libro')
  }
}
</script>
