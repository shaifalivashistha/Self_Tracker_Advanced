<template>
  <div id="tracker">
    <b-navbar toggleable="md" type="dark" variant="info">
      <b-navbar-brand :to="`/dashboard/${username}`">Add Trackers</b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item :to="`/dashboard/${username}`">Dashboard</b-nav-item>
        <b-nav-item @click=" logout()">Logout
        </b-nav-item>
      </b-navbar-nav>
    </b-navbar>

    <body class="container">
      <form @submit.prevent="addTrackerSubmit">
        <h3 class="form text-center mt-2 mb-4">Create Your Tracker here</h3>
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
        <div class="form-group">
          <div>
            <h5>Select Tracker Type:</h5>
            <b-form-group>
              <b-form-radio-group id="radio-group-2" v-model="tracker_type
              " name="radio-options">
                <h6>
                  <b-form-radio value="numeric">Numeric Tracker</b-form-radio>
                </h6>
                <h6>
                  <b-form-radio value="boolean">Boolean Tracker</b-form-radio>
                </h6>
              </b-form-radio-group>
            </b-form-group>
          </div>

        </div>
        <button type="submit" class="btn btn-dark btn-lg btn-block">
          Add Tracker
        </button>
      </form>
    </body>
  </div>
</template>

<script>
const baseURL = "http://127.0.0.1:5000"
export default {
  name: "createTrackerPage",
  data() {
    return {
      username: "",
      auth_token: "",
      tracker_name: "",
      tracker_des: "",
      tracker_type: "",
      error_txt: "",
      success_msg: "",
    }
  },
  async created() {
    this.auth_token = sessionStorage.getItem("authentication-token");
    this.username = sessionStorage.getItem("username");
  },
  methods: {
    async addTrackerSubmit() {
      const tracker_data = {
        tracker_name: this.tracker_name,
        tracker_des: this.tracker_des,
        tracker_type: this.tracker_type
      }
      const addTrackerRequestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
          "Authentication-Token": `${this.auth_token}`,
        },
        body: JSON.stringify(tracker_data)
      }
      try {
        if (!!this.auth_token) {
          await fetch(`${baseURL}/dashboard/${this.username}/create_tracker`, addTrackerRequestOptions)
            .then(async response => {
              if (!response.ok) {
                throw Error(response.statusText);
              }
              const myResp = await response.json();
              if (!!myResp) {
                if (myResp.resp == "ok") {
                  this.success_msg = myResp.msg;
                  this.$router.push({ path: `/dashboard/${this.username}` });
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
              console.log("Could not create tracker. Error: ", error);
            })
        }
        else {
          throw Error("authentication failed");
        }
      }
      catch (error) {
        this.error_txt = error;
        console.log("Tracker Request failed", err)
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
