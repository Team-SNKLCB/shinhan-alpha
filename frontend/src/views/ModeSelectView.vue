<template>
    <div class="modeSelectBox">
        <p class="title">어떤 모드를 선택하시겠어요?</p>
        <router-link to="/easy_menu"><img class="btn-mode" src="../assets/button-julin.png" /></router-link>
        <router-link to="/ordinary_menu"><img class="btn-mode" src="../assets/button-ordinary.png" /></router-link>
        <p class="sub-title">신한투자증권</p>
    </div>
</template>

<script>
export default {};
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
