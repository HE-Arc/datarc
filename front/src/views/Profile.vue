<template>
	<div class="h-screen">
		<div class="flex flex-col h-full w-full mx-auto rounded-lg">
			<NavigationBar :isConnected="true"/>
			<div class="w-11/12 mx-auto text-center text-2xl p-7 font-bold border-b-2 border-black dark:border-dark-border-1">
				Mon Profile
			</div>
			<div class="flex flex-col md:flex-row gap-4 mx-8 mt-8 relative">
				<div class="w-full md:w-1/2 h-full mx-auto relative">
					<div class="flex min-h-min justify-between bg-white-background-subtitle dark:bg-dark-background-subtitle rounded-md sticky top-0 z-30">
						<div class="text-3xl font-bold text-center p-4">
							Mes Fichiers
						</div>
						<input type="file" id="file" @change="upload" hidden/>
                        <label for="file" class="w-16 p-2 text-yellow-300 cursor-pointer">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" />
                            </svg>
                        </label>
					</div>
					<div class="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 overflow-x-auto relative">
						<UploadWindow />
						<File v-for="item in items" :key="item" :name="item.name" :date="item.date" :author="item.author" :url="item.url" :ispublic="item.ispublic"/>
					</div>
				</div>
				<div class="w-full md:w-1/2 mx-auto">
					<div class="flex bg-white-background-subtitle dark:bg-dark-background-subtitle rounded-md sticky top-0 z-30">
						<div class="text-3xl font-bold text-center p-4">
							Mes fichiers partagés avec moi
						</div>
					</div>
					<div class="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 overflow-x-auto relative">
						<File v-for="item in itemsOther" :key="item" :name="item.name" :date="item.date" :author="item.author" :url="item.url" :ispublic="item.ispublic"/>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import NavigationBar from "@/components/NavigationBar";
	import UploadWindow from "@/components/UploadWindow";
	import File from "@/components/File";
	import { getData } from "../Tools/Network.js";
	import { getCookie } from "../Tools/Cookie.js";
	import { goTo } from "../Tools/nav.js";
	import { uploadFile } from "../Tools/UploadTools.js";

	export default {
		name: "Profile",
		data() {
			return {
				items: [],
				itemsOther: [],
			};
		},
		methods: {
			async updateData() {
				let token = getCookie("token");
				try {
					let data = await getData("/files", {
						Authentication: token,
					});
					if (data.status == "ok") {
						this.items = [];
						for (let i = 0; i < data.myfiles.length; i++) {
							this.items.push({
								name: data.myfiles[i].name,
								data: "",
								author: "me",
								url: data.myfiles[i].url,
								ispublic: data.myfiles[i].public,
							});
						}
						this.itemsOther = [];
						for (let i = 0; i < data.sharedfiles.length; i++) {
							this.itemsOther.push({
								name: data.sharedfiles[i].name,
								date: "",
								author: "not me",
								url: data.sharedfiles[i].url,
								ispublic: data.sharedfiles[i].public,
							});
						}
					}
				} catch (error) {
					goTo("/");
				}
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
						uploadFile(selectedFile, token);
						this.$toast.open({
							message: "uploading ...",
							type: "success", // warning, info, error, success,
							dismissible: true,
						});
						setTimeout(this.updateData, 1000);
					} catch (e) {
						this.error(e);
					}
				}
			},
			error(msg) {
				console.log(msg);
				this.$toast.open({
					message: msg,
					type: "warning", // warning, info, error, success,
					dismissible: true,
				});
			},
		},
		components: {
			NavigationBar,
			UploadWindow,
			File,
		},
		async created() {
			let token = getCookie("token");
			if (token != "") {
				try {
					let data = await getData("/user", {
						Authentication: token,
					});
					if (data.status == "ok") {
						this.isConnected = true;
						this.name = data.name;
					}
				} catch (error) {
					goTo("/");
				}
				try {
					let data = await getData("/files", {
						Authentication: token,
					});
					if (data.status == "ok") {
						for (let i = 0; i < data.myfiles.length; i++) {
							this.items.push({
								name: data.myfiles[i].name,
								date: "",
								author: "me",
								url: data.myfiles[i].url,
								ispublic: data.myfiles[i].public,
							});

							console.log(this.items);
						}
						for (let i = 0; i < data.sharedfiles.length; i++) {
							this.itemsOther.push({
								name: data.sharedfiles[i].name,
								date: "",
								author: "not me",
								url: data.sharedfiles[i].url,
								ispublic: data.sharedfiles[i].public,
							});
						}
					}
				} catch (error) {
					goTo("/");
				}
			} else {
				goTo("/");
			}
		},
	};
</script>

<style></style>
