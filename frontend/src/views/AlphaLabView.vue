<template>
    <phone-header></phone-header>
    <div class="top-lab-bar">
        <span style="font-size: 14px">알파랩 설정</span>
        <router-link to="/menu_setting"><i class="xi-close"></i></router-link>
    </div>
    <hr />
    <div style="padding-bottom: 10px"><img style="width: 300px" src="../assets/alpha_lab.png" /></div>
    <hr />
    <div class="alpha-menu-div">
        <div class="alpha-menu">
            <div style="width: 195px; display: flex; flex-direction: column; text-align: left; margin-left: 25px; font-size: 14px">
                <p>주린이 모드</p>
                <p style="font-size: 10px; color: #8b8b8c">주식 입문자에게 투자가 조금 더 쉽게 다가올 수 있도록 할 수 있는 주린이 모드가 활성화 됩니다.</p>
            </div>
            <img v-if="save_toggle[0] === false" @click="changeToggle(0)" style="width: 70px; height: 35px; margin-left: 20px" src="../assets/off-btn.png" />
            <img v-else-if="save_toggle[0] === true" @click="changeToggle(0)" style="width: 70px; height: 35px; margin-left: 20px" src="../assets/on-btn.png" />
        </div>
        <div class="alpha-menu">
            <div style="width: 195px; display: flex; flex-direction: column; text-align: left; margin-left: 25px; font-size: 14px">
                <p>글자 크게 보기</p>
                <p style="font-size: 10px; color: #8b8b8c">모든 화면의 글자를 크게 볼 수 있습니다.</p>
            </div>
            <img v-if="save_toggle[1] === false" @click="changeToggle(1)" style="width: 70px; height: 35px; margin-left: 20px" src="../assets/off-btn.png" />
            <img v-else-if="save_toggle[1] === true" @click="changeToggle(1)" style="width: 70px; height: 35px; margin-left: 20px" src="../assets/on-btn.png" />
        </div>
        <div class="alpha-menu">
            <div style="width: 195px; display: flex; flex-direction: column; text-align: left; margin-left: 25px; font-size: 14px">
                <p>흔들기 기능</p>
                <p style="font-size: 10px; color: #8b8b8c">알파를 실행하고 휴대폰을 흔들면 설정한 흔들기 기능이 실행됩니다.</p>
            </div>
            <img v-if="save_toggle[2] === false" @click="changeToggle(2)" style="width: 70px; height: 35px; margin-left: 20px" src="../assets/off-btn.png" />
            <img v-else-if="save_toggle[2] === true" @click="changeToggle(2)" style="width: 70px; height: 35px; margin-left: 20px" src="../assets/on-btn.png" />
        </div>
        <div class="alpha-menu">
            <div style="width: 195px; display: flex; flex-direction: column; text-align: left; margin-left: 25px; font-size: 14px">
                <p>햅틱 기능</p>
                <p style="font-size: 10px; color: #8b8b8c">키패드와 증감버튼 터치시 햅틱 기능이 작동됩니다.</p>
            </div>
            <img v-if="save_toggle[3] === false" @click="changeToggle(3)" style="width: 70px; height: 35px; margin-left: 20px" src="../assets/off-btn.png" />
            <img v-else-if="save_toggle[3] === true" @click="changeToggle(3)" style="width: 70px; height: 35px; margin-left: 20px" src="../assets/on-btn.png" />
        </div>
    </div>
    <div style="display: flex; justify-content: space-around; margin-top: 10px">
        <router-link to="/menu_setting"><div class="cancel-btn">취소</div></router-link>
        <router-link to="/easy_menu"><div class="save-btn">저장</div></router-link>
    </div>
    <bottom-bar></bottom-bar>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
import BottomBar from "@/components/BottomBar.vue";
export default {
    data() {
        return {
            save_toggle: [false, false, false, false],
        };
    },
    components: { PhoneHeader, BottomBar },
    methods: {
        changeToggle(index) {
            this.save_toggle[index] = !this.save_toggle[index];
        },
    },
};
</script>

<style>
.top-lab-bar {
    margin-top: 40px;
    margin-left: 10px;
    margin-right: 10px;
    height: 30px;
    display: flex;
    justify-content: space-between;
}

hr {
    margin-top: 0;
    margin-bottom: 0;
}

.alpha-menu {
    width: 100%;
    display: flex;
    align-items: center;
    padding-top: 8px;
    padding-bottom: 8px;
    border-bottom: 1px solid #e3e2de;
}

.cancel-btn {
    width: 99px;
    height: 42px;
    color: white;
    background-color: #979797;
    border-radius: 8px;
    line-height: 42px;
}

.save-btn {
    width: 165px;
    height: 42px;
    color: white;
    background-color: #4276f2;
    border-radius: 8px;
    line-height: 42px;
}
i {
    color: black;
}
</style>
