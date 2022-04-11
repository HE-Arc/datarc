<template>
    <div class="bg-white cursor-pointer rounded-lg m-4 z-20" @click="openModal" @keydown.esc="closeModal" tabindex="0">
        <div class="w-full h-full relative">
            <svg class="h-5/6 text-black" xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            
            <div class="w-full h-1/6 rounded-b-lg bg-red-500 opacity-70">
                <div class="w-11/12 h-full font-bold overflow-hidden overflow-ellipsis mx-auto whitespace-nowrap blur-3xl">
                    {{ name }}
                </div>
            </div>
        </div>
    </div>
    <Modal :isShow="isSelected" @close-modal="closeModal" :name="name" :date="date" :author="author"/>
</template>

<script>

import Modal from "@/components/Modal";

export default {
    props: {
        name : String,
        date : String,
        author : String,
    },
    data() {
        return {
            isSelected : false,
        };
    },
    components: {
        Modal,
    },
    methods: {
        openModal() {
            this.isSelected = true;
        },
        closeModal(){
            this.isSelected = false;
        },
        keyPressed: function(event){
            if(this.isSelected){
                console.log(event.key);
                if(event.key === "Escape" || event.key === "Esc" || event.keyCode === 27){
                    this.closeModal();
                    console.log("PD");
                }
            }
        }
        
    },
};
</script>
<style >
</style>
