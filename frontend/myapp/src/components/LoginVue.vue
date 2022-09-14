<template>
  <div class="login">
    <h1><em>The Self Tracker</em></h1>
    <b-navbar toggleable="md" type="dark" variant="info">
      <b-navbar-brand href="/login">Login</b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item href="/">Home</b-nav-item>
        <b-nav-item href="/about">About</b-nav-item>
        <b-nav-item href="/register">Register</b-nav-item>
        <b-nav-item href="#">Contacts</b-nav-item>
      </b-navbar-nav>
    </b-navbar>

    <body class="container">
      <br>
      <h3 class="form text-center mt-2 mb-4">
        Login
      </h3>
      <div class="container">
        <p class="alert alert-danger" role="alert" v-if="error_email">
          {{ error_email }}
        </p>
        <p class="alert alert-danger" role="alert" v-if="error_password">
          {{ error_password }}
        </p>
      </div>
      <form>
        <div class="form-group">
          <label>Email address</label>
          <input v-model="email" id="email" type="email" class="form-control form-control-lg" placeholder="email"
            pattern="^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$" autocomplete="off" required />
        </div>
        <div class="form-group">
          <label>Password</label>
          <input v-model="password" id="password" type="password" class="form-control form-control-lg"
            placeholder="Password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" autocomplete="off" required />
        </div>
        <button type="submit" @click="login()" class="btn btn-dark btn-lg btn-block">
          Login
        </button>
        <p>
          <router-link to="/forgot-password">Forgot password ?</router-link>
        </p>
        <p>
          New User <router-link to="/register">Sign Up?</router-link>
        </p>
      </form>
    </body>
  </div>
</template>
<script>
export default {
  data() {
    return {
      email: '',
      password: '',
      error_email: '',
      error_password: '',
      auth: "",
      is_auth: false,
    };
  },
  methods: {
    async login() {
      this.$router.push('dashboard');
    }
  },
}
</script>
