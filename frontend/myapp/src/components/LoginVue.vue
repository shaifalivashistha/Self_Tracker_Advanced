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
      <br />
      <h3 class="form text-center mt-2 mb-4">Login</h3>
      <div class="container">
        <p class="alert alert-danger" role="alert" v-if="error_mail">
          {{ error_mail }}
        </p>
        <p class="alert alert-danger" role="alert" v-if="error_pwd">
          {{ error_pwd }}
        </p>
      </div>
      <form @submit.prevent="formLogin">
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
        <button id="" class="btn btn-dark btn-lg btn-block">
          Login
        </button>
        <p>
          <router-link to="/forgot-password">Forgot password ?</router-link>
        </p>
        <p>New User <router-link to="/register">Sign Up?</router-link>
        </p>
      </form>
    </body>
  </div>
</template>
<script>

const baseURL = "http://127.0.0.1:5000";
export default {
  name: "LoginVue",
  data() {
    return {
      email: "",
      password: "",
      error_mail: "",
      error_pwd: "",
      auth: "",
      is_auth: false,
    };
  },
  methods: {
    async formLogin() {
      const user_data = {
        email: this.email,
        password: this.password
      };
      const request_options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
          "Access-Control-Allow-Origin": "*"
        },
        body: JSON.stringify(user_data)
      }

      try {
        const res = await fetch(`${baseURL}/login?include_auth_token`, request_options)

        if (res) {
          console.log("In first IF block")
          if (res.ok) {
            const data = await res.json().catch(() => {
              throw Error("Something Went Wrong")
            })
            if (data) {
              if (res.errors) {
                if (res.errors[1]) {
                  this.error_email = res.errors[1];
                }
                this.error_password = res.errors[0];

                console.log(this.error_email, this.error_password);
              }
              else {
                this.auth = res.user.authentication_token;
                sessionStorage.setItem(
                  "authentication-token",
                  res.user.authentication_token
                );
                sessionStorage.setItem("email", this.email);
                this.$router.push("dashboard");
                console.log("its dashboard");
              }
            }
            else {
              throw Error(res.statusText)
            }
          }
        }
      }
      catch (err) {
        console.log("Login Failed", err)
      }

      // const login_data = {
      //   email: this.email,
      //   password: this.password,
      // };
      // const request_options = {
      //   method: "POST",
      //   headers: {
      //     "Content-Type": "application/json;charset=utf-8",
      //   },
      //   body: JSON.stringify(login_data),
      // };
      // try {
      //   console.log("before fetch");
      //   const response = await fetch(
      //     `${baseURL}/login?include_auth_token`,
      //     request_options
      //   )
      //     // console.log("Passed")
      //     // console.log(response)
      //     // if (response) {
      //     //   console.log("first if")
      //     //   if (response.ok) {
      //     //     const data = await response.json().catch(() => {
      //     //       throw Error("Error message")
      //     //     })
      //     //     if (data) {
      //     //       if (response.errors) {
      //     //         if (response.errors[1]) {
      //     //           this.error_email = response.errors[1]
      //     //         }
      //     //         this.error_password = response.errors[0]
      //     //         console.log(this.error_email, this.error_password)
      //     //       }
      //     //       this.auth = response.user.authentication_token;
      //     //       sessionStorage.setItem(
      //     //         "auth-token",
      //     //         response.user.authentication_token
      //     //       );
      //     //       sessionStorage.setItem("email", this.email);
      //     //       this.$router.push("dashboard")
      //     //     }
      //     //   }
      //     // }
      //     .then((resp) => resp.json())
      //     .then(async (login_data) => {
      //       const { response } = login_data;
      //       console.log(login_data);

      // if (response.errors) {
      //   if (response.errors[1]) {
      //     this.error_email = response.errors[1];
      //   }
      //   this.error_password = response.errors[0];

      //   console.log(this.error_email, this.error_password);
      // } else {
      //   this.auth = response.user.authentication_token;
      //   sessionStorage.setItem(
      //     "authentication-token",
      //     response.user.authentication_token
      //   );
      //   sessionStorage.setItem("email", this.email);
      //   this.$router.push("dashboard");
      //   console.log("its dashboard");
      // }
      //     })
      // } catch (error) {
      //   console.log("In catch");
      //   console.log("Login unsuccessful: ", error);
      // }
    },
  },
};
</script>
  <!-- //   fetch(`${baseURL}/login?include_auth_token`, request_options)
  //     .then((resp) => {
  //      resp.json();
  //     })
  //     .then(async (login_data) => {
  //       const { response } = login_data;
  //       if (response.errors) {
  //         const { email, password } = response.errors;
  //         console.log({ email, password });
  //         this.error_email = email ? email[0] : "";
  //         this.error_password = password ? password[0] : "";
  //         console.log(this.error_email, this.error_password);
  //       } else {
  //         this.auth = response.user.authentication_token;
  //         sessionStorage.setItem(
  //           "auth-token",
  //           response.user.authentication_token
  //         );
  //         sessionStorage.setItem("email", this.email);
  //         this.$router.push("dashboard");
  //       }
  //     })
  //     .catch((error) => {
  //       console.log(error);
  //     });
  // } catch (error) {
  //   console.log("Can't login in: ", error);
  // } -->
