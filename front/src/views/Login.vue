<template>
    <div class="w-full h-screen grid content-center">
        <router-link to="/">
            <div
                class="
                    text-center
                    logo
                    text-yellow-300 text-5xl
                    font-bold
                    mb-10
                "
            >
                Datarc
            </div>
        </router-link>
        <main class="bg-white mx-auto p-8 rounded-lg shadow-2xl w-1/3">
            <section>
                <h3 class="font-bold text-2xl">Welcome to Datarc</h3>
                <p class="text-gray-600 pt-2">Sign in to your account.</p>
            </section>

            <section class="mt-10">
                <div class="flex flex-col">
                    <div class="mb-6 pt-3 rounded bg-gray-200">
                        <label
                            class="
                                block
                                text-gray-700 text-sm
                                font-bold
                                mb-2
                                ml-3
                            "
                            for="email"
                            >Email</label
                        >
                        <input
                            type="text"
                            id="email"
                            class="
                                bg-gray-200
                                rounded
                                w-full
                                text-gray-700
                                focus:outline-none
                                border-b-4 border-gray-300
                                focus:border-purple-600
                                transition
                                duration-500
                                px-3
                                pb-3
                            "
                        />
                    </div>
                    <div class="mb-6 pt-3 rounded bg-gray-200">
                        <label
                            class="
                                block
                                text-gray-700 text-sm
                                font-bold
                                mb-2
                                ml-3
                            "
                            for="password"
                            >Password</label
                        >
                        <input
                            type="password"
                            id="password"
                            class="
                                bg-gray-200
                                rounded
                                w-full
                                text-gray-700
                                focus:outline-none
                                border-b-4 border-gray-300
                                focus:border-purple-600
                                transition
                                duration-500
                                px-3
                                pb-3
                            "
                        />
                    </div>
                    <div class="flex justify-between">
                        <router-link
                            to="register"
                            class="
                                text-sm text-purple-600
                                hover:text-purple-700 hover:underline
                                mb-6
                            "
                            >Don't have an account?</router-link
                        >
                        <router-link
                            to="recoverPassword"
                            class="
                                text-sm text-purple-600
                                hover:text-purple-700 hover:underline
                                mb-6
                            "
                            >Forgot your password?</router-link
                        >
                    </div>
                    <button
                        v-on:click="send"
                        class="
                            bg-purple-600
                            hover:bg-purple-700
                            text-white
                            font-bold
                            py-2
                            rounded
                            shadow-lg
                            hover:shadow-xl
                            transition
                            duration-200
                        "
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
import { validMail, validPassword } from "../Tools/Valid.js";

export default {
    name: "Login",
    components: {},
    methods: {
        async send() {
            let mail = document.getElementById("email").value;
            let password1 = document.getElementById("password").value;
            if (validMail(mail)) {
                if (validPassword(password1)) {
                    try {
                        console.log("SANDINGGG");
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
            console.log(msg);
        },
    },
};
</script>

<style>
</style>