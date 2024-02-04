/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./flaskr/templates/**/*.{html, jinja2, js}"],
  purge: {
    enabled: true,
    content: ["./flaskr/templates/**/*.{html, jinja2, js}"],
  },
  
  theme: {
    extend: {},
  },
  plugins: [],
}

