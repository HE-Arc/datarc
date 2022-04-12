<template>
	<div class="w-full bg-white-background-header dark:bg-dark-background-header">
		<div class="w-3/4 container flex justify-between items-center mx-auto">
			<div class="w-1/3">
				<div class="inline-block cursor-pointer text-yellow-300" @click="toggleDarkMode">
					<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 20 20" height="48px" viewBox="0 0 20 20" width="48px" fill="currentColor" v-if="!this.darkMode">
						<rect fill="none" height="20" width="20" />
						<path d="M10,7.5c1.38,0,2.5,1.12,2.5,2.5s-1.12,2.5-2.5,2.5S7.5,11.38,7.5,10S8.62,7.5,10,7.5z M10,6c-2.21,0-4,1.79-4,4s1.79,4,4,4 s4-1.79,4-4S12.21,6,10,6L10,6z M3.75,10.75c0.41,0,0.75-0.34,0.75-0.75c0-0.41-0.34-0.75-0.75-0.75h-2C1.34,9.25,1,9.59,1,10 s0.34,0.75,0.75,0.75H3.75z M18.25,10.75c0.41,0,0.75-0.34,0.75-0.75c0-0.41-0.34-0.75-0.75-0.75h-2c-0.41,0-0.75,0.34-0.75,0.75 s0.34,0.75,0.75,0.75H18.25z M9.25,3.75C9.25,4.16,9.59,4.5,10,4.5c0.41,0,0.75-0.34,0.75-0.75v-2C10.75,1.34,10.41,1,10,1 S9.25,1.34,9.25,1.75V3.75z M13.89,5.05c-0.29,0.29-0.29,0.77,0,1.06s0.77,0.29,1.06,0l1.06-1.06c0.29-0.29,0.29-0.77,0-1.06 c-0.29-0.29-0.77-0.29-1.06,0L13.89,5.05z M3.99,14.95c-0.29,0.29-0.29,0.77,0,1.06s0.77,0.29,1.06,0l1.06-1.06 c0.29-0.29,0.29-0.77,0-1.06c-0.29-0.29-0.77-0.29-1.06,0L3.99,14.95z M5.05,6.11c0.29,0.29,0.77,0.29,1.06,0s0.29-0.77,0-1.06 L5.05,3.99c-0.29-0.29-0.77-0.29-1.06,0s-0.29,0.77,0,1.06L5.05,6.11z M14.95,16.01c0.29,0.29,0.77,0.29,1.06,0s0.29-0.77,0-1.06 l-1.06-1.06c-0.29-0.29-0.77-0.29-1.06,0c-0.29,0.29-0.29,0.77,0,1.06L14.95,16.01z M9.25,18.25C9.25,18.66,9.59,19,10,19 c0.41,0,0.75-0.34,0.75-0.75v-2c0-0.41-0.34-0.75-0.75-0.75s-0.75,0.34-0.75,0.75V18.25z"/>
					</svg>
					<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 20 20" height="48px" viewBox="0 0 20 20" width="48px" fill="currentColor" v-if="this.darkMode" >
						<g>
							<rect fill="none" height="20" width="20" x="0" />
						</g>
						<g>
							<g>
								<path d="M15.46,13.85c-1.73,0-4.6-0.93-6.08-3.8C7.75,6.89,9.03,4.11,9.76,3C6,3.13,3,6.21,3,9.99c0,0.4,0.04,0.78,0.1,1.16 C3.39,11.06,3.69,11,4,11c0.03,0,0.06,0.01,0.09,0.01C4.04,10.68,4,10.34,4,9.99c0-2.63,1.67-4.85,4.03-5.67 c-0.52,1.53-0.79,3.76,0.46,6.18c1.2,2.33,3.32,3.66,5.31,4.14C12.74,15.51,11.41,16,10.01,16c-0.64,0-1.25-0.1-1.83-0.29 C8,16.03,7.76,16.3,7.46,16.52C8.25,16.82,9.11,17,10.01,17c2.45,0,4.6-1.26,5.86-3.17C15.74,13.85,15.6,13.85,15.46,13.85z"/>
								<path d="M7.5,14.5C7.5,13.67,6.83,13,6,13l-0.27,0C5.38,12.4,4.74,12,4,12c-1.1,0-2,0.9-2,2c0,1.1,0.9,2,2,2c0.53,0,1.54,0,2,0 C6.83,16,7.5,15.33,7.5,14.5z"/>
							</g>
						</g>
					</svg>
				</div>
			</div>
			<div class="">
				<router-link to="/" class="cursor-pointer">
					<div class=" text-center logo text-yellow-300 text-5xl font-bold my-4">
						Datarc
					</div>
				</router-link>
			</div>
			<div class="w-1/3">
				<ul class="flex flex-row justify-end mt-4 md:mt-0" v-if="!isConnected">
					<li>
						<router-link to="register" class="btn btn-yellow text-white bg-transparent rounded-r-none">
							Sign up
						</router-link>
					</li>
					<li>
						<router-link to="login" class="btn btn-yellow rounded-l-none">
							Sign in
						</router-link>
					</li>
				</ul>
				<ul class="flex flex-row justify-end mt-4 md:mt-0" v-else>
					<li>
						<button @click="deconnexion" class="btn btn-yellow text-white bg-transparent ">
							deconnexion
						</button>
					</li>
				</ul>
			</div>
		</div>
	</div>
</template>

<script>
	import { goTo } from "../Tools/nav.js";
	import { setCookie } from "../Tools/Cookie.js";

	export default {
		name: "SplashScreen",
		props: {
			isConnected: Boolean
		},
		data() {
			return {
				bool: true,
				darkMode: false,
			};
		},
		methods: {
			toggleDarkMode() {
				document.documentElement.classList.toggle("dark");
				this.darkMode = !this.darkMode;
				if (this.darkMode) {
					localStorage.theme = "dark";
				} else {
					localStorage.theme = "light";
				}
			},
			deconnexion() {
				setCookie("token", "");
				goTo("/");
			}
		},

		components: {},
		mounted() {
			if (
				localStorage.theme === "dark" ||
				(!("theme" in localStorage) &&
					window.matchMedia("(prefers-color-scheme: dark)").matches)
			) {
				document.documentElement.classList.add("dark");
			} else {
				document.documentElement.classList.remove("dark");
			}
			this.darkMode = document.documentElement.classList.contains("dark");
		},
	};
</script>

<style></style>
