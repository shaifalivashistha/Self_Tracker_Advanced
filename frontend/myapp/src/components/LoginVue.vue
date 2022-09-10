<!-- <template>
  <div class="loginPage">
    <b-navbar toggleable="md" type="dark" variant="info">
      <b-navbar-brand href="/login">Login</b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item href="/">Home</b-nav-item>
        <b-nav-item href="/about">About</b-nav-item>
        <b-nav-item href="/register">Register</b-nav-item>
        <b-nav-item href="#">Contacts</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <form>
      <h3>Login</h3>
      <div class="form-group">
        <label>Email address</label>
        <input type="email" class="form-control form-control-lg" />
      </div>
      <div class="form-group">
        <label>Password</label>
        <input type="password" class="form-control form-control-lg" />
      </div>
      <button type="submit" class="btn btn-dark btn-lg btn-block">Login</button>
      <p class="forgot-password text-right">
        Already registered
        <router-link :to="{ name: 'login' }">sign in?</router-link>
      </p>
    </form>
  </div>
</template>

<script>
export default {
  name: "LoginVue",
};
</script>
<style lang="scss">
body {
  margin: 0;
  padding: 0;
  font-family: 1.6rem/1.25 "Helvetica Neue", Helvetica, Arial, sans-serif;
  background-color: #f5f5f5;
}

.box {
  width: 300px;
  padding: 30px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: rgba(0, 0, 0, 0.4);
  text-align: center;
}

.box h1 {
  color: white;
  text-transform: uppercase;
  font-weight: 700;
}

.box input[type="text"],
.box input[type="password"] {
  border: 0;
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 3px solid #0367fd;
  padding: 14px 10px;
  width: 220px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25px;
}

.box input[type="text"]:focus,
.box input[type="password"]:focus {
  width: 270px;
  border-color: #ffc400ec;
}

.box input[type="submit"] {
  border: 0;
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 3px solid #ffc400ec;
  padding: 14px 35px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25px;
  cursor: pointer;
}

.box input[type="submit"]:hover {
  background: #ffc400ec;
}
</style> -->

<template>
  <div class="login">
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
      <form class="form">
        <h3>Login</h3>
        <div class="form-group">
          <label>Email address</label>
          <input type="email" class="form-control form-control-lg" />
        </div>
        <div class="form-group">
          <label>Password</label>
          <input type="password" class="form-control form-control-lg" />
        </div>
        <button type="submit" class="btn btn-dark btn-lg btn-block">
          Login
        </button>
        <p class="forgot-password text-right mt-2 mb-4">
          <router-link to="/forgot-password">Forgot password ?</router-link>
        </p>
      </form>
    </body>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
};
</script>
