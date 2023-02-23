<template>
    <phone-header></phone-header>
    <img
        style="margin-top: 40px"
        src="../assets/app-icon/MMF-next.svg"
        @click="
            () => {
                this.$router.push('/menu');
            }
        "
    />
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
export default {
    components: { PhoneHeader },
};
</script>

<style></style>
