<template>
    <div class="modeSelectBox">
        <p class="title">어떤 모드를 선택하시겠어요?</p>
        <img @click="click_julin" class="btn-mode" src="../assets/button-julin.png" />
        <img @click="click_ordinary" class="btn-mode" src="../assets/button-ordinary.png" />
        <p class="sub-title">신한투자증권</p>
    </div>
</template>

<script>
export default {
    methods: {
        click_julin() {
            this.$store.state.e_active = true;
            this.$router.push("/mode_tutorial");
        },
        click_ordinary() {
            this.$store.state.e_active = false;
            this.$router.push("/menu");
        },
    },
    created() {
        sessionStorage.setItem("B3Flag", false);
    },
};
</script>

<style>
.modeSelectBox {
    height: 666px;
    background-color: #373deb;
    padding-top: 131px;
    box-sizing: border-box;
}
.btn-mode {
    width: 253px;
    height: 108px;
    border-radius: 10px;
    box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
    margin-top: 30px;
}

p {
    margin: 0;
}

.title {
    font-family: "Noto Sans KR";
    font-style: normal;
    font-weight: 700;
    font-size: 20px;
    color: white;
}
.sub-title {
    font-family: "Noto Sans KR";
    font-style: normal;
    font-weight: 700;
    font-size: 15px;
    color: white;
    margin-top: 100px;
}
</style>
