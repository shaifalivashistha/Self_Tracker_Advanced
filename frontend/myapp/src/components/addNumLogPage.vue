<template>
    <div id="Numerical">
        <b-navbar toggleable="md" type="dark" variant="info">
            <b-navbar-brand :to="`/dashboard/${username}`">{{username}}</b-navbar-brand>
            <b-navbar-nav>
                <b-nav-item :to="`/dashboard/${username}`">Dashboard</b-nav-item>
                <b-nav-item @click="logout()">Logout</b-nav-item>
            </b-navbar-nav>
        </b-navbar>
        <div>
            <button @click="ExportEvents()">Export Events</button>
        </div>

        <body class="container">
            <form @submit.prevent="addLogEntry()">
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
            <h4 align="center">X----------Logged Events----------X</h4>
            <table align="center">
                <thead>
                    <tr>
                        <th>Value</th>
                        <th>Note</th>
                        <th>Timestamp</th>
                        <th>Delete Event</th>
                        <th>Update Event</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="log_entry in log_data">
                        <td>{{ log_entry.value }}</td>
                        <td>{{ log_entry.note }}</td>
                        <td>{{ log_entry.timestamp }}</td>
                        <td>
                            <button type="button" class="btn btn-danger btn-lg"
                                @click="deleteLog(log_entry.logID)">Delete</button>
                        </td>
                        <td>
                            <router-link :to="`/${username}/${trackerID}/${log_entry.logID}/update`">
                                <button class="btn btn-success btn-lg"
                                    @click="updateLog(log_entry.logID, log_entry.log, log_entry.value, log_entry.note)">
                                    Update
                                </button>
                            </router-link>

                        </td>
                    </tr>
                </tbody>
            </table>
            <h4 align="center"> X----------Visualize----------X</h4>
            <div align="center">
                <img :src="'data:image/png;base64,' + this.file" />
            </div>
        </body>
    </div>
</template>
  
