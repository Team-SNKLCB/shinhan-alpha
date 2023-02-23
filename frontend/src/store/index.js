import { createStore } from "vuex";
import { getUserMission, getUserDetail, changeUserMode } from "../api/index.js";

export default createStore({
    state: {
        missionList: [],
        userDetail: {},
        e_active: false,
        total_apps: [
            {
                x: 0,
                y: 0,
                w: 4,
                h: 2.5,
                i: "0",
                name: "이체",
                img: require("../assets/app-icon/이체.svg"),
                static: true,
                added: true,
            },
            {
                x: 4,
                y: 0,
                w: 4,
                h: 2.5,
                i: "1",
                name: "내 계좌 확인",
                img: require("../assets/app-icon/계좌확인.svg"),
                static: true,
                added: true,
            },
            {
                x: 8,
                y: 0,
                w: 4,
                h: 2.5,
                i: "2",
                name: "고객센터",
                img: require("../assets/app-icon/고객센터.svg"),
                static: true,
                added: true,
            },
            { x: 0, y: 2.5, w: 4, h: 2.5, i: "3", name: "MMF", img: require("../assets/app-icon/MMF.svg"), static: true, added: true },
            { x: 4, y: 2.5, w: 4, h: 2.5, i: "4", name: "RP", img: require("../assets/app-icon/RP.svg"), static: true, added: true },
            { x: 8, y: 2.5, w: 4, h: 2.5, i: "5", name: "국내주식", img: require("../assets/app-icon/국내주식.svg"), static: true, added: true },
            { x: 0, y: 5, w: 4, h: 2.5, i: "6", name: "해외주식", img: require("../assets/app-icon/해외주식.svg"), static: true, added: true },
            { x: 4, y: 5, w: 4, h: 2.5, i: "7", name: "국공채/국공채 펀드", img: require("../assets/app-icon/국공채.svg"), static: true, added: false },
            { x: 8, y: 5, w: 4, h: 2.5, i: "8", name: "전단채", img: require("../assets/app-icon/전단채.svg"), static: true, added: false },
            { x: 0, y: 7.5, w: 4, h: 2.5, i: "9", name: "채권형 펀드", img: require("../assets/app-icon/채권형 펀드.svg"), static: true, added: false },
            { x: 4, y: 7.5, w: 4, h: 2.5, i: "10", name: "회사채", img: require("../assets/app-icon/회사채.svg"), static: true, added: false },
            { x: 8, y: 7.5, w: 4, h: 2.5, i: "11", name: "ELS/DLS", img: require("../assets/app-icon/ELS.svg"), static: true, added: false },
            { x: 0, y: 10, w: 4, h: 2.5, i: "12", name: "ETF", img: require("../assets/app-icon/ETF.svg"), static: true, added: false },
            { x: 4, y: 10, w: 4, h: 2.5, i: "13", name: "혼합형/주식형 펀드", img: require("../assets/app-icon/주식형 펀드.svg"), static: true, added: false },
            { x: 8, y: 10, w: 4, h: 2.5, i: "14", name: "금", img: require("../assets/app-icon/금.svg"), static: true, added: false },
        ],
    },
    getters: {},
    mutations: {
        GET_USER_MISSION_LIST(state, missionList) {
            state.missionList = missionList;
        },
        GET_USER_DETAIL_MUT(state, userDetail) {
            state.userDetail = userDetail;
        },
        // CHANGE_USER_MENU_MODE(state, e_activate) {
        // },
    },
    actions: {
        async GET_MISSION_LIST(context) {
            return getUserMission()
                .then((res) => {
                    context.commit("GET_USER_MISSION_LIST", res.data.results);
                    return res.data;
                })
                .catch((err) => console.log(err));
        },

        async GET_USER_DETAIL(context) {
            return getUserDetail()
                .then((res) => {
                    context.commit("GET_USER_DETAIL_MUT", res.data.user);
                    return res.data;
                })
                .catch((err) => console.log(err));
        },

        // async CHANGE_USER_MODE(context) {
        //     return changeUserMode()
        //     .then(res => {
        //         context.commit('GET_USER_MENU_MODE') {
        //             return res;
        //         }
        //     })
        //     .catch(err=> console.log(err))
        // },
    },
    modules: {},
});
