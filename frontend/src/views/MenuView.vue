<template>
    <easy-menu-view-vue v-if="e_activate === true"></easy-menu-view-vue>
    <ordinary-menu-view-vue v-if="e_activate === false"></ordinary-menu-view-vue>
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
        e_activate() {
            return this.$store.state.e_activate;
        },
    },

    created() {
        this.$store.dispatch("CHANGE_MODE");
    },
};
</script>

<style></style>
