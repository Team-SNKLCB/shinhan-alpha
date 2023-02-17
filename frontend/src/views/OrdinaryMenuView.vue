<template>
    <phone-header></phone-header>
    <img class="ord-menu" src="../assets/ordinary-menu.png" />
    <bottom-bar></bottom-bar>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
import BottomBar from "@/components/BottomBar.vue";
export default {
    components: {
        PhoneHeader,
        BottomBar,
    },
};
</script>

<style>
.ord-menu {
    margin-top: 40px;
    margin-bottom: 45px;
    width: 300px;
}
</style>
