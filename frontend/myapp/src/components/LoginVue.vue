<template>
  <div class="login">
    <!-- <h1><em>The Self Tracker</em></h1> -->
    <b-navbar toggleable="md" type="dark" variant="info">
      <b-navbar-brand href="/login">Login</b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item href="/">Home</b-nav-item>
        <b-nav-item href="/about">About</b-nav-item>
        <b-nav-item href="/register">Register</b-nav-item>
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
      <div>
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
      </div>
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
      try {
        fetch("http://127.0.0.1:5000/login", {//?include_auth_token", {
          method: "POST",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password,
          }),
        })
          .then((resp) => {
            return resp.json();
          })
          .then(async (login_data) => {
            const { response } = login_data;
            if (response.errors) {
              const { email, password } = response.errors;
              console.log({ email, password });
              this.error_email = email ? email[0] : "";
              this.error_password = password ? password[0] : "";
              console.log(this.error_email, this.error_password);
            } else {
              this.auth = response.user.authentication_token;
              sessionStorage.setItem(
                "auth-token",
                response.user.authentication_token
              );
              sessionStorage.setItem("email", this.email);
              this.$router.push("dashboard");
            }
          })
          .catch((error) => {
            console.log(error);
          });
      } catch (error) {
        console.log("Can't login in: ", error);
      }
    },
  },
}
</script>

