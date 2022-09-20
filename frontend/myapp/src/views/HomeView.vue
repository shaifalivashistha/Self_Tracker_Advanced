<template>
  <div class="home">
    <h1>New to The Self Tracker Application.</h1>
    <HomePage></HomePage>
    <!-- <img left src="../assets/img1.jpeg" alt="Left image" width="500" height="700" /> -->

    <!-- <img alt="Tracker logo" src="../assets/logo.jpeg" width="200" height="200" /> -->
    <p>
      <b-button href="/login">Login</b-button>
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
