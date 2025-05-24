/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}"
    
  ],
  theme: {
    extend: {
      colors: {
        primario: '#1e40af',
        secundario: '#f59e0b',
        grisclaro: '#f3f4f6'
      }
    }
  },
  plugins: [],
}
