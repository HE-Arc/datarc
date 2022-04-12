<template>
	<div class="h-screen">
		<div class="flex flex-col h-full w-full mx-auto rounded-lg">
			<NavigationBar />
			<div
				class="w-11/12 mx-auto text-center text-2xl p-7 font-bold border-b-2 border-black dark:border-dark-border-1"
			>
				Mon Profile
			</div>
			<div class="flex gap-4 mx-8 mt-8 relative">
				<div class="w-1/2 h-full mx-auto relative">
					<div
						class="flex min-h-min justify-between bg-white-background-subtitle dark:bg-dark-background-subtitle rounded-md sticky top-0"
					>
						<div class="text-3xl font-bold text-center p-4">
							Mes Fichiers
						</div>
						<label
							for="file"
							class="w-16 p-2 text-yellow-300 cursor-pointer"
						>
							<input type="file" id="input1" required />
						</label>
						<button v-on:click="upload">Envoyer</button>
					</div>
					<div
						class="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 overflow-x-auto relative"
					>
						<UploadWindow />
						<File
							v-for="item in items"
							:key="item"
							:name="item.name"
							:date="item.date"
							:author="item.author"
							:url="item.url"
						/>
					</div>
				</div>
				<div class="w-1/2 mx-auto">
					<div
						class="flex bg-white-background-subtitle dark:bg-dark-background-subtitle rounded-md sticky top-0"
					>
						<div class="text-3xl font-bold text-center p-4">
							Mes fichiers partagés avec moi
						</div>
					</div>
					<div
						class="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 overflow-x-auto relative"
					>
						<File
							v-for="item in itemsOther"
							:key="item"
							:name="item.name"
							:date="item.date"
							:author="item.author"
							:url="item.url"
						/>
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
				itemsOther: [
					{
						name: "mathieu.xlsx",
						date: "02.04.2022",
						author: "Mathieu",
						url: "aa",
					},
					{
						name: "thibault.pdf",
						date: "02.04.2022",
						author: "Thibault",
						url: "aa",
					},
				],
			};
		},
		methods: {
			upload() {
				console.log("upload !");
				const selectedFile = document.getElementById("input1").files[0];
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
						for (let i = 0; i < data.files.length; i++) {
							this.items.push({
								name: data.files[i].name,
								data: "",
								author: "me",
								url: data.files[i].url,
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
