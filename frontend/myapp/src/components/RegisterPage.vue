<!-- <template>
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
</script> -->

<template>
  <div class="container">
    <b-navbar toggleable="md" type="dark" variant="info">
      <b-navbar-brand href="/register">Register</b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item href="/">Home</b-nav-item>
        <b-nav-item href="/about">About</b-nav-item>
        <b-nav-item href="/login">Login</b-nav-item>
        <b-nav-item href="#">Contacts</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <p class="alert alert-danger" role="alert" v-if="error_email">
      {{ error_email }}
    </p>
    <p class="alert alert-danger" role="alert" v-if="error_password">
      {{ error_password }}
    </p>
    <div class="row">
      <div class="col"></div>
      <div class="col-5">
        <br />
        <h2 class="title" align="center">Create new account</h2>
        <br />
        <div class="form-row">
          <div class="form-group">
            <input
              type="email"
              class="form-control"
              name="email"
              id="email"
              v-model="email"
              required
              placeholder="email"
            />
          </div>
        </div>
        <br />
        <div class="form-row">
          <div class="form-group">
            <input
              type="text"
              class="form-control"
              name="username"
              id="username"
              v-model="username"
              required
              placeholder="username"
            />
          </div>
        </div>
        <br />
        <div class="form-row">
          <div class="form-group">
            <input
              type="password"
              class="form-control"
              name="password"
              id="password"
              v-model="password"
              required
              placeholder="password"
              autocomplete="off"
            />
          </div>
        </div>
        <br />
        <button @click="register()" class="btn btn-primary">Register</button>
        <br /><br />
        <p>Already have an account? Go to <a href="login">Login</a></p>
      </div>
      <div class="col"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserRegister",
  data() {
    return {
      email: null,
      password: "",
      error_email: "",
      error_password: "",
      username: null,
    };
  },
  methods: {
    async register() {
      try {
        fetch("http://127.0.0.1:5000/api/user", {
          method: "POST",
          headers: {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json;charset=utf-8",
          },
          body: JSON.stringify({
            email: this.email,
            username: this.username,
            password: this.password,
          }),
        })
          .then((resp) => resp.json())
          .then(async (register_data) => {
            // const { response } = register_data;
            console.log(register_data);
            // console.log(response)
            if (!this.username) {
              this.error_email = "Please enter a valid username";
            }
            if (this.password == "") {
              this.error_password = "Enter a valid password";
            } else {
              this.$router.push("login");
            }
            if (!this.email) {
              this.error_email = "Please enter a valid email";
              console.log("wrong mail");
            } else if (!this.validEmail(this.email)) {
              this.error_email = "Not valid email";
            }
            // this.$router.push("login");
          })
          .catch((error) => {
            console.log(error);
          });
      } catch (error) {
        console.log("Registration unsuccessful: ", error);
      }
    },
    validEmail: function (email) {
      var re =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
  },
};
</script>

<style scoped></style>