<script>
const baseURL = "http://127.0.0.1:5000"
export default {
    name: "addNumLogPage",
    data() {
        return {
            logID: null,
            trackerID: null,
            username: "",
            auth_token: "",
            log_value: null,
            log_note: "",
            log_data: {},
            file: "",
            error_txt: "",
            success_msg: "",
        }
    },
    async created() {
        this.auth_token = sessionStorage.getItem("authentication-token");
        this.username = sessionStorage.getItem("username");
        this.trackerID = sessionStorage.getItem("trackerID");
        const getRequestOptions = {
            methods: "GET",
            headers: {
                "Content-Type": "application/json;charset=utf-8",
                "Authentication-Token": `${this.auth_token}`
            }
        }
        try {
            if (!!this.auth_token) {
                await fetch(`${baseURL}/${this.username}/${this.trackerID}/logs`, getRequestOptions)
                    .then(async response => {
                        if (!response.ok) {
                            throw Error(response.statusText);
                        }
                        const myResp = await response.json();
                        if (!!myResp) {
                            if (myResp.resp == "ok") {
                                this.success_msg = myResp.msg;
                                this.log_data = myResp.stuff.logData;
                                this.file = myResp.stuff.encodedImage;
                            }
                            else {
                                throw Error(myResp.msg);
                            }
                        }
                        else {
                            throw Error("something went wrong (data not received)");
                        }
                    })
                    .catch(error => {
                        this.error_txt = error;
                        console.log("Could not retrieve log data. Error: ", error);
                    })
            }
            else {
                this.logout();
                throw Error("authentication failed.")
            }
        }
        catch (error) {
            this.error_txt = error;
            console.log("Could not retrieve log data. Error: ", error);
        }
    },
    methods: {
        async addLogEntry() {
            const temp_data = {
                trackerID: this.trackerID,
                log_value: this.log_value,
                log_note: this.log_note,
            }
            const addLogEntryRequestOptions = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json;charset=utf-8",
                    "Authentication-Token": `${this.auth_token}`,
                },
                body: JSON.stringify(temp_data)
            }
            try {
                if (!!this.auth_token) {
                    await fetch(`${baseURL}/${this.username}/${this.trackerID}/logs`, addLogEntryRequestOptions)
                        .then(async response => {
                            if (!response.ok) {
                                throw Error(response.statusText);
                            }
                            const myResp = await response.json();
                            if (!!myResp) {
                                if (myResp.resp == "ok") {
                                    this.success_msg = myResp.msg;
                                    this.$router.go();
                                }
                                else {
                                    throw Error(myResp.msg);
                                }
                            }
                            else {
                                throw Error("something went wrong (data not received)");
                            }
                        })
                        .catch(error => {
                            this.error_txt = error;
                            console.log("Could not add entry to log. Error: ", error);
                        })
                }
                else {
                    this.logout();
                    throw Error("authentication failed.")
                }
            }
            catch (error) {
                this.error_txt = error;
                console.log("Could not add entry to log. Error: ", error);
            }
        },
        async updateLog(logID, trackerType, value, note) {
            sessionStorage.setItem("logID", logID)
            sessionStorage.setItem("trackerType", trackerType)
            sessionStorage.setItem("log_value", value)
            sessionStorage.setItem("log_note", note)
        },
        async deleteLog(logID) {
            const deleteRequestOptions = {
                methods: "GET",
                headers: {
                    "Content-Type": "application/json;charset=utf-8",
                    "Authentication-Token": `${this.auth_token}`,
                }
            }
            try {
                if (!!this.auth_token) {
                    await fetch(`${baseURL}/${this.username}/${this.trackerID}/${logID}/delete`, deleteRequestOptions)
                        .then(async response => {
                            if (!response.ok) {
                                throw Error(response.statusText);
                            }
                            const myResp = await response.json();
                            if (!!myResp) {
                                if (myResp.resp == "ok") {
                                    this.success_msg = myResp.msg;
                                    this.$router.go();
                                }
                                else {
                                    throw Error(myResp.msg);
                                }
                            }
                            else {
                                throw Error("something went wrong (data not received)");
                            }
                        })
                        .catch(error => {
                            this.error_txt = error;
                            console.log("Could not delete entry from log. Error: ", error);
                        })
                }
                else {
                    this.logout();
                    throw Error("authentication failed.")
                }
            }
            catch (error) {
                this.error_txt = error;
                console.log("Could not delete entry from log. Error: ", error);
            }
        },
        async logout() {
            const logoutRequestOptions = {
                method: "GET",
                headers: {
                    "Content-Type": "application/json;charset=utf-8",
                    "Authentication-Token": `${this.auth_token}`,
                },
            };
            await fetch(`${baseURL}/logout`, logoutRequestOptions)
                .then(async response => {
                    if (!response.ok) {
                        throw Error(response.statusText);
                    }
                    const myResp = await response.json();
                    sessionStorage.clear()
                    this.success_msg = myResp.msg;
                    this.$router.push({ path: `/login_page` })
                })
                .catch(error => {
                    this.error_txt = error;
                    console.log("Could not log out. Error: ", error);
                });
        },
        async ExportEvents() {
            const temp_data = this.log_data
            const exportEventsRequestOptions = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json;charset=utf-8",
                    "Authentication-Token": `${this.auth_token}`,
                },
                body: JSON.stringify(temp_data)
            }
            try {
                // console.log("trying to fetch")
                // console.log(post_req_opt.body)
                if (!!this.auth_token) {
                    await fetch(`${baseURL}/${this.username}/${this.trackerID}/export_events`, exportEventsRequestOptions)
                        .then(async response => {
                            if (!response.ok) {
                                throw Error(response.statusText);
                            }
                            const myResp = await response.json();
                            if (!!myResp) {
                                if (myResp.resp == "ok") {
                                    this.success_msg = myResp.msg;
                                    this.$router.go();
                                }
                                else {
                                    throw Error(myResp.msg);
                                }
                            }
                            else {
                                throw Error("something went wrong");
                            }
                        })
                        .catch(error => {
                            this.error_txt = error;
                            console.log("Failed to export. Error: ", error);
                        });
                }
                else {
                    this.logout();
                    throw Error("authentication failed");
                }
            }
            catch (error) {
                this.error_txt = error;
                console.log("Failed to export. Error: ", error)
            }
        },
    }
}
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
  