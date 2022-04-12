<template>
    <div
        class="w-full h-full absolute inline-block"
        @dragover.prevent
        @drop.prevent
    >
        <input type="file" id="file" ref="file" hidden />
        <div
            class="dropzone w-full h-full block border-dashed"
            @drop="onDrop"
            @dragenter="setEnter"
            @dragleave="setLeave"
        ></div>
    </div>
</template>

<script>
import { uploadFile } from "../Tools/UploadTools.js";
import { getCookie } from "../Tools/Cookie.js";

export default {
    name: "UploadWindow",
    data() {
        return {
            fileList: [],
        };
    },
    components: {},
    methods: {
        test() {
            console.log("yolo");
        },
        onChange() {
            this.fileList = [...this.$refs.file.files];
            this.upload();
        },
        setEnter(e) {
            if (e.target.classList.contains("dropzone")) {
                e.target.classList.add("border-8");
            }
        },
        setLeave(e) {
            if (e.target.classList.contains("dropzone")) {
                e.target.classList.remove("border-8");
            }
        },
        onDrop(e) {
            e.preventDefault();
            this.$refs.file.files = e.dataTransfer.files;
            this.number = this.$refs.file.files.length;
            this.onChange(); // Trigger the onChange event manually
            // Clean up
            this.setLeave(e);
        },
        upload() {
            console.log("upload !");
            const selectedFile = document.getElementById("file").files[0];
            if (selectedFile == null) {
                this.error("no file selected");
                return;
            }
            if (selectedFile.size > 2000000) {
                this.error("the file selected is too big !");
                return;
            }
            let token = getCookie("token");
            if (token != "") {
                try {
                    console.log("ahahahaha");
                    uploadFile(selectedFile, token);
                } catch (e) {
                    this.error(e);
                }
            }
        },
        error(msg) {
            console.log(msg);
        },
    },
};
</script>

<style >
</style>