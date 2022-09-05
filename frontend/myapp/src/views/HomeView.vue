<template class="container">
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/Background.jpeg" /> -->
    <HelloWorld msg="Welcome to Your Vue.js App" />
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

<style scoped lang="scss">
.container {
  margin: 0;
  padding: 0;
  font-family: sans-serif;
  background-image: url("~@/assets/Background.jpeg");
}
</style>
