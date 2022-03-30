<template>
    <div>
        <input type="file" id="input" multiple />
        <button v-on:click="upload">upload</button>
        <br />
        <button v-on:click="download">download</button>
    </div>
</template>

<script>
import { uploadFile, downloadFile } from "../Tools/UploadTools.js";

export default {
    name: "UploadWindow",
    data() {
        return {};
    },
    components: {},
    methods: {
        upload() {
            console.log("upload !");
            const selectedFile = document.getElementById("input").files[0];
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