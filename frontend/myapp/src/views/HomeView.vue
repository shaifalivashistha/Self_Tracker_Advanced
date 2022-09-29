<template>
  <div class="home">
    <h1>New to The Self Tracker Application.</h1>
    <HomePage></HomePage>
    <p>
      <b-button href="/login_page">Login</b-button>
    </p>
    <p>
      <b-button href="/register">Register</b-button>
    </p>
  </div>
</template>

<script>
// @ is an alias to /src
import HomePage from "@/components/HomePage.vue";
export default {
  name: "HomeView",
  components: {
    HomePage,
  },
};
</script>

<style>
body {
  background-color: plum;
}
</style>
