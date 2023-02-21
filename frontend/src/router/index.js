import { createRouter, createWebHistory } from "vue-router";
import SplashView from "../views/SplashView.vue";
import ModeSelectView from "../views/ModeSelectView.vue";
import OrdinaryMenuView from "../views/OrdinaryMenuView.vue";
import ModeTutorialView from "../views/ModeTutorialView.vue";
import EasyMenuView from "../views/EasyMenuView.vue";
import TierMainView from "../views/TierMainView.vue";
import MissionView from "../views/MissionView.vue";
import InviteFriendView from "../views/InviteFriendView.vue";
import TakeRewardView from "../views/TakeRewardView.vue";
import SelectLoginTypeView from "../views/SelectLoginTypeView.vue";
import LoginView from "../views/LoginView.vue";
import MakeAccountView from "../views/MakeAccountView.vue";
import ShinhanPopular from "../views/ShinhanPopular.vue";
import CheckMyAccount from "../views/CheckMyAccount.vue";
import SendMoney from "../views/SendMoney.vue";
import RewardEvent from "../views/RewardEvent.vue";
import BuyStockPage from "../views/BuyStockPage.vue";
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
    name: "mission",
    component: MissionView,
  },
  {
    path: "/invite",
    name: "invite",
    component: InviteFriendView,
  },
  {
    path: "/take_reward",
    name: "take_reward",
    component: TakeRewardView,
  },
  {
    path: "/select_login",
    name: "select_login",
    component: SelectLoginTypeView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/make_account",
    name: "make_account",
    component: MakeAccountView,
  },
  {
    path: "/shinhan_popular",
    name: "shinhan_popular",
    component: ShinhanPopular,
  },
  {
    path: "/check_account",
    name: "check_account",
    component: CheckMyAccount,
  },
  {
    path: "/send_money",
    name: "send_money",
    component: SendMoney,
  },
  {
    path: "/reward_event",
    name: "reward_event",
    component: RewardEvent,
  },
  {
    path: "/buy_stock",
    name: "buy_stock",
    component: BuyStockPage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
