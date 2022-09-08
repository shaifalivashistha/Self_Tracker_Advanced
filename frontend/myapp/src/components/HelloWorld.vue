<template>
  <div id="hello">
    <v-toolbar app color="brown darken-4" dark>
      <v-toolbar-side-icon></v-toolbar-side-icon>
      <v-toolbar-title>{{ appTitle }}</v-toolbar-title>
      <v-btn flat>Menu</v-btn>
      <v-spacer></v-spacer>
      <v-btn flat>SIGN IN</v-btn>
      <v-btn color="brown lighten-3">JOIN</v-btn>
    </v-toolbar>
    <h1>This is my home page.</h1>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
};
</script>
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
