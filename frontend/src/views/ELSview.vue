<template>
  <div>
    <phone-header></phone-header>
    <img
      @click="goBack"
      style="position: absolute; margin-top: 40px"
      src="../assets/X.png"
    />
    <img style="width: 320px" src="../assets/ELS.png" />
    <div class="check_box">
      <span style="color: white; font-size: 20px; font-weight: bold"
        >네,좋아요!</span
      >
    </div>
  </div>
</template>
<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
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
.check_box {
  background-color: #354ef2;
  width: 291px;
  height: 63px;
  position: absolute;
  border-radius: 6px;
  margin-top: 14px;
  line-height: 63px;
  left: 14px;
}
</style>
