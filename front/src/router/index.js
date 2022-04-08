import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Upload from '../views/Upload.vue'
import Register from '../views/Register.vue'
import Profile from '../views/Profile.vue'

const routes = [{
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            transition : 'fade',
        },
    },
    {
        path: '/login',
        name: 'login',
        component: Login,
        meta: {
        },
    },
    {
        path: '/upload',
        name: 'upload',
        component: Upload,
        meta: {
        },
    },
    {
        path: '/register',
        name: 'register',
        component: Register,
        meta: {
        },
    },
    {
        path: '/profile',
        name: 'profile',
        component: Profile,
        meta: {
        },
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router