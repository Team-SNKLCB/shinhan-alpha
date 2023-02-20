<template>
    <phone-header></phone-header>
    <div class="top-bar"></div>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
export default {
    components: {
        PhoneHeader,
    },
};
</script>

<style>
.top-bar {
    display: flex;
}
</style>
