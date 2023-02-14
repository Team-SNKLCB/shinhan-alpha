<template>
    <div class="home"></div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
    name: "HomeView",
    components: {
        HelloWorld,
    },
};
</script>

<style scoped>
.home {
    background-color: black;
    height: 100vh;
}
</style>
