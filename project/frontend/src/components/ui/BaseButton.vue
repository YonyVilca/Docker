<template>
  <button
    :class="[
      'align-middle select-none font-sans font-bold text-center uppercase transition-all disabled:opacity-50 disabled:pointer-events-none text-xs py-3 px-6 rounded-full',
      tipo === 'primario'
        ? 'bg-primario text-white shadow-md shadow-primario/10 hover:shadow-lg hover:shadow-primario/20 focus:opacity-85 active:opacity-85'
        : tipo === 'secundario'
        ? 'bg-secundario text-white shadow-md hover:shadow-lg'
        : 'bg-gray-900 text-white shadow-md shadow-gray-900/10 hover:shadow-lg hover:shadow-gray-900/20',
      extraClases
    ]"
    :type="type"
    @click="$emit('click')"
  >
    <slot />
  </button>
</template>

<script setup>
defineProps({
  tipo: { type: String, default: 'primario' },
  type: { type: String, default: 'button' },
  extraClases: { type: String, default: '' }
})
</script>
