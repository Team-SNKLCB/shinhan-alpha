import { createRouter, createWebHistory } from "vue-router";
import SplashView from "../views/SplashView.vue";
import ModeSelectView from "../views/ModeSelectView.vue";
import OrdinaryMenuView from "../views/OrdinaryMenuView.vue";
import ModeTutorialView from "../views/ModeTutorialView.vue";
import EasyMenuView from "../views/EasyMenuView.vue";
import TakeRewardView from "../views/TakeRewardView.vue";
const routes = [
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/take_reward",
    name: "take_reward",
    component: TakeRewardView,
  },

  {
    path: "/splash",
    name: "splash",
    component: SplashView,
  },
  {
    path: "/modeSelect",
    name: "modeSelect",
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
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
