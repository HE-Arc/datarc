<template>
    <div class="h-screen">
        <NavigationBar/>
        <div class="flex flex-col w-2/3 mx-auto rounded-lg">
            <div class="mx-auto">
                Mathieu
            </div>
            <div class="mx-auto">
                <div class="text-2xL">Mes Fichiers</div>
                <File/>
            </div>
            <div class="mx-auto">
                <div class="text-2xL">Mes Partager avec moi</div>
                <File/>
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