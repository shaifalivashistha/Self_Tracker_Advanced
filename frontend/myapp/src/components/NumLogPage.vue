<template>
    <div id="Numerical">
        <b-navbar toggleable="md" type="dark" variant="info">
            <b-navbar-brand href="#">Add Logs</b-navbar-brand>
            <b-navbar-nav>
                <b-nav-item href="/dashboard">Dashboard</b-nav-item>
                <b-nav-item @click="logout()">Logout</b-nav-item>
            </b-navbar-nav>
        </b-navbar>

        <body class="container">
            <form @submit.prevent="AddLogSubmit()">
                <h3 class="form text-center mt-2 mb-4">!!---Add Logs to your Tracker here---!!</h3>
                <div class="form-group">
                    <h5>Log Value:</h5>
                    <input id="log_value" type="number" min="0" v-model="log_value" ref="log_value"
                        class="form-control form-control-lg" placeholder="Log Value" required autocomplete="off" />
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
                    <tr v-for="log in log_result">
                        <td>{{ log.value }}</td>
                        <td>{{ log.note }}</td>
                        <td>{{ log.timestamp }}</td>
                        <td>
                            <button type="button" class="btn btn-danger btn-lg"
                                @click="deleteLog(log.log_id)">Delete</button>
                        </td>
                        <td>
                            <router-link :to="`/${email}/${trackerID}/${log.log_id}/update`">
                                <button class="btn btn-success btn-lg"
                                    @click="updateLog(log.log_id, log.log, log.value, log.note)">
                                    Update
                                </button>
                            </router-link>

                        </td>
                    </tr>
                </tbody>
            </table>
            <h4 align="center"> X----------LOG GRAPH----------X</h4>
            <div align="center">
                <img src="../assets/graph.png" alt="log_graph">
            </div>
        </body>
    </div>
</template>
  
<script>
const baseURL = "http://127.0.0.1:5000"
export default {
    name: "NumLogPage",
    data() {
        return {
            logID: null,
            trackerID: null,
            email: "",
            auth_token: "",
            log_value: null,
            log_note: "",
            log_result: {},


        }
    },
    async created() {
        this.auth_token = sessionStorage.getItem("authentication-token"),
            this.email = sessionStorage.getItem("email")
        this.trackerID = sessionStorage.getItem("id")
        console.log(this.trackerID)
        const get_req_opt = {
            methods: "GET",
            headers: {
                "Content-Type": "application/json;charset=utf-8",
                "Authentication-Token": `${this.auth_token}`
            }
        }
        try {
            const get_res = await fetch(`${baseURL}/${this.email}/${this.trackerID}/logs`, get_req_opt)
            console.log("sending get request")
            if (this.auth_token) {
                if (get_res) {
                    console.log("getting response fron get")
                    console.log(get_res)
                    if (get_res.ok) {

                        console.log("getting response fron get is ok")
                        const get_data = await get_res.json().catch(() => {
                            throw Error("Something Went Wrong")
                        })
                        if (get_data) {
                            this.log_result = get_data
                            console.log(this.log_result)
                        }
                    }
                }
            }
        }
        catch (err) {
            console.log(err)
        }
    },
    methods: {
        async AddLogSubmit() {
            console.log(this.email)
            console.log(this.trackerID)
            const log_data = {
                trackerID: this.trackerID,
                log_value: this.log_value,
                log_note: this.log_note,
            }
            const postRequestOptions = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json;charset=utf-8",
                    "Authentication-Token": `${this.auth_token}`,
                },
                body: JSON.stringify(log_data)
            }
            try {
                const post_res = await fetch(`${baseURL}/${this.email}/${this.trackerID}/logs`, postRequestOptions)

                if (post_res) {
                    console.log("post response fetch", post_res)
                    if (post_res.ok) {

                        const data = await post_res.json().catch(() => {
                            throw Error("Something Went Wrong")
                        })
                        if (data) {
                            this.$router.go()
                            return data
                        }
                        else {
                            throw Error(post_res.statusText)
                        }
                    }
                }
            }
            catch (err) {
                console.log("Tracker Request failed", err)
            }
        },
        async updateLog(id, type, value, note) {
            sessionStorage.setItem("logID", id)
            sessionStorage.setItem("trackerType", type)
            sessionStorage.setItem("log_value", value)
            sessionStorage.setItem("log_note", note)
            console.log(id)
            console.log(type)
            console.log(value)
            console.log(note)
        },
        async deleteLog(id) {
            const del_req_opt = {
                methods: "GET",
                headers: {
                    "Content-Type": "application/json;charset=utf-8",
                    "Authentication-Token": `${this.auth_token}`,
                }
            }
            try {
                console.log("delete trying before fetch")
                const res = await fetch(`${baseURL}/${this.email}/${this.trackerID}/${id}/delete`, del_req_opt)
                console.log("delete trying after fetch")
                if (this.auth_token) {
                    console.log("auth token check")
                    if (res) {
                        console.log("have response")
                        if (res.ok) {
                            console.log("Tracker Deleted Successfully")
                            this.$router.push(`/${this.email}/${this.trackerID}/logs`)
                        }
                    }
                    else {
                        throw Error(res.statusText)
                    }
                }
                else {
                    this.$router.push('login')
                    throw Error("Authentication Failed!! Login Again.")
                }
            }
            catch (err) {
                console.log("Error in delete", err)
            }
        },
        async logout() {
            sessionStorage.clear()
            this.$router.push("/")
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
  