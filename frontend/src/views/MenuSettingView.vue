<template>
  <div>
    <phone-header></phone-header>
    <div class="top-setting-bar">
      <i
        @click="goBack"
        style="font-size: 20px; margin-left: 5px"
        class="xi-angle-left"
      ></i>
      <span style="margin-left: 5px; margin-right: 3px">앱 설정</span>
      <img style="width: 16px" src="../assets/down.png" />
    </div>
    <div class="menu-box">
      <div
        @click="pushLab"
        v-for="menus in setting_menus"
        class="menu"
        :key="menus.title"
      >
        <img
          style="margin-right: 10px; width: 53px; height: 53px"
          :src="menus.img"
        />
        <div
          style="
            text-align: left;
            width: 163px;
            display: flex;
            flex-direction: column;
            align-items: baseline;
          "
        >
          <p style="font-size: 13px; font-weight: 500">{{ menus.title }}</p>
          <p style="font-size: 10px; color: #8b8b8c">{{ menus.info }}</p>
        </div>
        <i
          style="font-size: 16px; position: relative; left: 50px"
          class="xi-angle-right"
        ></i>
      </div>
      <div style="height: 44px"></div>
    </div>
    <bottom-bar></bottom-bar>
  </div>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
import BottomBar from "@/components/BottomBar.vue";

export default {
  data() {
    return {
      setting_menus: [
        {
          img: require("../assets/setting-8.png"),
          title: "편의기능",
          info: "나만의 설정으로 알파를 더욱 편리하게 사용할 수 있습니다.",
        },
        {
          img: require("../assets/setting-1.png"),
          title: "알림",
          info: "중요한 정보를 놓치지 않도록 알림을 설정할 수 있습니다",
        },
        {
          img: require("../assets/setting-2.png"),
          title: "매매기능",
          info: "나만의 매매기능 설정으로 빠르고 편리하게 투자할 수 있습니다.",
        },
        {
          img: require("../assets/setting-3.png"),
          title: "로그인",
          info: "로그인 시간, 동시접속 등 로그인 관련한 설정을 변경할 수 있습니다.",
        },
        {
          img: require("../assets/setting-4.png"),
          title: "계좌",
          info: "대표계좌를 설정하고 계좌의 순서를 변경할 수 있습니다.",
        },
        {
          img: require("../assets/setting-5.png"),
          title: "앱 정보 및 초기화",
          info: "앱 정보를 확인하고 최신버전으로 업데이트 할 수 있습니다.",
        },
        {
          img: require("../assets/setting-6.png"),
          title: "Smart ARS 서비스 이용 동의",
          info: "음성과 화면을 함께 이용할 수 있는 서비스 입니다.",
        },
        {
          img: require("../assets/setting-7.png"),
          title: "알파랩 설정",
          info: "알파의 새로운 기능을 먼저 접하실 수 있습니다.",
        },
      ],
    };
  },
  components: {
    PhoneHeader,
    BottomBar,
  },
  methods: {
    pushLab() {
      this.$router.push("/alpha_lab");
    },
    goBack() {
      window.history.length > 1 ? this.$router.go(-1) : this.$router.push("/");
    },
  },
};
</script>

<style scoped>
.top-setting-bar {
  display: flex;
  justify-content: baseline;
  align-items: center;
  margin-top: 40px;
  width: 100%;
  height: 40px;
  text-align: left;
}

.menu {
  padding: 13px;
  display: flex;
  border-bottom: 1px solid #e3e4e6;
  align-items: center;
}
</style>
