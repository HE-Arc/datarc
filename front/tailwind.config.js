module.exports = {
  darkMode: 'class',
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx,}'],
  content: [],
  theme: {
    extend: {
      fontFamily: {
        'display': ['chango','Megrim'],
      },
      colors: {
        'dark-background': '#171E29',
        'dark-background-header': '#213145',
        'dark-background-subtitle': '#25374F',
        'dark-font' : '#FFFFFF',
        'dark-border-1' : '#C5D9E8',
        'surline-yellow' :'#FDDC35',
        'crimson' : 'E0102B',
        'white-background': '#ECF5FD',
        'white-background-header': '#25374F',
        'white-background-subtitle': '#5980B1',
        'white-font' : '#24242E',
      },
    },
  },
  plugins: [],
}
