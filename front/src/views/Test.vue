<template>
    <button v-on:click="test">salut</button>
</template>

<script>
export default {
    name: "test",
    setup() {},
    methods: {
        test() {
            console.log("salut");
        },
    },
};
</script>

<style >
</style>