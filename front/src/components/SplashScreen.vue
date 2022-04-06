<template>
    <div class="fixed justify-center flex bg-gray-600 items-center w-full h-screen" :class="{fadeout: !isLoading }">
        <div class="text-4xl title text-yellow-300" >Welcome to Datarc 👋🏼</div>
    </div>
</template>

<script>

export default {
    name: "SplashScreen",
    props: {
      isLoading : Boolean,
    },
    
    methods: {},
    components: {},
};
</script>

<style>

.fadeout {
  animation: fadeout 0.5s forwards;
}

@keyframes fadeout {
  from{
    opacity: 1;
    top: 0px;
    visibility: initial;
  }
  to {
    opacity: 0;
    top: 100%;
    visibility: hidden;
  }
}
</style>