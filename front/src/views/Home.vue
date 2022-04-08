<template>
    <div class="h-screen">
        <NavigationBar/>
        <div class="grid justify-center mx-auto h-5/6 rounded-lg">
            <div class="flex m-auto gap-2">
                <div class="flex-col ">
                    <div class="title text-6xl text-yellow-400 mb-4">
                        Welcome
                    </div>
                    <p class="text-justify text-xl text-white">
                        {{ welcomeText }}
                    </p>
                </div>
                <div class="grid justify-center content-end w-1/3 p-2">
                    <router-link to="register" class="btn btn-yellow text-xl">Sign up</router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar';

export default {
    name: "Home",
    data() {
        return{
            welcomeText: 'Stocker et partager vos fichiers et dossier, entre vos appareils ou vos amis',
        }
    },
    methods: {},
    components: {
        NavigationBar,
    },
};
</script>

<style>

</style>