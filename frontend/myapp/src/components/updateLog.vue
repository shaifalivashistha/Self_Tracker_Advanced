<template>
    <div id="update_log">
        <b-navbar toggleable="md" type="dark" variant="info">
            <b-navbar-brand href="#">Add Trackers</b-navbar-brand>
            <b-navbar-nav>
                <b-nav-item href="/dashboard">Dashboard</b-nav-item>
                <b-nav-item @click="logout()">Logout</b-nav-item>
            </b-navbar-nav>
        </b-navbar>

        <body class="container">
            <div>
                <form @submit.prevent="UpdateNumericLog()">
                    <h3 class="form text-center mt-2 mb-4">Create Your Tracker here</h3>
                    <div class="form-group">
                        <h5>Log Value</h5>
                        <input id="log_value" type="number" v-model="log_value" ref="log_value"
                            class="form-control form-control-lg" placeholder="Log Value" required autocomplete="off" />
                    </div>
                    <div class="form-group">
                        <h5>Log Note:</h5>
                        <input id="log_note" type="text" v-model="log_note" ref="log_note"
                            class="form-control form-control-lg" placeholder="log note" required autocomplete="off" />
                    </div>
                    <button type="submit" class="btn btn-dark btn-lg btn-block">
                        Update Log
                    </button>
                </form>
            </div>
            <div>
                <form @submit.prevent="UpdateBooleanLog()">
                    <h3 class="form text-center mt-2 mb-4">Update your logs</h3>
                    <div class="form-group">
                        <div class="form-group">
                            <div>
                                <h5>Log Value:</h5>
                                <b-form-group>
                                    <b-form-radio-group id="log_value" v-model="log_value
                                    " name="radio-options">
                                        <b-form-radio value="Yes">Yes</b-form-radio>
                                        <b-form-radio value="No">No</b-form-radio>
                                    </b-form-radio-group>
                                </b-form-group>
                            </div>

                        </div>
                        <h5>Log Note</h5>
                        <input id="log_note" type="text" v-model="log_note" ref="log_note"
                            class="form-control form-control-lg" placeholder="Log Note" required autocomplete="off" />
                    </div>
                    <button type="submit" class="btn btn-dark btn-lg btn-block">
                        Update Log
                    </button>
                </form>
            </div>
        </body>
    </div>
</template>
  
<script>
const baseURL = "http://127.0.0.1:5000"
export default {
    name: "UpdateLog",
    data() {
        return {
            trackerID: null,
            email: "",
            auth_token: "",
            log_value: null,
            log_note: "",
            tracker_type: "",

        }
    },
    async created() {

        this.auth_token = sessionStorage.getItem("authentication-token"),
            this.email = sessionStorage.getItem("email")
        this.trackerID = sessionStorage.getItem("id")
        this.tracker_type = sessionStorage.getItem("tracker_type")

    },
    methods: {
        async UpdateBooleanLog() {
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
                const res = await fetch(`${baseURL}/dashboard/${this.email}/create_tracker`, requestOptions)

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
            this.$router.go('login')

        },
        async UpdateNumericLog() {
            console.log("numeric log updates")
            return ""
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
  