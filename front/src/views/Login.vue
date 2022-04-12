<template>
	<div class="w-full h-screen grid content-center">
		<router-link to="/">
			<div class="text-center logo text-yellow-300 text-8xl font-bold mb-10">
				Datarc
			</div>
		</router-link>
		<main class="bg-white mx-auto p-8 rounded-lg shadow-2xl md:w-1/3">
			<section>
				<h3 class="text-black font-bold text-2xl">Welcome to Datarc</h3>
				<p class="text-gray-600 pt-2">Sign in to your account.</p>
			</section>

			<section class="mt-10">
				<div class="flex flex-col">
					<div class="mb-6 pt-3 rounded bg-gray-200">
						<label class="block text-gray-700 text-sm font-bold mb-2 ml-3" for="username" >
							Username
						</label>
						<input type="text" id="username" class="bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-surline-yellow transition duration-500 px-3 pb-3"/>
					</div>
					<div class="mb-6 pt-3 rounded bg-gray-200">
						<label class="block text-gray-700 text-sm font-bold mb-2 ml-3" for="password">
							Password
						</label>
						<input type="password" id="password" class="bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-surline-yellow transition duration-500 px-3 pb-3"/>
					</div>
					<div class="flex justify-between">
						<router-link to="register" class="text-sm text-yellow-300 hover:text-yellow-400 hover:underline mb-6">
							Don't have an account?
						</router-link>
					</div>
					<button
						v-on:click="send"
						class="bg-yellow-300 hover:bg-yellow-400 text-white font-bold py-2 rounded shadow-lg hover:shadow-xl transition duration-200"
					>
						Sign In
					</button>
				</div>
			</section>
		</main>
	</div>
</template>

<script>
	import { sendData } from "../Tools/Network.js";
	import { setCookie } from "../Tools/Cookie.js";
	import { goTo } from "../Tools/nav.js";
	import { validUsername, validPassword } from "../Tools/Valid.js";

	export default {
		name: "Login",
		components: {},
		methods: {
			async send() {
				let mail = document.getElementById("username").value;
				let password1 = document.getElementById("password").value;
				if (validUsername(mail)) {
					if (validPassword(password1)) {
						try {
							let result = await sendData(
								"/login",
								{},
								{
									name: mail,
									password: password1,
								}
							);
							console.log(result);
							if (result.status == "ok") {
								setCookie("token", result.token);
								goTo("/");
							} else {
								this.error(result.status);
							}
						} catch {
							this.error("mail doesnt exist");
						}
					} else {
						this.error("password is not valid");
					}
				} else {
					this.error("mail is not valid");
				}
				return false;
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
