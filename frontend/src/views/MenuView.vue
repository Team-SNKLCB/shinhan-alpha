<template>
    <easy-menu-view-vue v-if="e_active === true"></easy-menu-view-vue>
    <ordinary-menu-view-vue v-if="e_active === false"></ordinary-menu-view-vue>
</template>

<script>
import EasyMenuViewVue from "./EasyMenuView.vue";
import OrdinaryMenuViewVue from "./OrdinaryMenuView.vue";
export default {
    components: {
        EasyMenuViewVue,
        OrdinaryMenuViewVue,
    },
    computed: {
        e_active() {
            return this.$store.state.e_active;
        },
    },
};
</script>

<style></style>
