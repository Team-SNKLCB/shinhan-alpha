<template>
    <div>
        <phone-header></phone-header>
        <div class="easy-menu-header">
            <span v-if="isLogin === null" style="font-size: 14px; color: white">만나서 반가워요!</span>
            <span v-else style="font-size: 14px; color: white">{{ userDetail.name }}님</span>
            <div class="edit-box">
                <img @click="toggleEdit" v-if="changeMode === false" class="icon" src="../assets/top/edit-icon.png" />
                <img style="background: blue" v-else-if="changeMode === true" @click="toggleEdit" class="icon" src="../assets/top/edit-icon.png" />
                <img class="icon" src="../assets/top/bell-icon.png" />
                <router-link to="/menu_setting"><img class="icon" src="../assets/top/setting-icon.png" /></router-link>
            </div>
        </div>
        <div v-if="isLogin" class="my-asset">
            <p style="font-size: 16px; font-weight: 500; margin-bottom: 5px">총 자산</p>
            <p style="font-size: 24px; font-weight: 600">10,587원</p>
            <p style="color: red; font-size: 12px">+500원 (2.00%)</p>
        </div>
        <div id="my-apps" v-if="changeMode === true">
            <my-grid-layout
                :col-num="12"
                :row-height="30"
                :is-draggable="true"
                :is-resizable="true"
                :is-mirrored="false"
                :responsive="responsive"
                :vertical-compact="true"
                :margin="[10, 10]"
                :use-css-transforms="true"
                :layout="layout"
                :is-bounded="true"
                :breakpoints="false"
                :cols="false"
            >
                <my-grid-item
                    style="text-align: center; display: flex; flex-direction: column; justify-content: space-between; align-items: center"
                    v-for="item in layout"
                    :x="item.x"
                    :y="item.y"
                    :w="item.w"
                    :h="item.h"
                    :i="item.i"
                    :key="item.i"
                >
                    <span class="remove" @click="removeItem(item.i)">x</span>
                    <div style="margin-top: 10px; width: 60px; height: 60px; background-color: aqua"></div>
                    <div style="font-size: 10px">{{ item.name }}</div>
                </my-grid-item>
            </my-grid-layout>
        </div>
        <div class="my-grid-item" v-else-if="isLogin === false">
            <div class="app" v-for="item in defaultLayout" :key="item">
                {{ item.name }}
            </div>
        </div>
        <div v-else-if="isLogin && changeMode === false" class="my-grid-item my-apps login">
            <div class="app" v-for="item in layout" :key="item">
                {{ item.name }}
            </div>
        </div>
        <div v-if="isLogin === null">
            <router-link to="/login"><div class="login-btn">로그인</div></router-link>
            <router-link to="/make_account"><div class="make-account-btn">계좌만들기</div></router-link>
        </div>
    </div>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
