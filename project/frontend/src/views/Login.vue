<template>
  <div class="h-screen flex items-center justify-center bg-grisclaro px-4">
    <div class="bg-white w-full max-w-sm p-6 rounded-lg shadow-lg space-y-6">
      <h2 class="text-center text-2xl font-bold text-primario">Iniciar Sesión</h2>

      <form @submit.prevent="login" class="space-y-4">
        <BaseInput
          v-model="username"
          label="Usuario"
          placeholder="ej: admin"
        />

        <BaseInput
          v-model="password"
          label="Contraseña"
          type="password"
          placeholder="********"
        />

<BaseButton tipo="primario" type="submit" class="w-full">Ingresar</BaseButton>

      </form>

      <p v-if="error" class="text-red-600 text-center text-sm">{{ error }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from '../api/axios'

import BaseInput from '@/components/ui/BaseInput.vue'
import BaseButton from '@/components/ui/BaseButton.vue'

const username = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()

const login = async () => {
  error.value = ''
  try {
    const res = await axios.post('/login', {
      username: username.value,
      password: password.value
    })
    localStorage.setItem('token', res.data.access_token)
    router.push('/libros')
  } catch {
    error.value = 'Credenciales inválidas'
  }
}
</script>
