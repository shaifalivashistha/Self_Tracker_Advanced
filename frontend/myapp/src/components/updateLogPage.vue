<template>
    <div id="UpdateLog">
        <b-navbar toggleable="md" type="dark" variant="info">
            <b-navbar-brand :to="`/dashboard/${username}`">{{username}}</b-navbar-brand>
            <b-navbar-nav>
                <b-nav-item :to="`/dashboard/${username}`">Dashboard</b-nav-item>
                <b-nav-item @click="logout()">Logout</b-nav-item>
            </b-navbar-nav>
        </b-navbar>

        <body class="container">
            <div v-if="trackerType == 'numeric'">
                <form @submit.prevent="updateNumericLog(logID)">
                    <h3 class="form text-center mt-2 mb-4">Update your logs here</h3>
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
            <div v-else>
                <form @submit.prevent="updateBooleanLog(logID)">
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
                            class="form-control form-control-lg" placeholder='' required autocomplete="off" />
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
    name: "updateLogPage",
    data() {
        return {
            logID: null,
            trackerID: null,
            username: "",
            auth_token: "",
            log_value: null,
            log_note: "",
            trackerType: "",
            error_txt: "",
            success_msg: "",
        }
    },
    async created() {

        this.auth_token = sessionStorage.getItem("authentication-token");
        this.username = sessionStorage.getItem("username");
        this.log_value = sessionStorage.getItem("log_value");
        this.log_note = sessionStorage.getItem("log_note");
        this.logID = sessionStorage.getItem("logID");
        this.trackerID = sessionStorage.getItem("trackerID");
        this.trackerType = sessionStorage.getItem("trackerType");

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
        async updateBooleanLog(logID) {
            const temp_data = {
                log_value: this.log_value,
                log_note: this.log_note
            }
            const updateRequestOptions = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json;charset=utf-8",
                    "Authentication-Token": `${this.auth_token}`,
                },
                body: JSON.stringify(temp_data)
            }
            try {
                if (!!this.auth_token) {
                    await fetch(`${baseURL}/${this.username}/${this.trackerID}/${logID}/update`, updateRequestOptions)
                        .then(async response => {
                            if (!response.ok) {
                                throw Error(response.statusText);
                            }
                            const myResp = await response.json();
                            if (!!myResp) {
                                if (myResp.resp == "ok") {
                                    this.success_msg = myResp.msg;
                                    sessionStorage.removeItem("logID");
                                    sessionStorage.removeItem("log_value");
                                    sessionStorage.removeItem("log_note");
                                    sessionStorage.removeItem("trackerType");
                                    this.$router.push({ path: `/${this.username}/${this.trackerID}/boolean` })
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
                            console.log("Could not update log. Error: ", error);
                        })
                }
                else {
                    this.logout();
                    throw Error("authentication failed.")
                }
            }
            catch (error) {
                this.error_txt = error;
                console.log("Could not update log. Error: ", error);
            }
        },
        async updateNumericLog(logID) {
            const temp_data = {
                log_value: this.log_value,
                log_note: this.log_note
            }
            const updateRequestOptions = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json;charset=utf-8",
                    "Authentication-Token": `${this.auth_token}`,
                },
                body: JSON.stringify(temp_data)
            }
            try {
                if (!!this.auth_token) {
                    await fetch(`${baseURL}/${this.username}/${this.trackerID}/${logID}/update`, updateRequestOptions)
                        .then(async response => {
                            if (!response.ok) {
                                throw Error(response.statusText);
                            }
                            const myResp = await response.json();
                            if (!!myResp) {
                                if (myResp.resp == "ok") {
                                    this.success_msg = myResp.msg;
                                    sessionStorage.removeItem("logID");
                                    sessionStorage.removeItem("log_value");
                                    sessionStorage.removeItem("log_note");
                                    sessionStorage.removeItem("trackerType");
                                    this.$router.push({ path: `/${this.username}/${this.trackerID}/numeric` })
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
                            console.log("Could not update log. Error: ", error);
                        })
                }
                else {
                    this.logout();
                    throw Error("authentication failed.")
                }
            }
            catch (error) {
                this.error_txt = error;
                console.log("Could not update log. Error: ", error);
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
                    this.success_msg = myResp.msg;
                })
                .catch(error => {
                    this.error_txt = error;
                    console.log("Could not log out. Error: ", error);
                });
            await fetch(`${baseURL}/logout_page`, logoutRequestOptions)
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
  