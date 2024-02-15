/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./flaskr/templates/**/*.{html, js}"],
  purge: {
    enabled: true,
    content: ["./flaskr/templates/**/*.{html, js}"],
  },
  
  theme: {
    extend: {},
  },
  plugins: [],
}

