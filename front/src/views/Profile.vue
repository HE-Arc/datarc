<template>
    <div class="h-screen">
        <div class="flex flex-col h-full w-full mx-auto rounded-lg">
            <NavigationBar/>
            <div class="mx-auto">
                Mon Profile
            </div>
            <div class="flex gap-4 h-full mx-8 mt-8">
                <div class="w-1/2 h-full mx-auto relative">
                <UploadWindow/>
                    <div class="flex justify-between bg-gray-700">
                        <div class="text-3xl font-bold text-center p-4">Mes Fichiers</div>
                        <svg class="w-16 p-2 text-yellow-300" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" />
                        </svg>
                    </div>
                    <div class="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
                        <File name="Salut daslikjdasolkdkj ojdal jslda"/>
                        <File/>
                    </div>
                </div>
                <div class="w-1/2 mx-auto">
                    <div class="flex bg-gray-700">
                        <div class="text-3xl font-bold text-center p-4">Mes fichiers partagés avec moi</div>
                    </div>
                    <div class="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
                        <File/>
                        <File/>
                    </div>
                </div> 
            </div> 
        </div>
    </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar';
import UploadWindow from '@/components/UploadWindow';
import File from '@/components/File';

export default {
    name: "Profile",
    methods: {},
    components: {
        NavigationBar,
        UploadWindow,
        File,
    },
};
</script>

<style>

</style>