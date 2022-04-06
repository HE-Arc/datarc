<template>
    <div class="h-screen">
        <NavigationBar/>
        <div class="flex flex-col w-full p-10 mx-auto rounded-lg">
            <div class="mx-auto">
                Mon Profile
            </div>
            <div class="flex gap-4">
                <div class="w-1/2 mx-auto">
                    <div class="flex justify-between bg-gray-700">
                        <div class="text-3xl font-bold text-center p-4">Mes Fichiers</div>
                        <svg class="w-10 p-2" xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                            <path strokeLinecap="round" strokeLinejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" />
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
import File from '@/components/File';

export default {
    name: "Profile",
    methods: {},
    components: {
        NavigationBar,
        File,
    },
};
</script>

<style>

</style>