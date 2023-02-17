<template>
    <phone-header></phone-header>
    <div class="easy-menu-header"></div>
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
.easy-menu-header {
    width: 320px;
    height: 46px;
    background-color: #354ef2;
}
</style>
