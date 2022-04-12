<template>
	<div class="w-full h-full absolute inline-block" @dragover.prevent @drop.prevent>
		<input type="file" id="file" ref="file" hidden />
		<div class="dropzone w-full h-full block border-blue-300 border-dashed z-50" @drop="onDrop" @dragenter="setEnter" @dragleave="setLeave">
			
		</div>
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
				document.getElementById("file").files = e.dataTransfer.files;
				console.log(document.getElementById("file").files)
				this.onChange(); // Trigger the onChange event manually
				// Clean up
				this.setLeave(e);
			},
			upload() {
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
						uploadFile(selectedFile, token);
						this.$parent.updateData();
					} catch (e) {
						this.error(e);
					}
				}
			},
			error(msg) {
				this.$toast.open({
					message: msg,
					type: "warning", // warning, info, error, success,
					dismissible: true,
				});
			},
		},
	};
</script>

<style></style>
