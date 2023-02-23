<template>
    <div>
        <phone-header></phone-header>
        <!-- 첫번째 모달 -->
        <div v-if="buy_click === 1" class="overlay_modal">
            <div class="modal_page">
                <br />
                <p style="font-weight: bold; position: absolute; left: 15px"><span style="color: red">현금매수</span> 주문확인</p>
                <br />
                <br />
                <div class="word_box" style="color: #979797">
                    <div>
                        <span style="color: #cccccc">계좌번호 </span>
                    </div>
                    <div><span>270-49-464210 [01]ISA양서정</span></div>
                </div>
                <div class="word_box" style="color: #979797">
                    <div>
                        <span style="color: #cccccc">주문종목 </span>
                    </div>
                    <div><span>에스엠</span></div>
                </div>
                <div class="word_box" style="color: #979797">
                    <div>
                        <span style="color: #cccccc">주문수량 </span>
                    </div>
                    <div>
                        <span style="color: red">{{ stock_num }}주</span>
                    </div>
                </div>
                <div class="word_box" style="color: #979797">
                    <div>
                        <span style="color: #cccccc">주문단가 </span>
                    </div>
                    <div>
                        <span style="color: red">{{ stock_prize }}원</span>
                    </div>
                </div>
                <div class="word_box" style="color: #979797">
                    <div>
                        <span style="color: #cccccc">주문유형 </span>
                    </div>
                    <div><span>지정가</span></div>
                </div>
                <div class="word_box" style="color: #979797">
                    <div>
                        <span style="color: #cccccc">주문수량 </span>
                    </div>
                    <div>
                        <span style="color: black">{{ stock_sum }}원</span>
                    </div>
                </div>

                <p style="font-weight: bold">
                    &nbsp;위 내용으로
                    <span style="color: red; font-size: 20px">매수주문</span>을 하시겠습니까?
                </p>
                <p style="color: #3d83ab; font-weight: bold; font-size: 15px">쿠폰사용 주문안내 ></p>
                <p style="color: #979797; font-size: 12px">※수수료 및 제세금은 체결내역에서 확인하실 수 있습니다.</p>
                <br />
                <div style="display: flex; line-height: 40px">
                    <div @click="buy_click = 0" class="not_buy">
                        <span style="color: white">취소</span>
                    </div>
                    <div @click="buy_stock(3)" class="buy_box">
                        <span style="color: white">매수주문</span>
                    </div>
                </div>
            </div>
        </div>
        <!-- 두번째 모달 -->
        <div v-if="buy_click === 2" class="overlay_modal_sec">
            <div class="modal_page">
                <br />
                <p style="font-weight: bold; position: absolute; left: 92px; top: 40px">
                    <span style="color: red; font-size: 35px">매수 성공</span>
                </p>
                <br />
                <br />
                <br />
                <br />
                <div class="word_box" style="color: #979797">
                    <div>
                        <span style="color: #cccccc">계좌번호 </span>
                    </div>
                    <div><span>270-49-464210 [01]ISA양서정</span></div>
                </div>
                <div class="word_box" style="color: #979797">
                    <div>
                        <span style="color: #cccccc">주문종목 </span>
                    </div>
                    <div><span>에스엠</span></div>
                </div>
                <div class="word_box" style="color: #979797">
                    <div>
                        <span style="color: #cccccc">주문수량 </span>
                    </div>
                    <div>
                        <span style="color: red">{{ stock_num }}주</span>
                    </div>
                </div>
                <div class="word_box" style="color: #979797">
                    <div>
                        <span style="color: #cccccc">주문단가 </span>
                    </div>
                    <div>
                        <span style="color: red">{{ stock_prize }}원</span>
                    </div>
                </div>
                <div class="word_box" style="color: #979797">
                    <div>
                        <span style="color: #cccccc">주문유형 </span>
                    </div>
                    <div><span>지정가</span></div>
                </div>
                <div class="word_box" style="color: #979797">
                    <div>
                        <span style="color: #cccccc">주문금액 </span>
                    </div>
                    <div>
                        <span style="color: black">{{ stock_sum }}원</span>
                    </div>
                </div>
                <br />
                <div style="display: flex; line-height: 40px">
                    <div
                        @click="
                            () => {
                                buy_click = 0;
                                this.$router.push('/easy_menu');
                            }
                        "
                        class="not_buy_sec"
                    >
                        <span style="color: white">닫기</span>
                    </div>
                </div>
            </div>
        </div>
        <div style="position: absolute; top: 37px">
            <img style="width: 320px; margin-left: 2px" src="../assets/stock_top.png" />
            <div style="display: flex">
                <img style="width: 120px; position: absolute; left: 0px" src="../assets/stock_bottom.png" />
                <img style="width: 200px; position: absolute; right: 0px" src="../assets/stock_bottom2.png" />
                <div class="up_bar">
                    <img @click="add_stock" style="position: absolute; right: 10px; top: 15px" src="../assets/plus.png" />
                    <img @click="sub_stock" style="position: absolute; left: 10px; top: 15px" src="../assets/minus.png" />
                    <span style="position: absolute; top: 13px; font-size: 18px; font-weight: bold; right: 85px">{{ stock_num }} </span>
                    <span style="position: absolute; top: 20px; font-size: 10px; right: 75px">주</span>
                </div>
                <div class="down_bar">
                    <img @click="add_prize" style="position: absolute; right: 10px; top: 15px" src="../assets/plus.png" />
                    <img @click="sub_prize" style="position: absolute; left: 10px; top: 15px" src="../assets/minus.png" />
                    <span style="position: absolute; top: 13px; font-size: 18px; font-weight: bold; right: 60px">{{ stock_prize }} </span
                    ><span style="position: absolute; top: 20px; font-size: 10px; right: 50px">원</span>
                </div>
            </div>
            <div class="prize_bar">
                <div>
                    <p style="font-size: 9px; font-weight: bold">쿠폰선택</p>
                    <p style="font-size: 9px; font-weight: bold; color: #979797">주문금액</p>
                </div>
            </div>
            <div class="now_prize">
                <span style="font-weight: bold">{{ stock_sum }}</span>
                <span style="font-size: 13px"> 원</span>
            </div>
            <font-awesome-icon icon="fa-soild fa-chevron-left" @click="goBack" class="back_stock" />
        </div>
        <div @click="buy_click = 1" class="buy_bar">
            <span style="color: white; position: absolute; right: 59px; top: 3px; font-weight: bold">현금매수</span>
        </div>
    </div>
