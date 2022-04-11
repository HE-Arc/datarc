<template>
    <div class="h-screen">
        <div class="flex flex-col h-full w-full mx-auto rounded-lg">
            <NavigationBar/>
            <div class="w-11/12 mx-auto text-center text-2xl p-7 font-bold border-b-2 border-black dark:border-dark-border-1">
                Mon Profile
            </div>
            <div class="flex gap-4 mx-8 mt-8 relative">
                <div class="w-1/2 h-full mx-auto relative">
                    <div class="flex min-h-min justify-between bg-white-background-subtitle dark:bg-dark-background-subtitle rounded-md sticky top-0 z-50">
                        <div class="text-3xl font-bold text-center p-4 ">
                            Mes Fichiers
                        </div>
                        <input type="file" id="file" hidden/>
                        <label for="file" class="w-16 p-2 text-yellow-300 cursor-pointer z-40">
                            <svg @click="upload" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" />
                            </svg>
                        </label>
                    </div>
                    <div class="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 overflow-x-auto relative">
                        <UploadWindow/>
                        <File v-for="item in items" :key="item" :name="item.name" :date="item.date" :author="item.author"/>
                    </div>
                </div>
                <div class="w-1/2 mx-auto">
                    <div class="flex bg-white-background-subtitle dark:bg-dark-background-subtitle rounded-md sticky top-0 z-50">
                        <div class="text-3xl font-bold text-center p-4">Mes fichiers partagés avec moi</div>
                    </div>
                    <div class="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 overflow-x-auto relative">
                        <File v-for="item in itemsOther" :key="item" :name="item.name" :date="item.date" :author="item.author"/>
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
    data() {
        return {
            items: [
                {
                    name : 'test',
                    date : '02.04.2022',
                    author : 'Loïc'
                },
                {
                    name : 'test1',
                    date : '02.04.2022',
                    author : 'Loïc'
                },
                {
                    name : 'test2',
                    date : '02.04.2022',
                    author : 'Loïc'
                },
                {
                    name : 'test3',
                    date : '02.04.2022',
                    author : 'Loïc'
                },
                {
                    name : 'test4dajkjdna lkndaslkd aslidjasoi jdaosijd asoijd oiasjdoasij oisajd oiasjasoidj asoidja',
                    date : '02.04.2022',
                    author : 'Loïc'
                },
            ],
            itemsOther: [
                {
                    name : 'mathieu.xlsx',
                    date : '02.04.2022',
                    author : 'Mathieu'
                },
                {
                    name : 'thibault.pdf',
                    date : '02.04.2022',
                    author : 'Thibault'
                },
            ],
        };
    },
    methods: {
    },
    components: {
        NavigationBar,
        UploadWindow,
        File,
    },
};
</script>

<style>

</style>