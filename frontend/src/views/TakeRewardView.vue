<template>
  <div>
    <div v-if="take_click === true" class="overlay">
      <div class="popup">
        <div class="back">
          <font-awesome-icon icon="fa-solid fa-x" @click="take_click = false" />
        </div>
        <br />

        <img src="../assets/silver_modal.png" /><br />
        <p style="font-size: 18px; font-weight: bold">
          <span style="color: #979797">실버</span> 달성을 축하합니다!
        </p>

        <p style="font-size: 20px; font-weight: bold">
          주식거래 수수료 우대 혜택
        </p>
      </div>
    </div>
    <phone-header></phone-header>
    <div class="back_page">
      <font-awesome-icon icon="fa-soild fa-chevron-left" @click="goBack" />
    </div>
    <div class="tier_degree" style="margin-top: 40px">
      <div
        v-if="user_tier === 0"
        class="progress gage"
        role="progressbar"
        aria-label="Animated striped example"
        aria-valuenow="20"
        aria-valuemin="0"
        aria-valuemax="100"
      >
        <div
          class="progress-bar progress-bar-striped progress-bar-animated"
          style="width: 20%"
        ></div>
      </div>
      <div
        v-if="user_tier === 1"
        class="progress gage"
        role="progressbar"
        aria-label="Animated striped example"
        aria-valuenow="40"
        aria-valuemin="0"
        aria-valuemax="100"
      >
        <div
          class="progress-bar progress-bar-striped progress-bar-animated"
          style="width: 40%"
        ></div>
      </div>
      <div
        v-if="user_tier === 2"
        class="progress gage"
        role="progressbar"
        aria-label="Animated striped example"
        aria-valuenow="60"
        aria-valuemin="0"
        aria-valuemax="100"
      >
        <div
          class="progress-bar progress-bar-striped progress-bar-animated"
          style="width: 60%"
        ></div>
      </div>
      <div
        v-if="user_tier === 3"
        class="progress gage"
        role="progressbar"
        aria-label="Animated striped example"
        aria-valuenow="80"
        aria-valuemin="0"
        aria-valuemax="100"
      >
        <div
          class="progress-bar progress-bar-striped progress-bar-animated"
          style="width: 80%"
        ></div>
      </div>
      <div
        v-if="user_tier === 4"
        class="progress gage"
        role="progressbar"
        aria-label="Animated striped example"
        aria-valuenow="100"
        aria-valuemin="0"
        aria-valuemax="100"
      >
        <div
          class="progress-bar progress-bar-striped progress-bar-animated"
          style="width: 100%"
        ></div>
      </div>
      <img class="bronze_star" src="../assets/bronze_star.png" />
      <img class="silver_star" src="../assets/silver_star.png" />
      <img class="gold_star" src="../assets/gold_star.png" />
      <img class="platinum_star" src="../assets/platinum_star.png" />
      <img class="dia_star" src="../assets/dia_star.png" />
      <img
        v-if="user_tier === 0"
        class="bronze_bear"
        src="../assets/tier_bear.png"
      />
      <img
        v-if="user_tier === 1"
        class="silver_bear"
        src="../assets/tier_bear.png"
      />
      <img
        v-if="user_tier === 2"
        class="gold_bear"
        src="../assets/tier_bear.png"
      />
      <img
        v-if="user_tier === 3"
        class="platinum_bear"
        src="../assets/tier_bear.png"
      />
      <img
        v-if="user_tier === 4"
        class="dia_bear"
        src="../assets/tier_bear.png"
      />
    </div>
    <div v-if="user_click === true" id="item">
      <!--검회-->
      <div class="box_text"><p>포인트 획득 내역</p></div>
      <div @click="user_click = false" class="box_text" style="color: #979797">
        <p>리워드 수령하기</p>
      </div>
    </div>
    <div v-if="user_click">
      <div v-for="(a, i) in index" class="point_check" :key="i">
        <div class="box_text_point_title">
          <p>출석체크</p>
          <br />
          <p class="point_time">2023.02.16 16:30:12</p>
        </div>
        <div>
          <p>+30P</p>
        </div>
      </div>
    </div>
    <div v-if="user_click === false" id="item">
      <!-- 회검 -->
      <div @click="user_click = true" class="box_text" style="color: #979797">
        <p>포인트 획득 내역</p>
      </div>
      <div class="box_text"><p>리워드 수령하기</p></div>
    </div>
    <template v-if="user_click === false">
      <div v-for="(rewards, i) in rewards" :key="i" class="point_check">
        <div class="tier_reward">
          <p style="font-weight: bold; font-size: 16px">
            {{ rewards.reward_title }}
          </p>
          <br />
          <p style="font-weight: bold; font-size: 11px; color: #979797">
            {{ rewards.reward_info }}
          </p>
        </div>
        <div v-if="rewards.reward_flag === 0">
          <p class="take_text_yet">미달성</p>
        </div>
        <div
          v-else-if="rewards.reward_flag === 1"
          @click="(rewards.reward_flag = 2), (take_click = true)"
        >
          <p class="take_text_done">수령하기</p>
        </div>
        <div v-else-if="rewards.reward_flag === 2">
          <p class="take_text_clear">수령완료</p>
        </div>
      </div>
    </template>
  </div>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
