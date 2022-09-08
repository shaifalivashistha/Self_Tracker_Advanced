<template>
  <!-- <v-toolbar app color="brown darken-4" dark>
    <v-toolbar-side-icon></v-toolbar-side-icon>
    <v-toolbar-title>{{ appTitle }}</v-toolbar-title>
    <v-btn flat>Menu</v-btn>
    <v-spacer></v-spacer>
    <v-btn flat>SIGN IN</v-btn>
    <v-btn color="brown lighten-3">JOIN</v-btn>
  </v-toolbar> -->
  <div class="home">
    <img alt="Tracker logo" src="../assets/logo.jpeg" />
    <h1>
      New to The Self Tracker Application.
    </h1>
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
