<template>
    <phone-header></phone-header>
    <div style="margin-top: 40px; background-color: #e9f0ff; height: 625px">
        <font-awesome-icon style="font-size: 20px; position: absolute; right: 25px; top: 50px" @click="goBack" icon="fa-solid fa-x" />
        <div class="title">
            <p>안전하고 간편한<br />로그인 방법을 선택하세요.</p>
        </div>
        <div class="login-select-box">
            <img class="login-img" src="../assets/login-1.png" />
            <img class="login-img" src="../assets/login-2.png" />
            <img class="login-img" src="../assets/login-3.png" />
            <router-link to="/login"><img style="margin-bottom: 30px" class="login-img" src="../assets/login-4.png" /></router-link>
        </div>
        <div style="background-color: #4a8ce2; color: white" class="make-account-btn">인증센터</div>
        <router-link to="/make_account"><div style="color: #4a8ce2" class="make-account-btn">계좌계설</div></router-link>
    </div>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
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
.login-img {
    width: 240px;
    margin: 0;
}

.title {
    margin: 40px;
    margin-right: 0px;
    text-align: left;
    padding-top: 60px;
    font-size: 18px;
    font-weight: 700;
    color: black;
}

.make-account-btn {
    width: 240px;
    height: 50px;
    border-radius: 30px;
    margin: 0 auto;
    border: 1px solid #4a8ce2;
    line-height: 50px;
    margin-bottom: 10px;
    font-family: "Noto Sans KR", sans-serif;
}

a {
    text-decoration: none;
}
</style>
