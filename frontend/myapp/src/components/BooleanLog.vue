<template>
    <div id="Boolean">
        <b-navbar toggleable="md" type="dark" variant="info">
            <b-navbar-brand href="#">Add Logs</b-navbar-brand>
            <b-navbar-nav>
                <b-nav-item href="/dashboard">Dashboard</b-nav-item>
                <b-nav-item @click="logout()">Logout</b-nav-item>
            </b-navbar-nav>
        </b-navbar>

        <body class="container">
            <form @submit.prevent="AddLogSubmit(id)">
                <h3 class="form text-center mt-2 mb-4">!!---Add Logs to your Tracker here---!!</h3>
                <!-- <div class="form-group">
                    <h5>Boolean Value:</h5>
                    <input id="log_value" type="number" min="0" v-model="log_value" ref="log_value"
                        class="form-control form-control-lg" placeholder="Value" required autocomplete="off" />
                </div> -->
                <div class="form-group">
                    <h5>Boolean Value</h5>
                    <b-form-group>
                        <b-form-radio-group id="log_value" v-model="log_value
                        " name="log_value">
                            <h5>
                                <b-form-radio value="Yes">Yes</b-form-radio>

                                <b-form-radio value="boolean">No</b-form-radio>
                            </h5>
                        </b-form-radio-group>
                    </b-form-group>
                </div>
                <div class="form-group">
                    <h5>Log Note:</h5>
                    <input id="log_note" type="text" v-model="log_note" ref="log_note"
                        class="form-control form-control-lg" placeholder="Log Note" required autocomplete="off" />

                </div>
                <button type="submit" class="btn btn-dark btn-lg btn-block">
                    Log it
                </button>
            </form>
            <h4 align="center">X----------LOG TABLE----------X</h4>
            <table align="center">
                <thead>
                    <tr>
                        <th>Log Value</th>
                        <th>Log Note</th>
                        <th>Last Logged at</th>
                        <th>Delete Log</th>
                        <th>Update Log</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="tracker in trck_result">
                        <td>{{ tracker.name }}</td>
                        <td>{{ tracker.description }}</td>
                        <td>{{ tracker.date_created }}</td>
                        <td>
                            <button type="button" class="btn btn-danger btn-lg"
                                @click="deleteLog(tracker.id)">Delete</button>
                        </td>
                        <td>
                            <router-link :to="`${email}/${id}/${log_id}/update`">
                                <button class="btn btn-success btn-lg">
                                    Update
                                </button>

                            </router-link>
                        </td>
                    </tr>
                </tbody>
            </table>
        </body>
    </div>
</template>
  
<script>
const baseURL = "http://127.0.0.1:5000"
export default {
    name: "BooleanLog",
    data() {
        return {
            log_id: null,
            trackerID: null,
            email: "",
            auth_token: "",
            log_value: null,
            log_note: "",

        }
    },
    async created() {
        this.auth_token = sessionStorage.getItem("authentication-token"),
            this.email = sessionStorage.getItem("email")
        this.trackerID = sessionStorage.getItem("id")
        // console.log(this.email)
        // console.log(this.auth_token)
    },
    methods: {
        async AddLogSubmit() {
            console.log(this.email)
            console.log(this.trackerID)
            const tracker_data = {
                log_value: this.log_value,
                log_note: this.log_note,
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

table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td {
    text-align: center;
}

th {
    border: 1px solid #dddddd;
    text-align: center;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
  