<template>
	<Transition name="fade">
		<div class="modal fixed w-full h-full top-0 left-0 flex items-center justify-center text-black z-10" v-if="isShow">
			<div class="modal-overlay absolute w-full h-full bg-gray-900 opacity-50"></div>

			<div class="modal-container bg-white w-11/12 md:max-w-md lg:max-w-lg mx-auto rounded shadow-lg z-50 overflow-y-auto">
				<div class="absolute top-0 right-0 cursor-pointer flex flex-col items-center mt-4 mr-4 text-white text-s0">
					<svg @click="closeModal" class="fill-current text-white" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
						<path d="M14.53 4.53l-1.06-1.06L9 7.94 4.53 3.47 3.47 4.53 7.94 9l-4.47 4.47 1.06 1.06L9 10.06l4.47 4.47 1.06-1.06L10.06 9z"></path>
					</svg>
					<span class="text-sm">(Esc)</span>
				</div>

				<!-- Add margin if you want to see some of the overlay behind the modal-->
				<div class="modal-content py-4 text-left px-6">
					<!--Title-->
					<div class="flex justify-between items-center pb-3">
						<p class="text-2xl font-bold">{{ name }}</p>
						<div @click="closeModal" class="cursor-pointer z-50">
							<svg class="fill-current text-black" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" >
								<path d="M14.53 4.53l-1.06-1.06L9 7.94 4.53 3.47 3.47 4.53 7.94 9l-4.47 4.47 1.06 1.06L9 10.06l4.47 4.47 1.06-1.06L10.06 9z"></path>
							</svg>
						</div>
					</div>

					<!--Body-->
					<p>Date de mise en ligne : {{ date }}</p>
					<p>Auteur : {{ author }}</p>
					<p>Format du fichier : {{ formatFile }}</p>
					<p>
						<label for="fname">name:</label>
						<input
							type="text"
							id="fname"
							name="fname"
							style="border-bottom: 1px solid orange"
						/>
						<button
							class="px-4 bg-transparent p-3 rounded-lg text-indigo-500 hover:bg-gray-100 hover:text-indigo-400 mr-2"
							@click="share"
						>
							share
						</button>
					</p>

					<!--Footer-->
					<div class="flex justify-end pt-2">
						<button class="px-4 bg-transparent p-3 rounded-lg text-indigo-500 hover:bg-gray-100 hover:text-indigo-400 mr-2" @click="copy">
							copy link
						</button>

						<button class="px-4 bg-transparent p-3 rounded-lg text-indigo-500 hover:bg-gray-100 hover:text-indigo-400 mr-2" @click="download">
							download
						</button>
						<button @click="closeModal" class="px-4 bg-indigo-500 p-3 rounded-lg text-white hover:bg-indigo-400">
							Close
						</button>
						<button @click="deleteFile" class="px-4 bg-red-500 p-3 rounded-lg text-white hover:bg-red-400">
							Delete
						</button>
					</div>
				</div>
			</div>
			<div id="snackbar">link copied to clipboard...</div>
		</div>
	</Transition>
</template>
<script>
	import { downloadFile, getLink } from "../Tools/UploadTools.js";
	import { getCookie } from "../Tools/Cookie.js";
	import { fileUpdate } from "../Tools/Network.js";
	import { validMail } from "../Tools/Valid.js";

	export default {
		props: {
			isShow: Boolean,
			name: String,
			date: String,
			author: String,
			url: String,
			ispublic: String,
		},
		data() {
			return {
				formatFile: "inconu",
			};
		},
		components: {},
		watch: {
			name: function () {
				let temp = this.name.split(".");
				if (temp.length() > 1) {
					this.formatFile = temp[temp.length() - 1];
				}
			},
		},
		methods: {
			async share() {
				let token = getCookie("token");
				let name = document.getElementById("fname").value;
				if (!validMail(name)) {
					return;
				}
				if (token != "") {
					try {
						let data = await fileUpdate(
							"sharefile",
							{
								Authentication: token,
							},
							this.url + "&name=" + name
						);
						this.error(data.status);
					} catch (error) {
						error;
					}
				}
			},
			async checked() {
				let token = getCookie("token");
				if (token != "") {
					try {
						await fileUpdate(
							"public",
							{
								Authentication: token,
							},
							this.url
						);
					} catch (error) {
						error;
					}
				}
			},
			async deleteFile() {
				let token = getCookie("token");
				if (token != "") {
					try {
						await fileUpdate(
							"delete",
							{
								Authentication: token,
							},
							this.url
						);
					} catch (error) {
						error;
					}
					this.closeModal();
				}
			},
			closeModal() {
				this.$emit("close-modal");
			},
			async download() {
				let token = getCookie("token");
				console.log(this.url);
				try {
					await downloadFile(this.url, token, this.name);
				} catch (e) {
					this.error("error while downloading the file");
				}
			},
			copy() {
				navigator.clipboard.writeText(getLink(this.url));
				var x = document.getElementById("snackbar");
				x.className = "show";
				setTimeout(function () {
					x.className = x.className.replace("show", "");
				}, 3000);
			},
			error(msg) {
				this.$toast.open({
					message: msg,
					type: "warning", // warning, info, error, success,
					dismissible: true,
				});
			},
		},
		created() {
			let temp = this.name.split(".");
			if (temp.length > 1) {
				this.formatFile = "." + temp[temp.length - 1];
			}
		},
	};
</script>
<style>

	.fade-enter-active,
	.fade-leave-active {
		transition: opacity 0.25s ease;
	}

	.fade-enter-from,
	.fade-leave-to {
		opacity: 0;
	}

	#snackbar {
		visibility: hidden;
		min-width: 250px;
		margin-left: -125px;
		color: #fff;
		background-color: #333;
		text-align: center;
		border-radius: 5px;
		padding: 16px;
		position: fixed;
		left: 50%;
		bottom: 30px;
		font-size: 17px;
	}

	#snackbar.show {
		visibility: visible;
		-webkit-animation: fadein 0.5s, fadeout2 0.5s 2.5s;
		animation: fadein 0.5s, fadeout2 0.5s 2.5s;
	}

	@-webkit-keyframes fadein {
		from {
			bottom: 0;
			opacity: 0;
		}
		to {
			bottom: 30px;
			opacity: 1;
		}
	}

	@keyframes fadein {
		from {
			bottom: 0;
			opacity: 0;
		}
		to {
			bottom: 30px;
			opacity: 1;
		}
	}

	@-webkit-keyframes fadeout2 {
		from {
			bottom: 30px;
			opacity: 1;
		}
		to {
			bottom: 0;
			opacity: 0;
		}
	}

	@keyframes fadeout2 {
		from {
			bottom: 30px;
			opacity: 1;
		}
		to {
			bottom: 0;
			opacity: 0;
		}
	}
</style>
