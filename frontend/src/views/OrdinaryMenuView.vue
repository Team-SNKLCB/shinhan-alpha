<template>
    <phone-header></phone-header>
    <!-- <img class="ord-menu" src="../assets/ordinary-menu.png" /> -->
    <div class="top-bar">
        <div class="search-div">
            <input style="font-size: 12px; padding-left: 5px" class="search" placeholder="메뉴·종목 검색" />
            <i class="xi-bell-o icon"></i>
            <router-link to="/menu_setting"><i class="xi-cog icon"></i></router-link>
        </div>
        <div style="padding-bottom: 20px" class="big-menu-div">
            <div class="top-click">매매</div>
            <div>상품</div>
            <div>뱅킹/공모주</div>
            <div>고객센터</div>
        </div>
    </div>
    <div style="display: flex">
        <div class="left-bar">
            <div :class="isClicked == menu ? 'selected-style' : 'no-style'" v-for="(menu, i) in centerMenu" :key="i">
                <a v-bind:href="`#${i}`" @click="clickLeft(menu)"
                    ><p :class="isClicked == menu ? 'selected-style' : 'no-style'">{{ menu }}</p></a
                >
            </div>
        </div>
        <div class="right-bar">
            <div v-for="(menu, b) in menus" :key="menu">
                <p :id="b" class="bigmenu">{{ centerMenu[b] }}</p>
                <div v-for="(minmenu, i) in Object.keys(menu)" :key="minmenu">
                    <p class="minmenu">{{ minmenu }}</p>
                    <div v-for="smallmenu in Object.values(menu)[i]" :key="smallmenu">
                        <p class="smallmenu">{{ smallmenu }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <bottom-bar></bottom-bar>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
import BottomBar from "@/components/BottomBar.vue";
export default {
    data() {
        return {
            centerMenu: ["국내주식", "해외주식", "CFD", "선물옵션", "기타시장", "투자정보", "투자플러스"],
            menus: [
                {
                    종목찾기: ["실시간 종목 순위", "신한인기종목", "외국인/기관 순매수", "테마(섹터)순위", "신한리서치추천", "신규상장종목", "공매도/대차", "시장조치", "ETF/ETN"],
                    종목조건검색: ["간편조건검색", "조건검색", "차트패턴검색"],
                    주식매매: ["주식종목검색", "관심종목", "주식/ETF 현재가", "주식/ETF 주문", "주식잔고/손익", "체결/매매내역", "물타기계산기"],
                    "다양한 주문": ["예약주문", "호가주문", "스탑자동주문", "바로주문", "알파카트(일괄매수)", "제휴대출주문", "대주차입주문", "권리공매도주문"],
                    "주식 거래확인": ["반대매매예정내역", "미수동결담보부족현황", "매매다이어리"],
                    "국내주식 소수점투자": ["소수점 투자", "소수점 거래신청"],
                    "국내주식 간편투자": ["주식/ETF 정기투자 가입", "주식/ETF 정기투자 내역"],
                    차트: ["종합차트", "지수/업종차트"],
                    "주식 가이드": ["주식투자 가이드", "주식용어 가이드"],
                },
                {
                    "해외주식 매매": [
                        "해외종목검색",
                        "관심종목",
                        "해외주식 현재가",
                        "해외주식 종합차트",
                        "해외주식 주문",
                        "해외주식 예약주문",
                        "해외주식 소수점 투자",
                        "해외주식 거래신청",
                        "실시간 시세신청",
                    ],
                    "해외주식 거래확인": ["해외주식 잔고/손익", "해외주식 체결/매매내역", "해외주식 배당/세금"],
                    환전: ["환율조회", "환전신청", "환전신청내역"],
                    종목상세검색: ["해외종목순위", "미국종목발굴", "글로벌 종목정보", "글로벌ETF 정보", "업종/테마별ETF", "미국레버리지ETF"],
                    "해외주식 시작하기": ["해외주식 공지사항", "해외주식 시장안내", "해외주식 유의사항", "해외주식 FAQ"],
                },
                {
                    "CFD 매매": ["CFD 종목검색", "CFD 현재가", "CFD 주문", "CFD 차트", "CFD 잔고/손익", "CFD 체결/매매내역", "CFD 청산내역", "CFD 리콜내역"],
                    "CFD 신청": ["CFD 신청"],
                },
                {
                    "선물옵션 매매": [
                        "선물옵션 현재가",
                        "선물옵션 주문",
                        "선물옵션 차트",
                        "선물옵션 잔고/손익",
                        "선물옵션 체결/매매내역",
                        "지수선물 전종목시세",
                        "지수옵션 전종목시세",
                        "선물옵션지수종합",
                        "기초자산추이",
                        "선물옵션 예약주문",
                    ],
                    "야간선물옵션 매매": ["야간선물옵션 현재가", "야간선물옵션 주문", "야간선물옵션 차트"],
                    "선물옵션 계좌/증거금": ["계좌별 위탁증거금", "종목별 위탁증거금", "선물옵션 주문증거금", "선물대용 지정/해제", "선물정산가 조회", "추가증거금계좌 복수주문"],
                    "신청/등록": ["선물옵션 거래신청", "매매신청(유렉스연계)", "사전투자경험신청", "타사 거래확인서 등록", "선물옵션 계좌유형설정", "선물옵션약관승인"],
                },
                {
                    금현물: ["금현물 현재가", "금현물 주문", "금현물 잔고"],
                    "K-OTC": ["K-OTC 현재가", "K-OTC 주문"],
                    ELW: ["ELW 현재가", "ELW 주문"],
                    신주인수권: ["신주인수권 현재가", "신주인수권 주문"],
                },
                {
                    시장동향: ["지수/환율/시장지표", "국내시장 매매동향", "최신시황", "글로벌경제지표"],
                    "이슈/일정": ["뉴스/공시", "국내/해외 증시일정", "해외주식 권리"],
                    디지털자산: ["디지털자산 시세", "디지털자산 리서치", "디지털자산 알아보기"],
                    신한리서치: ["신한리서치리포트", "리서치캘린더"],
                },
                {
                    종목찾기: ["마법공식", "종목분석검색", "취향저격", "고수들의 종목"],
                    종목추천: ["파워맵", "수급파인더", "5START", "스톡봇", "로보스탁", "시그널엔진", "뉴지스탁"],
                },
            ],
            isClicked: "국내주식",
        };
    },
    components: {
        PhoneHeader,
        BottomBar,
    },
    methods: {
        clickLeft(menu) {
            this.isClicked = menu;
        },
    },
};
</script>

<style scoped>
.ord-menu {
    margin-top: 40px;
    margin-bottom: 45px;
}

.top-bar {
    padding: 10px 0;
    height: 70px;
    background-color: #3f81d7;
    display: flex;
    flex-direction: column;
}

.big-menu-div {
    display: flex;
    color: #88b0eb;
    justify-content: space-between;
}

.search {
    width: 200px;
    height: 25px;
    border: none;
    background: white;
    border-radius: 5px;
}
.icon {
    font-size: 24px;
    color: white;
}

.search-div {
    display: flex;
    align-items: center;
    justify-content: space-around;
    margin-bottom: 5px;
}

.big-menu-div > div {
    margin: 0 13px;
}

.search-div > i,
input {
    margin: 0 8px;
}
a {
    text-decoration: none;
}

.left-bar {
    width: 100px;
    font-weight: 500;
    height: 513px;
    text-align: left;
    font-size: 14px;
    background-color: #f0f0f0;
}
.left-bar > div > a {
    color: black;
}
.left-bar > div {
    padding: 10px;
}

.right-bar {
    scroll-behavior: smooth;
    scroll-margin-top: 50px;
    width: 220px;
    height: 513px;
    text-align: left;
    padding-left: 10px;
    padding-right: 20px;
    overflow: scroll;
}

.bigmenu {
    height: 40px;
    line-height: 40px;
    font-weight: 600;
    margin-left: -10px;
    padding-left: 10px;
    width: 220px;
    margin-top: 30px;
    background-color: #f0f0f0;
}

.right-bar > div:nth-child(1) > p {
    margin-top: 0;
}

.minmenu {
    margin-bottom: 6px;
    font-size: 14px;
    font-weight: 500;
    padding-bottom: 8px;
    border-bottom: 1px solid grey;
    margin-top: 20px;
}

.smallmenu {
    font-size: 16px;
    font-weight: 400;
    margin-bottom: 6px;
    color: #8b8b8c;
}

.top-click {
    color: white;
}

.selected-style {
    background-color: white;
    color: #3f81d7;
}
</style>
