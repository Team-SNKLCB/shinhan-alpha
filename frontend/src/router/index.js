import { createRouter, createWebHistory } from "vue-router";
import SplashView from "../views/SplashView.vue";
import ModeSelectView from "../views/ModeSelectView.vue";
import OrdinaryMenuView from "../views/OrdinaryMenuView.vue";
import ModeTutorialView from "../views/ModeTutorialView.vue";
import EasyMenuView from "../views/EasyMenuView.vue";
import TierMainView from "../views/TierMainView.vue";
import MissionView from "../views/MissionView.vue";
import InviteFriendView from "../views/InviteFriendView.vue";
const routes = [
    {
        path: "/about",
        name: "about",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
    },
    {
        path: "/splash",
        name: "splash",
        component: SplashView,
    },
    {
        path: "/mode_select",
        name: "mode_select",
        component: ModeSelectView,
    },
    {
        path: "/ordinary_menu",
        name: "ordinary_menu",
        component: OrdinaryMenuView,
    },
    {
        path: "/mode_tutorial",
        name: "mode_tutorial",
        component: ModeTutorialView,
    },
    {
        path: "/easy_menu",
        name: "easy_menu",
        component: EasyMenuView,
    },
    {
        path: "/tier_main",
        name: "tier_main",
        component: TierMainView,
    },
    {
        path: "/mission",
        name: "misson",
        component: MissionView,
    },
    {
        path: "/invite",
        name: "invite",
        component: InviteFriendView,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
