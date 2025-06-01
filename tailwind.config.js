/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		"./api/**/*.html", // Incluye todos los archivos .templ
	],
	theme: {
		extend: {},
		fontFamily: {
			roboto: ["Roboto", "sans-serif"],
			// bangers: ["Bangers", "sans-serif"],
		},
	},
	plugins: [],
};
