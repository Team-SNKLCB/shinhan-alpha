<template>
  <div>
    <phone-header></phone-header>
    <div style="position: absolute; top: 37px">
      <img
        style="width: 320px; margin-left: 2px"
        src="../assets/stock_top.png"
      />
      <div style="display: flex">
        <img
          style="width: 120px; position: absolute; left: 0px"
          src="../assets/stock_bottom.png"
        />
        <img
          style="width: 200px; position: absolute; right: 0px"
          src="../assets/stock_bottom2.png"
        />
        <div
          style="
            background-color: #f8f8f8;
            position: absolute;
            width: 180px;
            height: 50px;
            right: 13px;
            top: 320px;
            z-index: 3;
            border-radius: 10px;
          "
        ></div>
        <div
          style="
            background-color: #f8f8f8;
            position: absolute;
            width: 180px;
            height: 50px;
            right: 13px;
            top: 380px;
            z-index: 3;
            border-radius: 10px;
          "
        ></div>
      </div>
      <font-awesome-icon
        icon="fa-soild fa-chevron-left"
        @click="goBack"
        class="back_stock"
      />
    </div>
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
.back_stock {
  position: absolute;
  left: 9px;
  top: 12px;
}
</style>
