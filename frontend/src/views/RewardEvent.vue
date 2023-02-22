<template>
  <div>
    <phone-header></phone-header>

    <img
      style="width: 320px; margin-top: 40px; position: relative"
      src="../assets/reward_bronze.png"
    />
    <img @click="goBack" class="back_x" src="../assets/X.png" />
  </div>
</template>
<script>
import PhoneHeader from "../components/PhoneHeader.vue";

export default {
  components: { PhoneHeader },

  methods: {
    goBack() {
      window.history.length > 1 ? this.$router.go(-1) : this.$router.push("/");
    },
  },
};
</script>
<style scoped>
.back_x {
  position: absolute;
  z-index: 3;
  top: 50px;
  left: 10px;
}
</style>
