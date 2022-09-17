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
                <h3 class="form text-center mt-2 mb-4">
                    Sign Up
                </h3>
                <div class="form-group">
                    <label>Username</label>
                    <input id="username" type="text" ref="username" class="form-control form-control-lg"
                        placeholder="Username" required autocomplete="off" />
                </div>
                <div class="form-group">
                    <label>Email address</label>
                    <input id="email" type="email" ref="email" class="form-control form-control-lg" placeholder="email"
                        pattern="^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$" required autocomplete="off" />
                </div>
                <p class="alert alert-danger" role="alert" v-if="error_email">
                    {{ error_email }}
                </p>
                <div class="form-group">
                    <label>Password</label>
                    <input id="password" type="password" ref="password" class="form-control form-control-lg"
                        placeholder="Password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" required
                        autocomplete="off" />
                </div>
                <button id="submit" @click="register" type="submit" class="btn btn-dark btn-lg btn-block">
                    Sign Up
                </button>
            </div>
        </body>
    </div>
</template>
<script>
const baseURL = "http://127.0.0.1:5000";

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
            const user_data = {
                username: this.$refs.username.value,
                email: this.$refs.email.value,
                password: this.$refs.password.value
            }
            const requestOptions = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json;charset=utf-8",
                },
                body: JSON.stringify(user_data),
            }
            try {
                console.log('Hello');
                // console.log(myOptions);
                const res = await fetch(`${baseURL}/register`, requestOptions)
                console.log(res)
                // .then((resp) => {
                //     console.log('HEllo then');
                //     // console.log(resp);
                //     resp.json();
                // })
                // .then((register_data) => {
                //     console.log('HEllo then2');
                //     // const response = register_data;
                //     if (register_data.errors) {
                //         console.log('HEllo if');
                //         const { email, password } = register_data.errors;
                //         console.log({ email, password });
                //         this.error_email = email ? email[0] : "";
                //         this.error_password = password ? password[0] : "";
                //         console.log(this.error_email, this.error_password);
                //     } else {
                //         console.log('HEllo else');
                //         this.$router.push("login");
                //     }
                // })
                // .catch((error) => {
                //     console.log('HEllo ctch');
                //     console.log(error);
                // });
                // console.log(res)
                if (!res.ok) {
                    const message = `An error has occured: ${res.status} - ${res.statusText}`;
                    throw new Error(message);
                }
                console.log('Here 1121')
                // const data = await res.json();
                // console.log('Here')
                // const result = {
                //     status: res.status + "-" + res.statusText,
                //     headers: {
                //         "Content-Type": res.headers.get("Content-Type"),
                //         "Content-Length": res.headers.get("Content-Length"),
                //     },
                //     data: data,
                // };
                // console.log('Here 1')
            } catch (error) {
                console.log('Hello real ctch');
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
  