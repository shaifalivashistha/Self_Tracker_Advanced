<template>
  <div class="registerPage">
    <b-navbar toggleable="md" type="dark" variant="info">
      <b-navbar-brand href="/register">Register</b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item href="/">Home</b-nav-item>
        <b-nav-item href="/about">About</b-nav-item>
        <b-nav-item href="/login">Login</b-nav-item>
        <b-nav-item href="#">Contacts</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <form>
      <h3>Register</h3>

      <div class="form-group">
        <label>Full Name</label>
        <input type="text" class="form-control form-control-lg" />
      </div>

      <div class="form-group">
        <label>Email address</label>
        <input type="email" class="form-control form-control-lg" />
      </div>

      <div class="form-group">
        <label>Password</label>
        <input type="password" class="form-control form-control-lg" />
      </div>

      <button type="submit" class="btn btn-dark btn-lg btn-block">
        Sign Up
      </button>

      <p class="forgot-password text-right">
        Already registered
        <router-link :to="{ name: 'login' }">Log in ?</router-link>
      </p>
    </form>
  </div>
</template>

<script>
export default {
  name: "RegisterPage",
  data() {
    return {};
  },
};
</script>
