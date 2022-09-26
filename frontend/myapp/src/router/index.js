import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginView from "../views/LoginView.vue";
import AboutView from "../views/AboutView.vue";
import RegisterView from "../views/RegisterView.vue";
import dashboardView from "../views/dashboardView.vue";
import createTrackerView from "../views/createTrackerView.vue"
import updateTrackerView from "../views/updateTrackerView.vue"
import addNumLogView from "../views/addNumLogView.vue"
import updateLogView from "../views/updateLogView"
import BooleanView from "../views/BooleanView.vue"

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
  {
    path: "/dashboard/:email/create_tracker",
    name: "createTrackerView",
    component: createTrackerView
  },
  {
    path: "/:email/update/:id",
    name: "updateTrackerView",
    component: updateTrackerView
  },
  {
    path: "/user/tracker/numlog",
    name: "addNumLogView",
    component: addNumLogView
  },
  {
    path: "/user/tracker/boolean",
    name: "BooleanView",
    component: BooleanView
  },
  {
    path: "user/tracker/log/update",
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
