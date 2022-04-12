<template>
    <div
        class="
            w-full
            h-screen
            grid
            content-center
            bg-white-background-header
            dark:bg-dark-background-header
        "
    >
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
        <main
            class="
                bg-white-background-subtitle
                mx-auto
                p-8
                rounded-lg
                shadow-2xl
                w-1/3
            "
        >
            <section>
                <h3 class="font-bold text-2xl">Welcome to Datarc</h3>
                <p class="text-gray-600 pt-2">Create your account.</p>
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
                                focus:border-surline-yellow
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
                            id="password1"
                            class="
                                bg-gray-200
                                rounded
                                w-full
                                text-gray-700
                                focus:outline-none
                                border-b-4 border-gray-300
                                focus:border-surline-yellow
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
                            id="password2"
                            class="
                                bg-gray-200
                                rounded
                                w-full
                                text-gray-700
                                focus:outline-none
                                border-b-4 border-gray-300
                                focus:border-surline-yellow
                                transition
                                duration-500
                                px-3
                                pb-3
                            "
                        />
                    </div>
                    <div class="flex justify-between">
                        <router-link
                            to="login"
                            class="
                                text-sm text-surline-yellow
                                hover:text-purple-700 hover:underline
                                mb-6
                            "
                            >Already have an account?</router-link
                        >
                    </div>
                    <button
                        class="
                            bg-surline-yellow
                            hover:bg-yellow-400
                            text-white-font
                            font-bold
                            py-2
                            rounded
                            shadow-lg
                            hover:shadow-xl
                            transition
                            duration-200
                        "
                        type="submit"
                        v-on:click="send"
                    >
                        Sign Up
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
    name: "Register",
    data() {},
    components: {},
    methods: {
        async send() {
            console.log("salut");
            let mail = document.getElementById("email").value;
            let password1 = document.getElementById("password1").value;
            let password2 = document.getElementById("password2").value;
            if (password1 == password2) {
                if (validMail(mail)) {
                    if (validPassword(password1)) {
                        try {
                            console.log("SANDINGGG");
                            let result = await sendData(
                                "/create_user",
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
                            this.error("mail already used");
                        }
                    } else {
                        this.error("password is not valid");
                    }
                } else {
                    this.error("mail is not valid");
                }
            } else {
                this.error("passwords are not similar");
            }
            return false;
        },
        created() {
            document.title = "Register - " + document.title;
        },
        error(error) {
            console.log(error);
        },
    },
};
</script>