<template>
    <div class="w-full h-screen grid content-center bg-white-background-header dark:bg-dark-background-header">
        <router-link to="/">
            <div class="text-center logo text-yellow-300 text-5xl font-bold mb-10">
                Datarc
            </div>
        </router-link>
        <main class="bg-white-background-subtitle mx-auto p-8 rounded-lg shadow-2xl w-1/3">
            <section>
                <h3 class="font-bold text-2xl">Welcome to Datarc</h3>
                <p class="text-gray-600 pt-2">Create your account.</p>
            </section>

            <section class="mt-10">
                <form class="flex flex-col" method="POST" action="#">
                    <div class="mb-6 pt-3 rounded bg-gray-200">
                        <label class="block text-gray-700 text-sm font-bold mb-2 ml-3" for="email">Email</label>
                        <input type="text" id="email" class="bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-surline-yellow transition duration-500 px-3 pb-3">
                    </div>
                    <div class="mb-6 pt-3 rounded bg-gray-200">
                        <label class="block text-gray-700 text-sm font-bold mb-2 ml-3" for="password">Password</label>
                        <input type="password" id="password" class="bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-surline-yellow transition duration-500 px-3 pb-3">
                    </div>
                    <div class="mb-6 pt-3 rounded bg-gray-200">
                        <label class="block text-gray-700 text-sm font-bold mb-2 ml-3" for="password">Password</label>
                        <input type="password" id="password" class="bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-surline-yellow transition duration-500 px-3 pb-3">
                    </div>
                    <div class="flex justify-between">
                        <router-link to="login" class="text-sm text-surline-yellow hover:text-purple-700 hover:underline mb-6">Already have an account?</router-link>
                    </div>
                    <button class="bg-surline-yellow hover:bg-yellow-400 text-white-font font-bold py-2 rounded shadow-lg hover:shadow-xl transition duration-200" type="submit">Sign Up</button>
                </form>
            </section>
        </main>
    </div>
</template>

<script>
export default {
    name: "Register",
    data(){

    },
    components: {},
    method: {},
    created(){
        document.title = 'Register - ' + document.title;
    },
};
</script>