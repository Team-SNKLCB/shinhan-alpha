import axios from "axios";

const config = {
    baseurl: "http://34.64.212.142",
};

function getPoints() {
    return axios.get(`${config.baseurl}/api/user/totalpoint`, {
        headers: {
            Authorization: "JWT " + sessionStorage.getItem("accessToken"),
        },
    });
}

function getUserMission() {
    return axios.get(`${config.baseurl}/api/user/mission`, {
        headers: {
            Authorization: "JWT " + sessionStorage.getItem("accessToken"),
        },
    });
}

function getUserDetail() {
    return axios.get(`${config.baseurl}/api/user/detail`, {
        headers: {
            Authorization: "JWT " + sessionStorage.getItem("accessToken"),
        },
    });
}

function changeUserMode() {
    return axios.post(`${config.baseurl}/api/user/detail`, {
        headers: {
            Authorization: "JWT " + sessionStorage.getItem("accessToken"),
        },
    });
}

function getPointLog() {
    return axios.get(`${config.baseurl}/api/user/point`, {
        headers: {
            Authorization: "JWT " + sessionStorage.getItem("accessToken"),
        },
    });
}

function getUserReward() {
    return axios.get(`${config.baseurl}/api/user/reward`, {
        headers: {
            Authorization: "JWT " + sessionStorage.getItem("accessToken"),
        },
    });
}

export { getUserMission, getUserDetail, changeUserMode, getPointLog, getUserReward, getPoints };
