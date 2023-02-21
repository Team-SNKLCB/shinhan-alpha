<template>
    <img id="splash" src="../assets/splash.png" />
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
export default {
    components: { PhoneHeader },
    created() {
        setTimeout(() => {
            this.$router.push("/mode_select");
        }, 3000);
    },
};
</script>

<style>
#splash {
    height: 668px;
    width: 320px;
}
</style>
