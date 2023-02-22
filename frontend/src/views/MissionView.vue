<template>
  <div>
    <phone-header></phone-header>
    <div class="top-background">
      <router-link to="/tier_main"
        ><font-awesome-icon
          style="
            position: absolute;
            left: 15;
            top: 58;
            font-size: 20px;
            color: white;
          "
          icon="fa-solid fa-chevron-left"
      /></router-link>
      <div class="title-div">
        <p>
          <span style="color: white">{{ userDetail.name }}</span> 님은
        </p>
        <p>
          <span style="color: gold">골드</span>
          <span style="color: white">가는중 !</span>
        </p>
      </div>
      <div class="info-div">
        <p>
          신규 미션을 진행하고<br />
          포인트를 얻어보세요 !
        </p>
        <p style="margin-top: 20px">
          다음 등급까지
          <span style="color: rgba(53, 78, 242, 0.9)">152P</span> 남았어요.
        </p>
      </div>
    </div>
    <div id="mission-div">
      <div
        class="mission-list"
        v-for="(mission, i) in missions"
        :key="mission.mission_name"
      >
        <p class="mission-title">{{ mission.mission_name }}</p>
        <p class="mission-info">{{ mission.mission_description }}</p>
        <div
          style="
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 30px;
          "
        >
          <div class="mission-point">{{ mission.mission_point }}P</div>
          <img
            v-if="mission.flag === 1"
            style="width: 44px; height: 44px"
            src="../assets/mission-ing.png"
          />
          <img
            v-else-if="mission.flag === 2"
            style="width: 44px; height: 44px"
            @click="changeStatus(i)"
            src="../assets/mission-end.png"
          />
          <div style="position: relative" v-else-if="mission.flag === 3">
            <img
              style="width: 44px; height: 44px"
              src="../assets/mission-completed.png"
            />
            <img
              style="
                width: 80px;
                height: 60px;
                position: absolute;
                left: -15px;
                bottom: 0px;
              "
              src="../assets/complete_stamp.png"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
export default {
  data() {
    return {
      // missions: [
      //   {
      //     mission_title: "1주일 연속 로그인하기",
      //     mission_info:
      //       "주식의 기본은 꾸준함 ! 1주일 연속 신한알파에 로그인해보세요.",
      //     mission_point: 500,
      //     mission_flag: 3,
      //   },
      //   {
      //     mission_title: "국내주식 1주 구매하기",
      //     mission_info:
      //       "‘국내주식-신한인기종목’에서 인기종목 확인하고 ‘주식매매-종목검색’에서 종목 검색한 뒤 주식을 1주이상 구매해보세요 !",
      //     mission_point: 500,
      //     mission_flag: 2,
      //   },
      //   {
      //     mission_title: "공모주 신청하기",
      //     mission_info:
      //       "새로 주식 시장에 들어오는 주식을 확인해요! ‘뱅킹/공모주-권리/공모주’에서 원하는 공모주를 선택하고 신청해보세요!",
      //     mission_point: 300,
      //     mission_flag: 1,
      //   },
      // ],
    };
  },
  methods: {
    changeStatus(index) {
      missions[index].mission_flag = 3;
    },
  },
  components: {
    PhoneHeader,
  },
  computed: {
    missions() {
      return this.$store.state.missionList;
    },
    userDetail() {
      return this.$store.state.userDetail;
    },
  },
  created() {
    this.$store.dispatch("GET_MISSION_LIST");
    this.$store.dispatch("GET_USER_DETAIL");
  },
};
</script>

<style scoped>
.top-background {
  margin-top: 40px;
  background: rgba(53, 78, 242, 0.9);
  height: 180px;
}

.title-div {
  color: black;
  margin-top: 15px;
  font-size: 24px;
  font-weight: 600;
  padding-top: 10px;
}

.info-div {
  color: black;
  margin: 0 auto;
  margin-top: 15px;
  box-shadow: 2px 2px 4px 1px rgba(0, 0, 0, 0.25);
  width: 284px;
  height: 140px;
  border-radius: 13px;
  background: #ffffff;
  padding-top: 20px;
  box-sizing: border-box;
  font-weight: 600;
}

#mission-div {
  margin-top: 75px;
  margin-bottom: 30px;
  text-align: left;
}

.mission-list {
  width: 284px;
  box-shadow: 2px 2px 4px 1px rgba(0, 0, 0, 0.25);
  background: #ffffff;
  border-radius: 13px;
  margin: 0 auto;
  margin-bottom: 20px;
  padding: 24px;
  box-sizing: border-box;
}

.mission-title {
  font-weight: 700;
  font-size: 16px;
}

.mission-info {
  font-weight: 400;
  font-size: 10px;
  color: #979797;
}

.mission-point {
  font-family: "Inter", sans-serif;
  text-align: center;
  width: 67px;
  height: 22px;
  background: rgba(129, 66, 227, 0.2);
  border-radius: 10px;
  font-size: 12px;
  line-height: 22px;
}
</style>
