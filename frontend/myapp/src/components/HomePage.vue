<template>
  <div id="homePage">
    <b-navbar fixed="top" toggleable="md" type="dark" variant="info">
      <b-navbar-brand :to="`/`">Tracker</b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item href="/about">About</b-nav-item>
        <b-nav-item href="/register">Register</b-nav-item>
        <b-nav-item href="/login_page">Login</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <h1>This is my home page.</h1>
  </div>
</template>

<script>
export default {
  name: "HomePage",
  beforeMount() {
    sessionStorage.clear();
  },
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
