<template>
    <phone-header></phone-header>
    <div class="top-bar">
        <router-link to="tier_main"><font-awesome-icon style="font-size: 20px" icon="fa-solid fa-x" /></router-link>
        <span class="copy-code">초대코드 복사</span>
    </div>
    <div class="invite-info">
        <p style="font-weight: 600; color: #b8b8b8; font-size: 10px; margin-bottom: 10px">신한 알파의 주린이 서비스를 모르는 친구가 있나요?</p>
        <p style="font-weight: 600; color: black; font-size: 13px; margin-bottom: 20px">친구에게 주린이 서비스를 알리면<br />친구도 나도 포인트를 받아요</p>
        <p style="font-weight: 400; color: #979797; font-size: 9px; margin-bottom: 8px">친구 휴대폰에 신한 알파를 설치해주세요!</p>
        <p style="font-weight: 400; color: #979797; font-size: 9px">계좌개설 후 초대코드를 입력하면 완료!</p>
    </div>
    <div class="code-div">
        <p style="color: #979797; font-weight: 600; font-size: 9px">초대코드</p>
        <p style="color: #000000; font-weight: 600; font-size: 18px">010 9968 7216</p>
    </div>
    <p style="font-size: 9px; font-weight: 600; margin-top: 8px">초대코드는 가입 후 24시간 내까지 입력할 수 있어요</p>
    <div class="send-btn">친구에게 알리기</div>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
export default {
    components: {
        PhoneHeader,
    },
};
</script>

<style>
.top-bar {
    display: flex;
    justify-content: space-between;
    margin-top: 40px;
    height: 28px;
    align-items: center;
    padding-right: 15px;
    padding-left: 15px;
}

.copy-code {
    font-weight: 600;
    font-size: 10px;
    color: rgba(0, 0, 0, 0.5);
}

.invite-info {
    text-align: left;
    margin-top: 30px;
    margin-left: 20px;
}

.code-div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 245px;
    height: 140px;
    border-radius: 10px;
    background-color: #f0f0f0;
    text-align: center;
    margin: 0 auto;
    margin-top: 40px;
}

.send-btn {
    width: 277px;
    height: 40px;
    text-align: center;
    color: white;
    border-radius: 10px;
    background-color: #354ef2;
    font-weight: 600;
    font-size: 11px;
    margin: 0 auto;
    margin-top: 120px;
    line-height: 40px;
}

a {
    color: black;
}
</style>
