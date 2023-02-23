<template>
    <div>
        <phone-header></phone-header>
        <div class="top-background">
            <router-link to="/tier_main"
                ><font-awesome-icon style="position: absolute; left: 15; top: 58; font-size: 20px; color: white" icon="fa-solid fa-chevron-left"
            /></router-link>
            <div class="title-div">
                <p>
                    <span style="color: white">{{ userDetail.name }}</span> 님은
                </p>
                <p>
                    <span :style="{ color: tier ? tier[Number(userDetail.tier)].color : white }">{{ tier[Number(userDetail.tier)].tier }}</span>
                    <span style="color: white"> 가는중 !</span>
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
            <div v-for="mission in missions" :key="mission.mission_name">
                <div class="mission-list" v-if="mission.flag !== 0">
                    <p class="mission-title">{{ mission.mission_name }}</p>
                    <p class="mission-info">{{ mission.mission_description }}</p>
                    <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 30px">
                        <div class="mission-point">{{ mission.mission_point }}P</div>
                        <img v-if="mission.flag === 1" style="width: 44px; height: 44px" src="../assets/mission-ing.png" />
                        <img v-else-if="mission.flag === 2" style="width: 44px; height: 44px" @click="changeStatus(mission.id)" src="../assets/mission-end.png" />
                        <div style="position: relative" v-else-if="mission.flag === 3">
                            <img style="width: 44px; height: 44px" src="../assets/mission-completed.png" />
                            <img style="width: 80px; height: 60px; position: absolute; left: -15px; bottom: 0px" src="../assets/complete_stamp.png" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
import axios from "axios";
export default {
    data() {
        return {};
    },
    methods: {
        changeStatus(index) {
            axios.put(
                "http://localhost:8000/api/user/mission",
                {
                    id: index,
                    flag: 2,
                },
                {
                    headers: {
                        Authorization: "JWT " + sessionStorage.getItem("accessToken"),
                    },
                }
            );
        },
    },
    components: {
        PhoneHeader,
    },
    computed: {
        missions() {
            return this.$store.state.userMissionList;
        },
        userDetail() {
            return this.$store.state.userDetail;
        },
        tier() {
            return this.$store.state.checkTier;
        },
    },
    beforeMount() {
        this.$store.dispatch("GET_USER_MISSION");
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
