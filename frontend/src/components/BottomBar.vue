<template>
    <div class="btm-bar">
        <div class="item item-one-line fa-bars"><font-awesome-icon icon="fa-solid fa-bars" /></div>
        <div style="color: white" class="item item-one-line"><bold>홈</bold></div>
        <div class="item">관심<br />종목</div>
        <div class="item item-one-line">현재가</div>
        <div class="item">주식<br />주문</div>
        <div class="item">주식<br />잔고</div>
        <div class="item item-one-line fa-right"><font-awesome-icon icon="fa-solid fa-chevron-right" /></div>
    </div>
</template>

<script>
export default {};
</script>

<style>
.btm-bar {
    width: 100%;
    height: 45px;
    background-color: #34383e;
    position: fixed;
    bottom: 0;
    display: flex;
}

.item {
    width: 54px;
    height: 100%;
    font-size: 13px;
    font-weight: 600;
    color: #838384;
    text-align: center;
    line-height: 22px;
}

.item-one-line {
    line-height: 45px;
}

.fa-bars {
    font-size: 24px;
    color: white;
}

.fa-right {
    font-size: 24px;
    color: #8b95a1;
}
</style>
