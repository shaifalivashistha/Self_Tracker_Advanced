import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginView from "../views/LoginView.vue";
import AboutView from "../views/AboutView.vue";
import RegisterView from "../views/RegisterView.vue";
import dashboardView from "../views/dashboardView.vue";
import createTrackerView from "../views/createTrackerView.vue"
import updateTrackerView from "../views/updateTrackerView.vue"
import addLogView from "../views/addLogView.vue"
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
    path: "/login",
    name: "logout",
    component: LoginView
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
    path: "/dashboard/:email",
    name: "dashboard",
    component: dashboardView,
  },
  {
    path: "/dashboard/:email/create_tracker",
    name: "createTrackerView",
    component: createTrackerView
  },
  {
    path: "",
    name: "updateTrackerView",
    component: updateTrackerView
  },
  {
    path: "",
    name: "addLogView",
    component: addLogView
  },
  {
    path: "",
    name: "updateLogView",
    component: updateLogView
  }


];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
