<template>
    <div class="w-full h-screen grid content-center">
        <main class="bg-white mx-auto p-8 rounded-lg shadow-2xl w-1/3">
            <section>
                <h3 class="font-bold text-2xl">Welcome to Datarc</h3>
                <p class="text-gray-600 pt-2">Create your account.</p>
            </section>

            <section class="mt-10">
                <form class="flex flex-col" method="POST" action="#">
                    <div class="mb-6 pt-3 rounded bg-gray-200">
                        <label class="block text-gray-700 text-sm font-bold mb-2 ml-3" for="email">Email</label>
                        <input type="text" id="email" class="bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-purple-600 transition duration-500 px-3 pb-3">
                    </div>
                    <div class="mb-6 pt-3 rounded bg-gray-200">
                        <label class="block text-gray-700 text-sm font-bold mb-2 ml-3" for="password">Password</label>
                        <input type="password" id="password" class="bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-purple-600 transition duration-500 px-3 pb-3">
                    </div>
                    <div class="mb-6 pt-3 rounded bg-gray-200">
                        <label class="block text-gray-700 text-sm font-bold mb-2 ml-3" for="password">Password</label>
                        <input type="password" id="password" class="bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-purple-600 transition duration-500 px-3 pb-3">
                    </div>
                    <div class="flex justify-between">
                        <router-link to="login" class="text-sm text-purple-600 hover:text-purple-700 hover:underline mb-6">Already have an account?</router-link>
                        <router-link to="recoverPassword" class="text-sm text-purple-600 hover:text-purple-700 hover:underline mb-6">Forgot your password?</router-link>
                    </div>
                    <button class="bg-purple-600 hover:bg-purple-700 text-white font-bold py-2 rounded shadow-lg hover:shadow-xl transition duration-200" type="submit">Sign Up</button>
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