<template>
    <phone-header></phone-header>
    <div style="margin-top: 40px">
        <img id="img_move" src="../assets/tier_degree.png" />
    </div>
    <div v-if="user_click === true" id="item">
        <!--검회-->
        <div class="box_text"><p>포인트 획득 내역</p></div>
        <div @click="user_click = false" class="box_text" style="color: #979797">
            <p>리워드 수령하기</p>
        </div>
    </div>
    <div v-if="user_click === true" v-for="(a, i) in index" class="point_check" :key="i">
        <div class="box_text_point_title">
            <p>출석체크</p>
            <br />
            <p class="point_time">2023.02.16 16:30:12</p>
        </div>
        <div>
            <p>+30P</p>
        </div>
    </div>
    <div v-if="user_click === false" id="item">
        <!-- 회검 -->
        <div @click="user_click = true" class="box_text" style="color: #979797">
            <p>포인트 획득 내역</p>
        </div>
        <div class="box_text"><p>리워드 수령하기</p></div>
    </div>
    <div v-if="user_click === false" class="point_check">
        <div class="tier_reward">
            <p style="font-weight: bold; font-size: 16px">브론즈 달성</p>
            <br />
            <p style="font-weight: bold; font-size: 11px; color: #979797">국내 주식 랜덤 1주</p>
        </div>
        <div><p class="take_text_clear">수령완료</p></div>
    </div>

    <div v-if="user_click === false && take_click === true" class="point_check">
        <div class="tier_reward">
            <p style="font-weight: bold; font-size: 16px">실버 달성</p>
            <br />
            <p style="font-weight: bold; font-size: 11px; color: #979797">수수료 우대</p>
        </div>
        <div @click="take_click = false">
            <p class="take_text_done">수령하기</p>
        </div>
    </div>
    <div v-if="user_click === false && take_click === false" class="point_check">
        <div class="tier_reward">
            <p style="font-weight: bold; font-size: 16px">실버 달성</p>
            <br />
            <p style="font-weight: bold; font-size: 11px; color: #979797">수수료 우대</p>
        </div>
        <div>
            <p class="take_text_clear">수령완료</p>
        </div>
    </div>

    <div v-if="user_click === false" class="point_check">
        <div class="tier_reward">
            <p style="font-weight: bold; font-size: 16px">골드 달성</p>
            <br />
            <p style="font-weight: bold; font-size: 11px; color: #979797">수수료 우대</p>
        </div>
        <div><p class="take_text_yet">미달성</p></div>
    </div>
    <div v-if="user_click === false" class="point_check">
        <div class="tier_reward">
            <p style="font-weight: bold; font-size: 16px">플레티넘 달성</p>
            <br />
            <p style="font-weight: bold; font-size: 11px; color: #979797">신한 플러스 3개월 할인</p>
        </div>
        <div><p class="take_text_yet">미달성</p></div>
    </div>
    <div v-if="user_click === false" class="point_check">
        <div class="tier_reward">
            <p style="font-weight: bold; font-size: 16px">다이아 달성</p>
            <br />
            <p style="font-weight: bold; font-size: 11px; color: #979797">국내 주식 랜덤 1주</p>
        </div>
        <div><p class="take_text_yet">미달성</p></div>
    </div>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
export default {
    components: { PhoneHeader },
    data() {
        return {
            user_click: true,
            take_click: true,
            index: ["a", "b", "c"],
        };
    },
};
</script>
<style>
.img_move {
    width: 320px;
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
    height: 20px;
    width: 60px;
}

.take_text_done {
    padding: 5px;
    background-color: #4276f2;
    border-radius: 11px;
    font-size: 12px;
    font-weight: bold;
    color: white;
    height: 20px;
    width: 60px;
}

.take_text_yet {
    padding: 5px;
    background-color: #979797;
    border-radius: 11px;
    font-size: 12px;
    font-weight: bold;
    color: white;
    height: 20px;
    width: 60px;
}

.tier_reward {
    padding: 3px;
    line-height: 10px;
    text-align: left;
}
</style>
