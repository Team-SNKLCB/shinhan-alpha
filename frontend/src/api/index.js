import axios from "axios";

const config = {
    baseurl: "http://127.0.0.1:8000",
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
export { getUserMission, getUserDetail, changeUserMode };
