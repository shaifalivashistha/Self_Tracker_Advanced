import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginView from "../views/LoginView.vue";
import AboutView from "../views/AboutView.vue";
import RegisterView from "../views/RegisterView.vue";
import dashboardView from "../views/dashboardView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    component: AboutView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/register",
    name: "register",
    component: RegisterView,
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: dashboardView,
  },
  // {
  // path: "/dashboard/",
  // name: "create_trackers",
  // component: create_tracker
  // }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
