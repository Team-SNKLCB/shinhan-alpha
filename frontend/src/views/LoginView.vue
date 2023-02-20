<template>
    <phone-header></phone-header>
    <div style="display: flex; justify-content: space-between; padding: 0 25px; margin-top: 40px; align-items: center">
        <p>아이디 로그인</p>
        <font-awesome-icon style="font-size: 20px" @click="goBack" icon="fa-solid fa-x" />
    </div>

    <div style="margin-top: 10px; background-color: #e9f0ff; height: 625px">
        <div class="title">
            <p>아이디 로그인</p>
            <p style="font-size: 12px; color: #666464">공동인증서 비밀번호를 입력해주세요.</p>
        </div>
        <div class="login-form">
            <input id="id" v-model="id" placeholder="아이디" />
            <input id="password" v-model="password" placeholder="비밀번호" />
            <input id="finance_password" v-model="finance_password" placeholder="공동인증서 비밀번호" /><br />
            <div style="display: flex; justify-content: right; align-items: center; margin-top: 10px; margin-right: 15px">
                <span style="font-size: 12px; margin-bottom: 8px; margin-right: 5px; color: #65666b">아이디저장</span>
                <img @click="changeToggle" v-if="save_toggle === false" src="../assets/off-btn.png" style="width: 80px; height: 40px" />
                <img @click="changeToggle" v-else-if="save_toggle === true" src="../assets/on-btn.png" style="width: 80px; height: 40px" />
            </div>
        </div>
        <div style="background-color: #4a8ce2; color: white" class="make-account-btn">로그인</div>
    </div>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
export default {
    data() {
        return {
            id: "",
            password: "",
            finance_password: "",
            save_toggle: false,
        };
    },
    components: { PhoneHeader },
    methods: {
        goBack() {
            window.history.length > 1 ? this.$router.go(-1) : this.$router.push("/");
        },
    },
    methods: {
        goBack() {
            window.history.length > 1 ? this.$router.go(-1) : this.$router.push("/");
        },

        changeToggle() {
            this.save_toggle = !this.save_toggle;
        },
    },
};
</script>

<style scoped>
.title {
    margin: 40px;
    margin-right: 0px;
    margin-top: 0px;
    margin-left: 30px;
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
}

.login-form {
    margin-top: 80px;
    margin-bottom: 90px;
}

.login-form > input {
    width: 240px;
    border: none;
    border-bottom: 1px solid #ced2d9;
    background-color: #e9f0ff;
    padding: 25px;
    padding-bottom: 10px;
    outline: none;
}
</style>
