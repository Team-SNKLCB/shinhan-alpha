<template>
  <phone-header></phone-header>
  <div class="back_page" style="display: flex; align-items: center">
    <font-awesome-icon icon="fa-soild fa-chevron-left" @click="goBack" />
    <p style="font-size: 14px">신한인기종목</p>
    <img style="height: 13px; width: 13x" src="../assets/down.png" />
  </div>
  <div>
    <img style="width: 320px" src="../assets/page1.png" />
  </div>
  <div>
    <bottom-bar></bottom-bar>
  </div>
</template>
<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
import BottomBar from "@/components/BottomBar.vue";
export default {
  components: { PhoneHeader, BottomBar },
  methods: {
    goBack() {
      window.history.length > 1 ? this.$router.go(-1) : this.$router.push("/");
    },
  },
};
</script>
<style scoped></style>
