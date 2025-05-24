<template>
  <div class="mb-4">
    <label v-if="label" class="block mb-1 font-medium text-gray-700">{{ label }}</label>
    <select
      :value="modelValue"
      @change="$emit('update:modelValue', $event.target.value)"
      class="w-full px-3 py-2 border rounded shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-300"
    >
      <option disabled value="">{{ placeholder }}</option>
      <option v-for="item in opciones" :key="item[claveId]" :value="item[claveId]">
        {{ item[claveTexto] }}
      </option>
    </select>
  </div>
</template>

<script setup>
defineProps({
  modelValue: [String, Number],
  label: String,
  placeholder: { type: String, default: 'Selecciona una opción' },
  opciones: { type: Array, required: true },
  claveId: { type: String, default: 'id' },       // Ej: 'genero_id'
  claveTexto: { type: String, default: 'nombre' } // Ej: 'nombre_genero'
})
defineEmits(['update:modelValue'])
</script>
