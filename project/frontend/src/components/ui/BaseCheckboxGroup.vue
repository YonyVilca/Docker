<template>
  <div class="mb-4">
    <label v-if="label" class="block mb-1 font-medium text-gray-700">{{ label }}</label>
    <div class="grid grid-cols-2 gap-2">
      <label
        v-for="item in opciones"
        :key="item[claveId]"
        class="flex items-center gap-2"
      >
        <input
          type="checkbox"
          class="form-checkbox"
          :value="item[claveId]"
          :checked="modelValue.includes(item[claveId])"
          @change="toggle(item[claveId])"
        />
        {{ item[claveTexto] }}
      </label>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: Array,
  label: String,
  opciones: { type: Array, required: true },
  claveId: { type: String, default: 'id' },
  claveTexto: { type: String, default: 'nombre' }
})
const emit = defineEmits(['update:modelValue'])

const toggle = (valor) => {
  const nuevo = [...props.modelValue]
  const index = nuevo.indexOf(valor)
  if (index === -1) {
    nuevo.push(valor)
  } else {
    nuevo.splice(index, 1)
  }
  emit('update:modelValue', nuevo)
}
</script>
