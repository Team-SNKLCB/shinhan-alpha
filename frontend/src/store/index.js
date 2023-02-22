import { createStore } from "vuex";
import { getUserMission, getUserDetail } from "../api/index.js";

export default createStore({
    state: {
        missionList: [],
        userDetail: {},
        e_activate: false,
    },
    getters: {},
    mutations: {
        GET_USER_MISSION_LIST(state, missionList) {
            state.missionList = missionList;
        },
        GET_USER_DETAIL_MUT(state, userDetail) {
            state.userDetail = userDetail;
        },
        CHANGE_MENU_MODE(state, e_activate) {
            state.e_activate = !state.e_activate;
        },
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
                    context.commit("GET_USER_DETAIL_MUT", res.data);
                    return res.data;
                })
                .catch((err) => console.log(err));
        },

        CHANGE_MODE(context) {
            context.commit("CHANGE_MENU_MODE");
        },
    },
    modules: {},
});
