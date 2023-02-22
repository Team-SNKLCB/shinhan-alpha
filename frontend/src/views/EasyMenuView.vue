<template>
    <div>
        <phone-header></phone-header>
        <div class="easy-menu-header">
            <span v-if="isLogin === null" style="font-size: 14px; color: white">만나서 반가워요!</span>
            <span v-else style="font-size: 14px; color: white">{{ userDetail.name }}님</span>
            <div class="edit-box">
                <img class="icon" src="../assets/top/edit-icon.png" />
                <img class="icon" src="../assets/top/bell-icon.png" />
                <router-link to="/menu_setting"><img class="icon" src="../assets/top/setting-icon.png" /></router-link>
            </div>
        </div>
        <div v-if="isLogin" class="my-asset">
            <p style="font-size: 16px; font-weight: 500; margin-bottom: 5px">총 자산</p>
            <p style="font-size: 24px; font-weight: 600">10,587원</p>
            <p style="color: red; font-size: 12px">+500원 (2.00%)</p>
        </div>
        <div id="my-apps">
            <div class="groups">
                <div class="group">
                    <Container group-name="1" :get-child-payload="getChildPayload1" @drop="onDrop('items1', $event)">
                        <Draggable v-for="item in items1" :key="item.id">
                            <div class="drag-item">
                                {{ item.name }}
                            </div>
                        </Draggable>
                    </Container>
                </div>
                <div class="group">
                    <Container group-name="1" :get-child-payload="getChildPayload2" @drop="onDrop('items2', $event)">
                        <Draggable v-for="item in items2" :key="item.id">
                            <div class="drag-item">
                                {{ item.name }}
                            </div>
                        </Draggable>
                    </Container>
                </div>
                <div class="group">
                    <Container group-name="1" :get-child-payload="getChildPayload3" @drop="onDrop('items3', $event)">
                        <Draggable v-for="item in items3" :key="item.id">
                            <div class="drag-item">
                                {{ item.name }}
                            </div>
                        </Draggable>
                    </Container>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
import { Container, Draggable } from "vue-dndrop";
import { applyDrag } from "../utils/helper.js";
export default {
    data() {
        return {
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
        Container,
        Draggable,
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
        onDrop(collection, dropResult) {
            this[collection] = applyDrag(this[collection], dropResult);
        },

        getChildPayload1(index) {
            return this.items1[index];
        },

        getChildPayload2(index) {
            return this.items2[index];
        },

        getChildPayload3(index) {
            return this.items3[index];
        },
        shouldAcceptDrop(sourceContainerOptions, payload) {
            return true;
        },
    },

    created() {
        this.$store.dispatch("GET_USER_DETAIL");
    },
};
</script>

<style>
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
</style>
