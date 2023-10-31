/** @type {import('tailwindcss').Config} */

const { join } = require('path');

module.exports = {
  content: [
    "./src/**/*.{html,js}",
    // join(__dirname,"./src/**/*.{html,js}"),
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

