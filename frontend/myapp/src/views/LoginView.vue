<template>
  <div class="login">
    <!-- <h1><em>The Self Tracker</em></h1> -->
    <LoginVue></LoginVue>
  </div>
</template>

<script>
// @ is an alias to /src
import LoginVue from "@/components/LoginVue.vue";

export default {
  name: "LoginView",
  components: {
    LoginVue,
  },
};
</script>
<style>
h1 {
  background-color: darksalmon;
}
</style>