import { GridLayout, GridItem } from "vue3-grid-layout-next";
export default {
    data() {
        return {
            changeMode: false,
            defaultLayout: [
                { x: 0, y: 0, w: 4, h: 2.5, i: "0", name: "이체" },
                { x: 4, y: 0, w: 4, h: 2.5, i: "1", name: "내 계좌 확인" },
                { x: 8, y: 0, w: 4, h: 2.5, i: "2", name: "고객센터" },
            ],
            layout: [
                { x: 0, y: 0, w: 4, h: 2.5, i: "0", name: "이체" },
                { x: 4, y: 0, w: 4, h: 2.5, i: "1", name: "내 계좌 확인" },
                { x: 8, y: 0, w: 4, h: 2.5, i: "2", name: "고객센터" },
                { x: 0, y: 0, w: 4, h: 2.5, i: "3", name: "하하" },
                { x: 4, y: 0, w: 4, h: 2.5, i: "4", name: "히히" },
                { x: 8, y: 0, w: 4, h: 2.5, i: "5", name: "호호" },
            ],
            draggable: true,
            resizable: true,
            index: 0,
            items1: [
                {
                    id: 1,
                    name: "이체",
                },
                {
                    id: 2,
                    name: "내 계좌 확인",
                },
                {
                    id: 3,
                    name: "고객센터",
                },
            ],
            items2: [
                {
                    id: 4,
                    name: "이체",
                },
                { id: 5, name: "내 계좌 확인" },
                { id: 6, name: "고객센터" },
            ],
            items3: [
                { id: 7, name: "이체" },
                { id: 8, name: "내 계좌 확인" },
                { id: 9, name: "고객센터" },
            ],
        };
    },
    components: {
        PhoneHeader,
        myGridLayout: GridLayout,
        myGridItem: GridItem,
    },
    computed: {
        userDetail() {
            return this.$store.state.userDetail;
        },
        isLogin() {
            return sessionStorage.getItem("accessToken");
        },
    },
    methods: {
        toggleEdit() {
            if (this.isLogin === null) {
                alert("로그인이 필요합니다.");
                this.$router.push("/login");
                return;
            }
            this.changeMode = !this.changeMode;
        },
        addItem: function () {
            // Add a new item. It must have a unique key!
            this.layout.push({
                x: (this.layout.length * 2) % (this.colNum || 12),
                y: this.layout.length + (this.colNum || 12), // puts it at the bottom
                w: 2,
                h: 2,
                i: this.index,
            });
            // Increment the counter to ensure key is always unique.
            this.index++;
        },
        removeItem: function (val) {
            const index = this.layout.map((item) => item.i).indexOf(val);
            this.layout.splice(index, 1);
        },
    },

    created() {
        this.$store.dispatch("GET_USER_DETAIL");
    },
};
</script>

<style>
.my-grid-item {
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
}

.remove {
    cursor: pointer;
    position: absolute;
    right: 2px;
}
.login {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    margin-left: 10px;
    margin-top: 20px;
}
.app {
    font-size: 10px;
    width: 93px;
    height: 90px;
    border: 1px solid black;
    margin-bottom: 10px;
}
.easy-menu-header {
    width: 291px;
    height: 46px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #354ef2;
    margin: 0 auto;
    margin-top: 51px;
    padding: 0 12px;
    border-radius: 6px;
}

.edit-box {
    display: flex;
    align-items: center;
}

.icon {
    margin-left: 10px;
    width: 24px;
    height: 24px;
}

.my-asset {
    width: 291px;
    height: 95px;
    background-color: #f0f0f0;
    border-radius: 6px;
    text-align: left;
    margin: 0 auto;
    margin-top: 11px;
    padding-left: 12px;
    padding-top: 4px;
    box-sizing: border-box;
}

.groups {
    display: flex;
    justify-content: stretch;
}

.group {
    flex: 1;
}

/* #my-apps {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
} */

.drag-item {
    width: 105px;
    height: 105px;
    border: 1px solid black;
}

.login-btn {
    background-color: #354ef2;
    color: white;
    border-radius: 25px;
    width: 283px;
    height: 50px;
    margin: 0 auto;
    line-height: 50px;
    margin-top: 60px;
    font-weight: 700;
}

.make-account-btn {
    background-color: #a8b4ff;
    color: #354ef2;
    border-radius: 25px;
    width: 283px;
    height: 50px;
    margin: 0 auto;
    line-height: 50px;
    margin-top: 20px;
    font-weight: 700;
}

.vue-grid-layout {
    background: #ffffff;
}
.vue-grid-item:not(.vue-grid-placeholder) {
    background: #ffffff;
    border: 1px solid grey;
}
.vue-grid-item .resizing {
    opacity: 0.9;
}
.vue-grid-item .static {
    background: rgb(255, 255, 255);
}
.vue-grid-item .text {
    font-size: 10px;
    text-align: center;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;
    height: 100%;
    width: 100%;
}
.vue-grid-item .no-drag {
    height: 100%;
    width: 100%;
}
.vue-grid-item .minMax {
    font-size: 12px;
}
.vue-grid-item .add {
    cursor: pointer;
}
.vue-draggable-handle {
    position: absolute;
    width: 20px;
    height: 20px;
    top: 0;
    left: 0;
    background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='10' height='10'><circle cx='5' cy='5' r='5' fill='#999999'/></svg>") no-repeat;
    background-position: bottom right;
    padding: 0 8px 8px 0;
    background-repeat: no-repeat;
    background-origin: content-box;
    box-sizing: border-box;
    cursor: pointer;
}
</style>
