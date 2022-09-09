<template>
  <div class="home">
    <HomePage></HomePage>
    <img
      alt="Tracker logo"
      src="../assets/logo.jpeg"
      width="200"
      height="200"
    />
    <h1>New to The Self Tracker Application.</h1>
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
