<template>
    <div class="bg-gray-200 max-w-full min-w-0 cursor-pointer rounded-lg m-4 z-20" @click="toggleModal">
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
    <div class="modal fixed w-full h-full top-0 left-0 flex items-center justify-center z-30" v-if="isSelected">
        <div class="modal-overlay absolute w-full h-full bg-gray-900 opacity-50"></div>
    
        <div class="modal-container bg-white w-11/12 md:max-w-md mx-auto rounded shadow-lg z-50 overflow-y-auto">
      
            <div class="absolute top-0 right-0 cursor-pointer flex flex-col items-center mt-4 mr-4 text-white text-sm z-50">
                <svg @click="toggleModal" class="fill-current text-white" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
                    <path d="M14.53 4.53l-1.06-1.06L9 7.94 4.53 3.47 3.47 4.53 7.94 9l-4.47 4.47 1.06 1.06L9 10.06l4.47 4.47 1.06-1.06L10.06 9z"></path>
                </svg>
                <span class="text-sm">(Esc)</span>
            </div>

            <!-- Add margin if you want to see some of the overlay behind the modal-->
            <div class="modal-content py-4 text-left px-6">
                <!--Title-->
                <div class="flex justify-between items-center pb-3">
                <p class="text-2xl font-bold">{{ filename }}</p>
                <div @click="toggleModal" class="cursor-pointer z-50">
                    <svg class="fill-current text-black" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
                        <path d="M14.53 4.53l-1.06-1.06L9 7.94 4.53 3.47 3.47 4.53 7.94 9l-4.47 4.47 1.06 1.06L9 10.06l4.47 4.47 1.06-1.06L10.06 9z"></path>
                    </svg>
                </div>
                </div>

                <!--Body-->
                <p>Modal content can go here </p>
                <p>...</p>
                <p>...</p>
                <p>...</p>
                <p>...</p>

                <!--Footer-->
                <div class="flex justify-end pt-2">
                    <button class="px-4 bg-transparent p-3 rounded-lg text-indigo-500 hover:bg-gray-100 hover:text-indigo-400 mr-2">Action</button>
                    <button @click="toggleModal" class="px-4 bg-indigo-500 p-3 rounded-lg text-white hover:bg-indigo-400">Close</button>
                </div>
            
            </div>
        </div>
    </div>
</template>

<script>

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
    },
    methods: {
        toggleModal () {
            this.isSelected = !this.isSelected
        },
        keyPressed: function(evt){
            if(this.isSelected){
                if(evt.key === "Escape" || evt.key === "Esc" || evt.keyCode === 27){
                    this.toggleModal()
                }
            }
        }
        
    },
    mounted() {
        window.addEventListener('keypress', this.keyPressed);
        if (this.name != null)
            this.filename = this.name
    },
    unmounted() {
        window.removeEventListener('keypress', this.keyPressed);
    },
};
</script>
<style >
.modal {
    transition: opacity 0.25s ease;
}
body.modal-active {
    overflow-x: hidden;
    overflow-y: visible !important;
}
</style>