</template>
<script>
import PhoneHeader from "../components/PhoneHeader.vue";
import axios from "axios";
export default {
    components: { PhoneHeader },
    data() {
        return {
            stock_num: 0,
            stock_sum: 0,
            stock_prize: 121100,
            buy_click: 0,
        };
    },
    methods: {
        goBack() {
            window.history.length > 1 ? this.$router.go(-1) : this.$router.push("/");
        },
        add_stock() {
            this.stock_num += 1;
            this.stock_sum += this.stock_prize;
        },
        sub_stock() {
            if (this.stock_num > 0) {
                this.stock_num -= 1;
            }
            this.stock_sum -= this.stock_prize;
        },
        add_prize() {
            this.stock_prize += 100;
        },
        sub_prize() {
            if (this.stock_prize > 0) {
                this.stock_prize -= 100;
            }
        },
        buy_stock(id) {
            this.buy_click = 2;
            axios.put(
                "http://34.64.212.142/api/user/mission",
                {
                    id: id,
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
};
</script>
<style scoped>
.back_stock {
    position: absolute;
    left: 9px;
    top: 12px;
}
.up_bar {
    background-color: #f8f8f8;
    position: absolute;
    width: 180px;
    height: 50px;
    right: 13px;
    top: 320px;
    z-index: 3;
    border-radius: 10px;
}
.down_bar {
    background-color: #f8f8f8;
    position: absolute;
    width: 180px;
    height: 50px;
    right: 13px;
    top: 380px;
    z-index: 3;
    border-radius: 10px;
}
.prize_bar {
    display: flex;
    position: absolute;
    right: 150px;
    top: 500px;
}
.now_prize {
    position: absolute;
    right: 15px;
    top: 508px;
}
.buy_bar {
    height: 34px;
    width: 179px;
    position: absolute;
    background-color: red;
    border-radius: 3px;
    top: 575px;
    right: 12px;
}
.modal_page {
    position: absolute;
    width: 320px;
    height: 369px;
    background-color: white;
    border-radius: 15px 15px 0px 0px;
    z-index: 10;
    bottom: 0px;
}
.overlay_modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 320px;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 5;
}
.overlay_modal_sec {
    position: fixed;
    top: 0;
    left: 0;
    width: 320px;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 6;
}
.word_box {
    font-size: 15px;
    font-weight: bold;
    display: flex;
    justify-content: space-between;
    margin: 0px 15px;
}
.buy_box {
    width: 180px;
    height: 40px;
    background-color: red;
    border-radius: 5px;
    margin-left: 10px;
}
.not_buy {
    background-color: #979797;
    width: 80px;
    height: 40px;
    margin-left: 25px;
    border-radius: 5px;
}
.not_buy_sec {
    background-color: #979797;
    width: 80px;
    height: 40px;
    margin-left: 125px;
    border-radius: 5px;
}
</style>
