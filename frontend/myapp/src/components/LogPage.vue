<template>
    <div id="add_logs">
        <b-navbar toggleable="md" type="dark" variant="info">
            <b-navbar-brand href="#">Add Logs</b-navbar-brand>
            <b-navbar-nav>
                <b-nav-item href="/dashboard/">Dashboard</b-nav-item>
                <b-nav-item @click="logout">Logout</b-nav-item>
            </b-navbar-nav>
        </b-navbar>

        <body class="container">
            <form @submit.prevent="AddLogSubmit">
                <h3 class="form text-center mt-2 mb-4">Create Your Tracker here</h3>
                <div class="form-group">
                    <h5>Log Name:</h5>
                    <input id="log_name" type="text" v-model="log_name" ref="log_name"
                        class="form-control form-control-lg" placeholder="Tracker Name" required autocomplete="off" />
                </div>
                <div class="form-group">
                    <h5>Log Value:</h5>
                    <input id="log_value" type="text" v-model="log_value" ref="log_value"
                        class="form-control form-control-lg" placeholder="Description" required autocomplete="off" />
                </div>
                <div class="form-group">
                    <h5>Log Note:</h5>
                    <input id="log_note" type="text" v-model="log_note" ref="log_note"
                        class="form-control form-control-lg" placeholder="Description" required autocomplete="off" />

                </div>
                <button type="submit" class="btn btn-dark btn-lg btn-block">
                    Add Logs
                </button>
            </form>
        </body>
    </div>
</template>
  
<script>
const baseURL = "http://127.0.0.1:5000"
export default {
    name: "AddLogs",
    data() {
        return {
            email: "",
            auth_token: "",
            tracker_name: "",
            tracker_des: "",
            tracker_type: "",

        }
    },
    async created() {
        this.auth_token = sessionStorage.getItem("authentication-token"),
            this.email = sessionStorage.getItem("email")
        // console.log(this.email)
        // console.log(this.auth_token)
    },
    methods: {
        async AddTrackerSubmit() {
            const tracker_data = {
                tracker_name: this.tracker_name,
                tracker_des: this.tracker_des,
                tracker_type: this.tracker_type
            }
            const requestOptions = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json;charset=utf-8",
                    "Authentication-Token": `${this.auth_token}`,
                },
                body: JSON.stringify(tracker_data)
            }
            try {
                const res = await fetch(`${baseURL}/${this.email}/${this.id}/logs`, requestOptions)

                if (res) {
                    console.log("post response fetch", res)
                    if (res.ok) {

                        const data = await res.json().catch(() => {
                            throw Error("Something Went Wrong")
                        })
                        if (data) {
                            console.log("post fetch data ->", data)
                            this.$router.push(`/dashboard/${this.email}`)
                            return data
                        }
                        else {
                            throw Error(res.statusText)
                        }
                    }
                }
            }
            catch (err) {
                console.log("Tracker Request failed", err)
            }
        },
        async logout() {

            console.log(this.auth_token)
            console.log("in logout")
            sessionStorage.removeItem("authentication-token")
            this.$router.push("login")

        }
    }
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
  