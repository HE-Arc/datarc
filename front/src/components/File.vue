<template>
    <div class="bg-white rounded-lg border-0">
        <div v-on:click="extend" id="test" class="p-2">
            <h1 class="text-3xl" id="title">{{ name }} {{ id }}</h1>
            <p>{{ description }}</p>
            <Like v-on:click="liked" :n="like" />
        </div>
        <div id="body">
        </div>
    </div>
</template>

<script>

export default {
    data() {
        return {
            filename: "New File",
            date: "17.03.2022",
        };
    },
    components: {
    },
    methods: {
    }
};
</script>


<style >
</style>
