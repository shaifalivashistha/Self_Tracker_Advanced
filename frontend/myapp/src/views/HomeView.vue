<template>
  <div class="home">
    <img
      alt="Tracker logo"
      src="../assets/logo.jpeg"
      width="200"
      height="200"
    />
    <h1>New to The Self Tracker Application.</h1>
    <HelloWorld></HelloWorld>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "HomeView",
  components: {
    HelloWorld,
  },
};
</script>
