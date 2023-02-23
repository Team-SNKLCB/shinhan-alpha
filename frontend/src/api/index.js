import axios from "axios";

const config = {
    baseurl: "http://34.64.212.142",
};

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

function getPoints() {
    return axios.get(`${config.baseurl}/api/user/signin`, {
        headers: {
            Authorization: "JWT " + sessionStorage.getItem("accessToken"),
        },
    });
}

function getMissionList() {
    return axios.get(`${config.baseurl}/api/user/reward`, {
        headers: {
            Authorization: "JWT " + sessionStorage.getItem("accessToken"),
        },
    });
}

export { getUserMission, getUserDetail, changeUserMode, getPoints, getMissionList };
