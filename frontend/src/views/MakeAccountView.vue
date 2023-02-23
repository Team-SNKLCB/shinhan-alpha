<template>
    <div>
        <phone-header></phone-header>
        <div style="display: flex; justify-content: space-between; padding: 0 25px; margin-top: 40px; align-items: center">
            <p>계좌개설</p>
            <font-awesome-icon style="font-size: 20px" @click="goBack" icon="fa-solid fa-x" />
        </div>

        <div style="margin-top: 10px; background-color: #e9f0ff; height: 670px">
            <div class="title">
                <p>기본 정보 입력</p>
            </div>
            <div class="login-form">
                <p>이름</p>
                <input id="name" v-model="name" placeholder="이름" />
                <p>영문이름</p>
                <input id="english_name" v-model="english_name" placeholder="영어이름" />
                <p>주민등록번호('-' 제외)</p>
                <input id="id_number" v-model="id_number" placeholder="XXXXXX - XXXXXXX" /><br />
                <p>휴대폰번호('-' 제외)</p>
                <input id="tel" v-model="tel" placeholder="010-XXXX-XXXX" />
                <p>아이디</p>
                <input id="id" v-model="id" placeholder="아이디" />
                <p>비밀번호(4자리)</p>
                <input type="password" id="password" v-model="password" placeholder="비밀번호" />
            </div>
            <div @click="makeAccount" style="background-color: #4a8ce2; color: white" class="make-account-btn">계좌개설</div>
        </div>
    </div>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
import axios from "axios";
export default {
    data() {
        return {
            id: "",
            password: "",
            name: "",
            english_name: "",
            id_number: "",
            tel: "",
        };
    },
    components: { PhoneHeader },
    methods: {
        goBack() {
            window.history.length > 1 ? this.$router.go(-1) : this.$router.push("/");
        },

        changeToggle() {
            this.save_toggle = !this.save_toggle;
        },

        makeAccount() {
            axios
                .post("http://localhost:8000/api/user", {
                    password: this.password,
                    name: this.name,
                    ename: this.english_name,
                    rrn: this.id_number,
                    tel: this.tel,
                    tier: 1,
                    username: this.id,
                })
                .then((res) => this.$router.push("/login"))
                .catch((err) => console.log(err));
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
    padding-top: 40px;
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
    margin-top: 40px;
}

.login-form > p {
    text-align: left;
    margin-left: 40px;
    font-size: 12px;
    color: #878786;
}

.login-form > input {
    width: 240px;
    border: none;
    border-bottom: 1px solid #ced2d9;
    background-color: #e9f0ff;
    padding-bottom: 10px;
    padding-top: 10px;
    outline: none;
    margin-bottom: 20px;
}
</style>
