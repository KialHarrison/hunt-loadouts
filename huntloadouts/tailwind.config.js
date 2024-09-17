/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		".loadouts/templates/loadouts/**/*.html",
		".roadmap/templates/roadmap/**/*.html",
		".user/templates/user/**/*.html",
		".dashboard/templates/dashboard/**/*.html",
		"./templates/**/*.html",
	],
	theme: {
		extend: {},
	},
	plugins: [require("@tailwindcss/forms")],
};
