import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
/* import the fontawesome core */
import { library } from "@fortawesome/fontawesome-svg-core";

/* import font awesome icon component */
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

/* import specific icons */
import { faWifi } from "@fortawesome/free-solid-svg-icons";
import { faBatteryFull } from "@fortawesome/free-solid-svg-icons";
import { faSignal } from "@fortawesome/free-solid-svg-icons";
import { faBars } from "@fortawesome/free-solid-svg-icons";
import { faChevronRight } from "@fortawesome/free-solid-svg-icons";
/* add icons to the library */
library.add(faWifi, faBatteryFull, faSignal, faBars, faChevronRight);

createApp(App).use(store).use(router).component("font-awesome-icon", FontAwesomeIcon).mount("#app");
