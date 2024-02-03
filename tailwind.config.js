/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  purge: {
    enabled: true,
    content: ["./templates/**/*.{html,js}"],
  },
  
  theme: {
    extend: {},
  },
  plugins: [],
}

