import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import "bootstrap";

/* import the fontawesome core */
import { library } from "@fortawesome/fontawesome-svg-core";

/* import font awesome icon component */
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import veProgress from "vue-ellipse-progress";

/* import specific icons */
import { faPencil, faWifi } from "@fortawesome/free-solid-svg-icons";
import { faBatteryFull } from "@fortawesome/free-solid-svg-icons";
import { faSignal } from "@fortawesome/free-solid-svg-icons";
import { faBars } from "@fortawesome/free-solid-svg-icons";
import { faChevronRight, faChevronLeft } from "@fortawesome/free-solid-svg-icons";
import { faX } from "@fortawesome/free-solid-svg-icons";
import { faBell } from "@fortawesome/free-solid-svg-icons";
/* add icons to the library */
library.add(faWifi, faBatteryFull, faSignal, faBars, faChevronRight, faChevronLeft, faX, faBell, faPencil);

createApp(App).use(store).use(router).use(veProgress).component("font-awesome-icon", FontAwesomeIcon).mount("#app");
