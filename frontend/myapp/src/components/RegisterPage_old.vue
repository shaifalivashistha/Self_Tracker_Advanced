<template>
  <div class="login">
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
      <form>
        <h3 class="form text-center mt-2 mb-4">
          Sign Up
        </h3>
        <div class="form-group">
          <label>Username</label>
          <input id="username" type="text" v-model="username" class="form-control form-control-lg"
            placeholder="Username" required autocomplete="off" />
        </div>
        <div class="form-group">
          <label>Email address</label>
          <input id="email" type="email" v-model="email" class="form-control form-control-lg" placeholder="email"
            pattern="^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$" required autocomplete="off" />
        </div>
        <p class="alert alert-danger" role="alert" v-if="error_email">
          {{ error_email }}
        </p>
        <div class="form-group">
          <label>Password</label>
          <input id="password" type="password" v-model="password" class="form-control form-control-lg"
            placeholder="Password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" required autocomplete="off" />
        </div>
        <button id="submit" @click="register" type="submit" class="btn btn-dark btn-lg btn-block">
          Sign Up
        </button>
      </form>
    </body>
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
    // async register() {
    //   try {
    //     fetch("http://127.0.0.1:5000/register", {
    //       method: "POST",
    //       headers: {
    //         "Access-Control-Allow-Origin": "*",
    //         "Content-Type": "application/json;charset=utf-8",
    //       },
    //       body: JSON.stringify({
    //         email: this.email,
    //         username: this.username,
    //         password: this.password,
    //       }),
    //     })
    //       .then((resp) => resp.json())
    //       .then(async (register_data) => {
    //         console.log(register_data);
    //         if (!this.username) {
    //           this.error_email = "Please enter a valid username";
    //         }
    //         if (this.password == "") {
    //           this.error_password = "Enter a valid password";
    //         } else {
    //           this.$router.push("login");
    //         }
    //         if (!this.email) {
    //           this.error_email = "Please enter a valid email";
    //           console.log("wrong mail");
    //         } else if (!this.validEmail(this.email)) {
    //           this.error_email = "Not valid email";
    //         }
    //       })
    //       .catch((error) => {
    //         console.log(error);
    //       });
    //   } catch (error) {
    //     console.log("Registration unsuccessful: ", error);
    //   }
    // },
    // validEmail: function (email) {
    //   var re =
    //     /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    //   return re.test(email);
    // },
    // validPassword: function () {
    //   var pass = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/
    //   if (this.password.value.match(pass)) {
    //     letter.classList.remove("invalid");
    //     letter.classList.add("valid");
    //   } else {
    //     letter.classList.remove("valid");
    //     letter.classList.add("invalid");
    //   }
    // },
    async register() {
      try {
        console.log('HEllo');
        const myOptions = {
          // mode: "no-cors",
          method: "POST",
          headers: {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json;charset=utf-8",
          },
          body: JSON.stringify({
            username: this.username,
            email: this.email,
            password: this.password
          }),
        }
        // console.log(myOptions);
        fetch("http://127.0.0.1:5000/register", myOptions)
          .then((resp) => {
            console.log('HEllo then');
            console.log(resp);
            return resp.json();
          })
          .then(async (register_data) => {
            console.log('HEllo then2');
            const { response } = register_data;
            if (response.errors) {
              console.log('HEllo if');
              const { email, password } = response.errors;
              console.log({ email, password });
              this.error_email = email ? email[0] : "";
              this.error_password = password ? password[0] : "";
              console.log(this.error_email, this.error_password);
            } else {
              console.log('HEllo else');
              this.$router.push("login");
            }
          })
          .catch((error) => {
            console.log('HEllo ctch');
            console.log(error);
          });
      } catch (error) {
        console.log('HEllo real ctch');
        console.log("Registration unsuccessful: ", error);
      }
    },
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
