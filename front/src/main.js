import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './index.css'
import VueToast from 'vue-toast-notification';
createApp(App)
    .use(router)
    .use(VueToast, {
        // One of the options
        position: 'bottom-right',
        duration: 2000,
    })
    .mount('#app')