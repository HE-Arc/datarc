<template>
    <div class="w-full h-full absolute inline-block" @dragover.prevent @drop.prevent>
        <input type="file" id="file" ref="file" accept=".pdf,.jpg,.jpeg,.png" @change="changeFile" hidden/>
        <div class="dropzone w-full h-full block border-dashed" @drop="onDrop" @dragenter="setEnter" @dragleave="setLeave">
        </div>
    </div>
</template>

<script>
import { uploadFile, downloadFile } from "../Tools/UploadTools.js";

export default {
    name: "UploadWindow",
    data() {
        return {
            fileList: [],
            number: 0,
        };
    },
    components: {},
    methods: {
        onChange(){
            this.fileList = [...this.$refs.file.files];
        },
        setEnter(e){
            if (e.target.classList.contains("dropzone") ) {
                e.target.classList.add("border-8");
            }
        },
        setLeave(e){
            if (e.target.classList.contains("dropzone") ) {
                e.target.classList.remove("border-8");
            }
        },
        onDrop(e){
            e.preventDefault();
            this.$refs.file.files = e.dataTransfer.files;
            console.log(this.$refs.file.files);
            console.log(this.$refs.file.files[0]);
            this.number = this.$refs.file.files.length;
            this.onChange(); // Trigger the onChange event manually
            // Clean up
            this.setLeave(e);
        },
        upload() {
            console.log("upload !");
            const selectedFile = document.getElementById("file").files[0];

            if (selectedFile == null) {
                return;
            }
            uploadFile(selectedFile, "7d501b56-d161-4250-baea-a9a2bccb6c99");
        },
        download() {
            downloadFile(
                "2f8d6671f92f4cb8ad753a30ae751187",
                "7d501b56-d161-4250-baea-a9a2bccb6c99"
            );
        },
    },
};
</script>

<style >
#errorMsg {
    display: v-bind(display);
}
</style>