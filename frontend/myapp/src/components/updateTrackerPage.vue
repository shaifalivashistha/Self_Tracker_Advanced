<template>
    <div id="updateTracker">
        <b-navbar toggleable="md" type="dark" variant="info">
            <b-navbar-brand :to="`/dashboard/${username}`">{{username}}</b-navbar-brand>
            <b-navbar-nav>
                <b-nav-item :to="`/dashboard/${username}`">Dashboard</b-nav-item>
                <b-nav-item @click="logout()">Logout</b-nav-item>
            </b-navbar-nav>
        </b-navbar>

        <body class="container">
            <form @submit.prevent="updateTrackerMethod(trackerID)">
                <h3 class="form text-center mt-2 mb-4">x---Update Your Tracker---x</h3>
                <div class="form-group">
                    <h5>Tracker Name:</h5>
                    <input id="tracker_name" type="text" v-model="tracker_name" ref="tracker_name"
                        class="form-control form-control-lg" placeholder="Tracker Name" required autocomplete="off" />
                </div>
                <div class="form-group">
                    <h5>Tracker Description:</h5>
                    <input id="tracker_des" type="text" v-model="tracker_des" ref="tracker_des"
                        class="form-control form-control-lg" placeholder="Description" required autocomplete="off" />
                </div>
                <button type="submit" class="btn btn-dark btn-lg btn-block">
                    Update Tracker
                </button>
            </form>
        </body>
    </div>
</template>
  
<script>
const baseURL = "http://127.0.0.1:5000"
export default {
    name: "updateTrackerPage",
    data() {
        return {
            trackerID: null,
            username: "",
            auth_token: "",
            tracker_data: {},
            tracker_name: "",
            tracker_des: "",
            tracker_type: "",
            error_text: "",
            success_msg: "",
        }
    },
    async created() {
        this.auth_token = sessionStorage.getItem("authentication-token");
        this.username = sessionStorage.getItem("username");
        this.trackerID = sessionStorage.getItem("trackerID");
        this.tracker_name = sessionStorage.getItem("trackerName");
        this.tracker_des = sessionStorage.getItem("trackerDescription")
        const getRequestOptions = {
            methods: "GET",
            headers: {
                "Content-Type": "application/json;charset=utf-8",
                "Authentication-Token": `${this.auth_token}`
            }
        }
        try {
            if (!!this.auth_token) {
                await fetch(`${baseURL}/dashboard/${this.username}`, getRequestOptions)
                    .then(async response => {
                        if (!response.ok) {
                            throw Error(response.statusText);
                        }
                        const myResp = await response.json();
                        if (!!myResp) {
                            if (myResp.resp == "ok") {
                                this.success_msg = myResp.msg;
                                this.tracker_data = myResp.stuff;
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
                        console.log("Could not retrieve tracker data. Error: ", error);
                    })
            }
            else {
                this.logout();
                throw Error("authentication failed.")
            }
        }
        catch (error) {
            this.error_txt = error;
            console.log("Could not retrieve tracker data. Error: ", error);
        }
    },
    methods: {
        async updateTrackerMethod(trackerID) {
            const tracker_data = {
                tracker_name: this.tracker_name,
                tracker_des: this.tracker_des,
            }
            const updateRequestOptions = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json;charset=utf-8",
                    "Authentication-Token": `${this.auth_token}`,
                },
                body: JSON.stringify(tracker_data)
            }
            try {
                if (!!this.auth_token) {
                    await fetch(`${baseURL}/${this.username}/${this.trackerID}/update`, updateRequestOptions)
                        .then(async response => {
                            if (!response.ok) {
                                throw Error(response.statusText);
                            }
                            const myResp = await response.json();
                            if (!!myResp) {
                                if (myResp.resp == "ok") {
                                    this.success_msg = myResp.msg;
                                    sessionStorage.removeItem("trackerID");
                                    sessionStorage.removeItem("trackerDescription");
                                    sessionStorage.removeItem("trackerName");
                                    this.$router.push({ path: `/dashboard/${this.username}` })
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
                            console.log("Could not update tracker. Error: ", error);
                        })
                }
                else {
                    this.logout();
                    throw Error("authentication failed.")
                }
            }
            catch (error) {
                this.error_txt = error;
                console.log("Could not update tracker. Error: ", error);
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
  