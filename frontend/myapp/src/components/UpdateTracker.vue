<template>
    <div id="update_tracker">
        <b-navbar toggleable="md" type="dark" variant="info">
            <b-navbar-brand href="#">Add Trackers</b-navbar-brand>
            <b-navbar-nav>
                <b-nav-item href="/dashboard/">Dashboard</b-nav-item>
                <b-nav-item @click="logout">Logout</b-nav-item>
            </b-navbar-nav>
        </b-navbar>

        <body class="container">
            <form @submit.prevent="UpdateTrackerSubmit">
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
    name: "UpdateTracker",
    data() {
        return {
            email: "",
            auth_token: "",
            tracker_details: {},
            tracker_name: "",
            tracker_des: "",
            tracker_type: ""

        }
    },
    async created() {
        this.auth_token = sessionStorage.getItem("authentication-token"),
            this.email = sessionStorage.getItem("email")
        const get_req = {
            methods: "GET",
            headers: {
                "Content-Type": "application/json;charset=utf-8",
                "Authentication-Token": `${this.auth_token}`
            }
        }
        try {
            const get_response = await fetch(`${baseURL}/dashboard/${this.email}`, get_req)

            if (this.auth_token) {
                if (get_response) {
                    if (get_response.ok) {
                        const getResData = await get_response.json().catch(() => {
                            throw Error("Something Went Wrong")
                        })
                        if (getResData) {
                            console.log(getResData)
                            this.tracker_details = getResData
                            tracker_name = this.tracker_details.name,
                                tracker_des = this.tracker_details.description,
                                tracker_type = this.tracker_details.tracker_type
                        }
                    }
                }
            }
        }
        catch (err) {
            console.log("Get response Error : ", err)
        }
        // console.log(this.email)
        // console.log(this.auth_token)
    },
    methods: {
        async UpdateTrackerSubmit() {
            const tracker_data = {
                tracker_name: tracker.tracker_name,
                tracker_des: this.tracker_des,
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
                const res = await fetch(`${baseURL}/${this.email}/update/${this.tracker_details.id}`, requestOptions)

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
                console.log("Tracker Update failed", err)
            }
        },
        async logout() {

            console.log(this.auth_token)
            console.log("in logout")
            sessionStorage.removeItem("authentication-token")
            this.$router.replace("login")

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
  