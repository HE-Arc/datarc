<template>
    <SplashScreen :isLoading="isLoading"/>
    <router-view v-slot="{ Component }" v-if="!isLoading">
        <component :is="Component"/>
    </router-view>
</template>

<script>
import SplashScreen from '@/components/SplashScreen';

export default {
    name: "App",
    components: {
        SplashScreen,
    },
    data() {
        return { 
            isLoading: true
        };
    },
    mounted() {
        setTimeout(() => {
            this.isLoading = false;
        }, 2000);
    }
};
</script>

<style>

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}


.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
