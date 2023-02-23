<template>
    <div>
        <phone-header></phone-header>
        <div class="x-btn">
            <router-link to="easy_menu"><font-awesome-icon icon="fa-solid fa-x" /></router-link>
        </div>
        <div class="tier-head">
            <div style="position: relative">
                <img id="tier-image" :src="tier[0].tier_image" />
                <div id="tier-descript">
                    <p>나의 티어는?</p>
                    <span class="my-tier" :style="{ color: tiers[userDetail.tier].color }">{{ tiers[userDetail.tier].tier }}</span>
                </div>
                <ve-progress :process="[-100, 100]" id="point-bar" color="#354EF2" empty-color="#F1F1F1" :thickness="border" empty-thickness="5%" :progress="points" :size="300">
                </ve-progress>
            </div>
            <div id="link-btn-div">
                <router-link to="/take_reward"
                    ><div class="link-btn">리워드 <br />수령하기</div></router-link
                >
                <router-link to="/mission" class="link-btn"><div>미션 확인</div></router-link>
                <router-link to="/mission"
                    ><div class="link-btn">내 자산 <br />확인하기</div></router-link
                >
                <router-link to="/invite"
                    ><div class="link-btn">친구 <br />추천하기</div></router-link
                >
            </div>
        </div>
    </div>
    <div style="height: 10px; background-color: #f0f0f0"></div>
    <div id="tier-reward-descript">
        <div class="reward-descript-div" v-for="item in tier" :key="item.tier">
            <img class="tier-reward-img" :src="item.tier_image" />
            <div class="tier-reward-descript">
                <strong
                    ><p style="font-size: 11px">{{ item.tier }}</p></strong
                >
                <p style="font-size: 8px; color: #cccccc">{{ item.tier_reward }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
import "vue3-circle-progress/dist/circle-progress.css";
import CircleProgress from "vue3-circle-progress";
import { veProgress } from "vue-ellipse-progress";
export default {
    data() {
        return {
            tier: [
                {
                    tier: "브론즈",
                    tier_reward: "국내 주식 랜덤 1주",
                    tier_image: require("../assets/tier/tier_bronze_img.png"),
                },
                {
                    tier: "실버",
                    tier_reward: "수수료 우대",
                    tier_image: require("../assets/tier/tier_silver_img.png"),
                },
                {
                    tier: "골드",
                    tier_reward: "수수료 우대",
                    tier_image: require("../assets/tier/tier_gold_img.png"),
                },
                {
                    tier: "플래티넘",
                    tier_reward: "신한플러스 3개월 할인",
                    tier_image: require("../assets/tier/tier_platinum_img.png"),
                },
                {
                    tier: "다이아",
                    tier_reward: "해외 주식 랜덤 1주",
                    tier_image: require("../assets/tier/tier_dia_img.png"),
                },
            ],
        };
    },
    components: {
        PhoneHeader,
        CircleProgress,
        veProgress,
    },

    computed: {
        userDetail() {
            return this.$store.state.userDetail;
        },
        tiers() {
            return this.$store.state.checkTier;
        },
        points() {
            return this.$store.state.total_point;
        },
    },
    created() {
        this.$store.dispatch("GET_USER_DETAIL");
        this.$store.dispatch("GET_USER_TOTAL_POINT");
    },
};
</script>

<style scoped>
#point-bar {
    width: 300px;
    height: 300px;
    position: absolute;
    top: 33px;
    right: 10.5px;
    z-index: -1;
}
.x-btn {
    margin-top: 40px;
    height: 30px;
    line-height: 30px;
    text-align: left;
    margin-left: 15px;
    font-size: 20px;
}

.tier-head {
    width: 100%;
    height: 500px;
}

#tier-image {
    margin-top: 65px;
}

#tier-descript {
    font-family: "Noto Sans KR";
    margin-top: 35px;
    font-size: 14px;
}

#link-btn-div {
    display: flex;
    justify-content: space-between;
    margin: 0 41px;
    margin-top: 60px;
}

.link-btn {
    color: white;
    font-family: "Noto Sans KR";
    font-weight: 400;
    width: 45px;
    height: 45px;
    border-radius: 5px;
    background-color: #354ef2;
    font-size: 9px;
    padding-top: 6px;
    box-sizing: border-box;
}

.link-btn:nth-child(2) {
    padding: 0;
    line-height: 45px;
}

.my-tier {
    font-size: 26px;
    font-weight: 600;
}

.tier-reward-img {
    width: 65px;
}

.reward-descript-div {
    padding: 10px;
    display: flex;
    align-items: center;
}

.tier-reward-descript {
    margin-left: 15px;
    text-align: left;
    line-height: 25px;
}
a {
    text-decoration: none;
    color: black;
}
</style>
