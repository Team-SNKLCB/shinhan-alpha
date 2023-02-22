<template>
    <my-grid-layout
        :col-num="12"
        :row-height="30"
        :is-draggable="true"
        :is-resizable="true"
        :is-mirrored="false"
        :vertical-compact="true"
        :margin="[10, 10]"
        :use-css-transforms="true"
        :layout="layout"
    >
        <my-grid-item v-for="item in layout" :x="item.x" :y="item.y" :w="item.w" :h="item.h" :i="item.i" :key="item.i">
            <div style="width: 30px; height: 30px; background-color: aquamarine; display: inline-block">{{ item.i }}</div>
        </my-grid-item>
    </my-grid-layout>
</template>

<script>
import { GridLayout, GridItem } from "vue3-grid-layout-next";
export default {
    components: {
        myGridLayout: GridLayout,
        myGridItem: GridItem,
    },
    data() {
        return {
            layout: [
                { x: 0, y: 0, w: 4, h: 2, i: "0" },
                { x: 2, y: 0, w: 4, h: 2, i: "1" },
                { x: 4, y: 0, w: 4, h: 2, i: "2" },
                { x: 0, y: 0, w: 4, h: 2, i: "3" },
                { x: 2, y: 0, w: 4, h: 2, i: "4" },
                { x: 4, y: 0, w: 4, h: 2, i: "5" },
                { x: 0, y: 0, w: 4, h: 2, i: "6" },
                { x: 2, y: 0, w: 4, h: 2, i: "7" },
                { x: 4, y: 0, w: 4, h: 2, i: "8" },
            ],
            draggable: true,
            resizable: true,
            index: 0,
        };
    },
    methods: {
        itemTitle(item) {
            let result = item.i;
            if (item.static) {
                result += " - Static";
            }
            return result;
        },
    },
};
</script>

<style scoped>
.vue-grid-layout {
    background: #eee;
}
.vue-grid-item:not(.vue-grid-placeholder) {
    background: #ccc;
    border: 1px solid black;
}
.vue-grid-item .resizing {
    opacity: 0.9;
}
.vue-grid-item .static {
    background: #cce;
}
.vue-grid-item .text {
    font-size: 24px;
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
