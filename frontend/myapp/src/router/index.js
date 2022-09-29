import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginView from "../views/LoginView.vue";
import AboutView from "../views/AboutView.vue";
import RegisterView from "../views/RegisterView.vue";
import DashboardView from "../views/DashboardView.vue";
import createTrackerView from "../views/createTrackerView.vue"
import updateTrackerView from "../views/updateTrackerView.vue"
import addNumLogView from "../views/addNumLogView.vue"
import addBoolLogView from "../views/addBoolLogView.vue"
import updateLogView from "../views/updateLogView"

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
    path: "/register",
    name: "register",
    component: RegisterView,
  },
  {
    path: "/login_page",
    name: "login",
    component: LoginView,
  },
  {
    path: "/dashboard/:username",
    name: "dashboard",
    component: DashboardView,
  },
  {
    path: "/dashboard/:username/create_tracker",
    name: "createTrackerView",
    component: createTrackerView
  },
  {
    path: "/:username/:trackerID/update",
    name: "updateTrackerView",
    component: updateTrackerView
  },
  {
    path: "/:username/:trackerID/numeric",
    name: "addNumLogView",
    component: addNumLogView
  },
  {
    path: "/:username/:trackerID/boolean",
    name: "addBoolLogView",
    component: addBoolLogView
  },
  {
    path: "/:username/:trackerID/:logID/update",
    name: "updateLogView",
    component: updateLogView
  },

];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
