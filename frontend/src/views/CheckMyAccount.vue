<template>
  <div>
    <phone-header></phone-header>
    <div
      class="back_page"
      style="display: flex; align-items: center; justify-content: space-between"
    >
      <div>
        <font-awesome-icon icon="fa-soild fa-chevron-left" @click="goBack" />
        <span style="font-size: 14px"> 전계좌현황 </span>
        <img style="height: 13px; width: 13px" src="../assets/down.png" />
      </div>
      <div style="display: flex; margin-right: 10px">
        <div class="account_box">
          <p style="font-size: 10px; color: white">총자산현황</p>
        </div>
        <img style="width: 30px; height: 30px" src="../assets/more.png" />
      </div>
    </div>
    <img style="width: 320px" src="../assets/account.png" />
    <div>
      <bottom-bar></bottom-bar>
    </div>
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
<style scoped>
.account_box {
  display: flex;
  padding: 10px;
  background-color: black;
  border-radius: 10px;
}
</style>
