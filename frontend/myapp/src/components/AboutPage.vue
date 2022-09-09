<template>
  <div id="aboutPage">
    <b-navbar toggleable="md" type="dark" variant="info">
      <b-navbar-brand href="/about">About</b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item href="/">Home</b-nav-item>
        <b-nav-item href="#">Contacts</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <h1>This is my about page.</h1>
  </div>
</template>

<script>
export default {
  name: "AboutPage",
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
