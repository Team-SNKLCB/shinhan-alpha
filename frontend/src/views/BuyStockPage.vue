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
        <div class="up_bar">
          <img
            @click="add_stock"
            style="position: absolute; right: 10px; top: 15px"
            src="../assets/plus.png"
          />
          <img
            @click="sub_stock"
            style="position: absolute; left: 10px; top: 15px"
            src="../assets/minus.png"
          />
          <span
            style="
              position: absolute;
              top: 13px;
              font-size: 18px;
              font-weight: bold;
              right: 85px;
            "
            >{{ stock_num }} </span
          ><span
            style="position: absolute; top: 20px; font-size: 10px; right: 75px"
            >주</span
          >
        </div>
        <div class="down_bar">
          <img
            @click="add_prize"
            style="position: absolute; right: 10px; top: 15px"
            src="../assets/plus.png"
          />
          <img
            @click="sub_prize"
            style="position: absolute; left: 10px; top: 15px"
            src="../assets/minus.png"
          />
          <span
            style="
              position: absolute;
              top: 13px;
              font-size: 18px;
              font-weight: bold;
              right: 60px;
            "
            >{{ stock_prize }} </span
          ><span
            style="position: absolute; top: 20px; font-size: 10px; right: 50px"
            >원</span
          >
        </div>
      </div>
      <div class="prize_bar">
        <div>
          <p style="font-size: 9px; font-weight: bold">쿠폰선택</p>
          <p style="font-size: 9px; font-weight: bold; color: #979797">
            주문금액
          </p>
        </div>
      </div>
      <div class="now_prize">
        <span style="font-weight: bold">{{ stock_sum }}</span>
        <span style="font-size: 13px"> 원</span>
      </div>
      <font-awesome-icon
        icon="fa-soild fa-chevron-left"
        @click="goBack"
        class="back_stock"
      />
    </div>
    <div class="buy_bar">
      <span
        style="
          color: white;
          position: absolute;
          right: 59px;
          top: 3px;
          font-weight: bold;
        "
        >현금매수</span
      >
    </div>
  </div>
</template>
<script>
import PhoneHeader from "../components/PhoneHeader.vue";

export default {
  components: { PhoneHeader },
  data() {
    return {
      stock_num: 0,
      stock_sum: 0,
      stock_prize: 121100,
    };
  },
  methods: {
    goBack() {
      window.history.length > 1 ? this.$router.go(-1) : this.$router.push("/");
    },
    add_stock() {
      this.stock_num += 1;
      this.stock_sum += this.stock_prize;
    },
    sub_stock() {
      if (this.stock_num > 0) {
        this.stock_num -= 1;
      }
      this.stock_sum -= this.stock_prize;
    },
    add_prize() {
      this.stock_prize += 100;
    },
    sub_prize() {
      if (this.stock_prize > 0) {
        this.stock_prize -= 100;
      }
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
.up_bar {
  background-color: #f8f8f8;
  position: absolute;
  width: 180px;
  height: 50px;
  right: 13px;
  top: 320px;
  z-index: 3;
  border-radius: 10px;
}
.down_bar {
  background-color: #f8f8f8;
  position: absolute;
  width: 180px;
  height: 50px;
  right: 13px;
  top: 380px;
  z-index: 3;
  border-radius: 10px;
}
.prize_bar {
  display: flex;
  position: absolute;
  right: 150px;
  top: 500px;
}
.now_prize {
  position: absolute;
  right: 15px;
  top: 508px;
}
.buy_bar {
  height: 34px;
  width: 179px;
  position: absolute;
  background-color: red;
  border-radius: 3px;
  top: 575px;
  right: 12px;
}
</style>
