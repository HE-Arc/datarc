<template>
	<div class="h-screen">
		<NavigationBar :isConnected="isConnected"/>
		<div class="grid justify-center mx-auto h-5/6 rounded-lg w-full">
			<div class="flex flex-col md:flex-row m-auto gap-2 w-full">
				<div class="">
					<div v-if="isConnected">
						<div class="title text-4xl md:text-6xl text-yellow-400 mb-4">
							Welcome
						</div>
						<div class="text-lg font-bold my-2 text-yellow-400">
							{{ name }} !
						</div>
					</div>
					
					<div v-else class="title text-4xl md:text-6xl text-yellow-400 mb-4">
						Welcome
					</div>
					<p class="text-justify text-lg md:text-xl">
						{{ welcomeText }}
					</p>
				</div>
				<div class="grid justify-center content-end w-1/3 p-2">
					<router-link
						v-if="isConnected"
						to="profile"
						class="btn btn-yellow text-lg md:text-xl"
						>profile</router-link
					>
					<router-link
						v-else
						to="register"
						class="btn btn-yellow text-lg md:text-xl"
						>Sign up</router-link
					>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import NavigationBar from "@/components/NavigationBar";
import { getCookie } from "../Tools/Cookie.js";
import { getData } from "../Tools/Network.js";

export default {
  name: "Home",
  data() {
    return {
      welcomeText:
        "Stocker et partager vos fichiers et dossier, entre vos appareils ou vos amis",
      isConnected: false,
      name: "",
    };
  },
  methods: {},
  components: {
    NavigationBar,
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
        error;
      }
    }
  },
};
</script>

<style></style>
