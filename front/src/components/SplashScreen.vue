<template>
    <div class="fixed justify-center flex bg-gray-600 items-center w-full h-screen" :class="{fadeout: !isLoading }">
        <div class="text-4xl title text-yellow-300" >Welcome to Datarc 👋🏼</div>
    </div>
</template>

<script>

export default {
    name: "SplashScreen",
    props: ['isLoading'],
    
    methods: {},
    components: {},
};
</script>

<style>

.fadeout {
  animation: fadeout 2s forwards;
}

@keyframes fadeout {
  to {
    opacity: 0;
    visibility: hidden;
  }
}
</style>