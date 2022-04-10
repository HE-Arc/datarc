<template>
    <div class="bg-gray-200 max-w-full min-w-0 cursor-pointer rounded-lg m-4 z-20" @click="openModal" @keydown.esc="closeModal" tabindex="0">
        <div class="w-full">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            
            <div class="w-full rounded-b-lg bg-red-400 opacity-70">
                <div class="w-11/12 font-bold overflow-hidden overflow-ellipsis mx-auto whitespace-nowrap backdrop-opacity-100">
                    {{ filename }}
                </div>
            </div>
        </div>
    </div>
    <Modal :isShow="isSelected" @close-modal="closeModal"/>
</template>

<script>

import Modal from "@/components/Modal";

export default {
    props: {
        name : String,
    },
    data() {
        return {
            filename: "New File",
            date: "17.03.2022",
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
    mounted() {
        if (this.name != null)
            this.filename = this.name;
    },
};
</script>
<style >
</style>
