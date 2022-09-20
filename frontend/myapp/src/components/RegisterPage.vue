<template>
  <div class="signup">
    <b-navbar toggleable="md" type="dark" variant="info">
      <b-navbar-brand href="/register">Sign Up</b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item href="/">Home</b-nav-item>
        <b-nav-item href="/login">Login</b-nav-item>
        <b-nav-item href="/about">About</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <p class="alert alert-danger" role="alert" v-if="error_email">
      {{ error_email }}
    </p>
    <p class="alert alert-danger" role="alert" v-if="error_password">
      {{ error_password }}
    </p>

    <body class="container">
      <div>
        <h3 class="form text-center mt-2 mb-4">Sign Up</h3>
        <div class="form-group">
          <label>Username</label>
          <input id="username" type="text" v-model="username" ref="username" class="form-control form-control-lg"
            placeholder="Username" required autocomplete="off" />
        </div>
        <div class="form-group">
          <label>Email address</label>
          <input id="email" type="email" v-model="email" ref="email" class="form-control form-control-lg"
            placeholder="email" pattern="^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$" required autocomplete="off" />
        </div>
        <p class="alert alert-danger" role="alert" v-if="error_email">
          {{ error_email }}
        </p>
        <div class="form-group">
          <label>Password</label>
          <input id="password" type="password" v-model="password" ref="password" class="form-control form-control-lg"
            placeholder="Password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" required autocomplete="off" />
        </div>
        <button id="submit" @click="signup" type="submit" class="btn btn-dark btn-lg btn-block">
          Sign Up
        </button>
      </div>
    </body>
  </div>
</template>
<script>
const baseURL = "http://127.0.0.1:5000";

export default {
  name: "RegisterPage",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      error_email: "",
      error_password: "",
    };
  },
  methods: {
    // async register() {
    //   try {
    //     fetch("http://127.0.0.1:5000/register", {
    //       method: "POST",
    //       headers: {
    //         "Access-Control-Allow-Origin": "*",
    //         "Content-Type": "application/json;charset=utf-8",
    //       },
    //       body: JSON.stringify({ email: this.$refs.email.value, username: this.$refs.username.value, password: this.$refs.password.value }),
    //     }).then((resp) => resp.json())
    //       .then(async (register_data) => {
    //         console.log(register_data);
    //         this.$router.push("login")
    //       }).catch((error) => {
    //         console.log(error);
    //       });
    //   } catch (error) {
    //     console.log("Registration unsuccessful: ", error);
    //   }
    // },



    // async register() {
    //     try {
    //         const data = {
    //             username: this.username,
    //             email: this.email,
    //             password: this.password
    //         }
    //         const request_options = {
    //             method: "POST",
    //             headers: {
    //                 "Access-Control-Allow-Origin": "*",
    //                 "Content-Type": "application/json;charset=utf-8",
    //             },
    //             body: JSON.stringify(data),
    //         }
    //         console.log("before fetch")
    //         const response = await fetch(`${baseURL}/register`, request_options)
    //             .then((resp) => {
    //                 console.log("after fetch then 1")
    //                 resp.json()
    //             }
    //             ).
    //             then(async (register_data) => {
    //                 if (!this.username) { this.error_email = "Invalid Username" }
    //                 if (this.password == "") { this.error_password = "Enter a valid password" }
    //                 else {
    //                     this.$router.push("login");
    //                 }
    //                 if (!this.email) {
    //                     this.error_email = "Please enter a valid email"
    //                     console.log("wrong mail");
    //                 } else if (!this.validEmail(this.email)) {
    //                     this.error_email = "Not valid email"
    //                 }
    //             });
    //     }
    //     catch (error) {
    //         console.log("Try catch")
    //         console.log('Hello real ctch');
    //         console.log("Registration unsuccessful: ", error);
    //     }
    // }




    async signup() {
      const user_data = {
        username: this.$refs.username.value,
        email: this.$refs.email.value,
        password: this.$refs.password.value,
      };
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
        },
        body: JSON.stringify(user_data),
      };
      try {
        console.log("Hello");
        console.log(user_data);
        const res = await fetch(`${baseURL}/register`, requestOptions);
        console.log("Passed");
        console.log(res);
        if (res) {
          console.log("first if");
          if (res.ok) {
            // const message = `An error has occured: ${res.status} - ${res.statusText}`;
            const data = await res.json().catch(() => {
              throw Error("Error message");
            });
            if (data) {
              this.$router.push("login")
              console.log(data);
              return data;
            } else {
              throw Error(res.statusText);
            }
          }
        }
        console.log("Here 1121");
      } catch (error) {
        console.log("Hello real ctch");
        console.log("Registration unsuccessful: ", error);
      }
    },



    // async register() {
    //     const user_data = {
    //         username: this.$refs.username.value,
    //         email: this.$refs.email.value,
    //         password: this.$refs.password.value
    //     }
    //     const requestOptions = {
    //         method: "POST",
    //         headers: {
    //             "Content-Type": "application/json;charset=utf-8",
    //         },
    //         body: JSON.stringify(user_data),
    //     }
    //     try {
    //         console.log('Hello');
    //         console.log(user_data)
    //         const res = await fetch(`${baseURL}/register`, requestOptions)
    //         console.log('Passed')
    //         console.log(res)
    //         if (!res.ok) {
    //             const message = `An error has occured: ${res.status} - ${res.statusText}`;
    //             throw new Error(message);
    //         }

    //         console.log('Here 1121')
    //     } catch (error) {
    //         console.log('Hello real ctch');
    //         console.log("Registration unsuccessful: ", error);
    //     }
    // },
  },
};
</script>

<style scoped lang="scss">
h3 {
  text-align: center;
}

.invalid {
  color: red;
}
</style>