export default {
  components: { PhoneHeader },
  data() {
    return {
      user_click: true,
      take_click: false,
      index: ["a", "b", "c"],
      user_tier: 1,
      rewards: [
        {
          reward_title: "브론즈 달성",
          reward_info: "국내 주식 랜덤 1주",
          reward_flag: 2,
        },
        {
          reward_title: "실버 달성",
          reward_info: "수수료 우대",
          reward_flag: 1,
        },
        {
          reward_title: "골드 달성",
          reward_info: "수수료 우대",
          reward_flag: 0,
        },
        {
          reward_title: "플레티넘 달성",
          reward_info: "신한 플러스 3개월 할인",
          reward_flag: 0,
        },
        {
          reward_title: "다이아 달성",
          reward_info: "국내 주식 랜덤 1주",
          reward_flag: 0,
        },
      ],
    };
  },
  methods: {
    goBack() {
      window.history.length > 1 ? this.$router.go(-1) : this.$router.push("/");
    },
  },
};
</script>
<style>
.img_move {
  width: 320px;
  position: relative;
}

#item {
  display: flex;
}

.box_text {
  display: flex;
  justify-content: center;
  align-items: center;
  border-bottom: 1px solid;
  font-size: 12px;
  font-weight: bold;
  text-align: center;
  width: 160px;
  height: 47px;
}

li {
  list-style: none;
}

.point_check {
  display: flex;
  border-bottom: 1px solid #979797;
  justify-content: space-between;
  align-items: center;
  padding: 10px 15px;
}

.point_time {
  font-size: 8px;
  font-weight: bold;
  color: #979797;
}

.box_text_point_title {
  line-height: 10px;
  text-align: left;
}

.take_text_clear {
  padding: 5px;
  background-color: #c15bff;
  border-radius: 11px;
  font-size: 12px;
  font-weight: bold;
  color: white;
  height: 30px;
  width: 60px;
}

.take_text_done {
  padding: 5px;
  background-color: #4276f2;
  border-radius: 11px;
  font-size: 12px;
  font-weight: bold;
  color: white;
  height: 30px;
  width: 60px;
}

.take_text_yet {
  padding: 5px;
  background-color: #979797;
  border-radius: 11px;
  font-size: 12px;
  font-weight: bold;
  color: white;
  height: 30px;
  width: 60px;
}

.tier_reward {
  padding: 3px;
  line-height: 10px;
  text-align: left;
}
#silver_modal {
  position: absolute;
  top: 150px;
  left: 20px;
  height: 271px;
  width: 280px;
  background-color: white;
  border-radius: 28px;
}

.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
}

.overlay .popup {
  background: white;
  border-radius: 15px;
  padding: 20px;
  height: 260px;
  width: 260px;
}

.back {
  text-align: left;
}
.back_page {
  margin-top: 40px;
  text-align: left;
  margin-left: 10px;
}
.gage {
  width: 233px;
  position: absolute;
  left: 42px;
  top: 150px;
}
.tier_degree {
  width: 320px;
  height: 154px;
}
.bronze_star {
  position: absolute;
  left: 71px;
  top: 170px;
}
.silver_star {
  position: absolute;
  left: 117.5px;
  top: 167px;
}
.gold_star {
  position: absolute;
  left: 167px;
  top: 167px;
}
.platinum_star {
  position: absolute;
  left: 211px;
  top: 165px;
}
.dia_star {
  position: absolute;
  left: 256px;
  top: 165px;
}
.silver_bear {
  position: absolute;
  left: 105px;
  top: 90px;
}
.bronze_bear {
  position: absolute;
  left: 60px;
  top: 90px;
}
.gold_bear {
  position: absolute;
  left: 153px;
  top: 90px;
}
.platinum_bear {
  position: absolute;
  left: 198px;
  top: 90px;
}
.dia_bear {
  position: absolute;
  left: 245px;
  top: 90px;
}
</style>
