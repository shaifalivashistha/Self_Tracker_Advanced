<template>
  <div id="dashboard">
    <div>
      <b-navbar fixed="top" toggleable="md" type="dark" variant="info">
        <b-navbar-brand :to="`/dashboard/${username}`">{{ username }}</b-navbar-brand>
        <b-navbar-nav>
          <b-nav-item @click="logout()">Logout</b-nav-item>
        </b-navbar-nav>
      </b-navbar>
      <h1>Welcome to the Self tracker.</h1>
      <!-- <h2>Hello!!</h2> -->
      <h4>
        Hi {{username}}, welcome to your tracker dashboard.
        <strong> Let's Track it</strong> with
        <strong> Self Tracker!!</strong>
      </h4>
      <div class="container">
        <p id="error_txt" class="alert alert-danger" role="alert" v-if="error_txt">
          {{ error_txt }}
        </p>
        <p id="success_msg" class="alert alert-success" role="alert" v-if="success_msg">
          {{ success_msg }}
        </p>
      </div>
      <div>
        <router-link tag="button" :to="`/dashboard/${username}/create_tracker`">Add Tracker</router-link>
      </div>
      <br />
      <div>
        <button @click="ExportTrackers()">Export Trackers</button>
      </div>
      <div>----------Tracker Details----------</div>
      <table align="center">
        <thead>
          <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Type</th>
            <th>Last Updated</th>
            <th>Add Logs</th>
            <th>Delete</th>
            <th>Update</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="tracker in tracker_data">
            <td>{{ tracker.name }}</td>
            <td>{{ tracker.description }}</td>
            <td>
              {{ tracker.type }}
            </td>
            <td>{{ tracker.date_created }}</td>
            <td v-if="tracker.type == 'numeric'">
              <router-link :to="`/${username}/${tracker.id}/numeric`">
                <button type="button" class="btn btn-info btn-lg" @click="addNumTrackerLogs(tracker.id)">
                  Add Logs</button>
              </router-link>
            </td>
            <td v-else-if="tracker.type == 'boolean'">
              <router-link :to="`/${username}/${tracker.id}/boolean`">
                <button type="button" class="btn btn-info btn-lg" @click="addBoolTrackerLogs(tracker.id)">
                  Add Logs</button>
              </router-link>
            </td>
            <td>
              <button type="button" class="btn btn-danger btn-lg" @click="deleteTracker(tracker.id)">Delete</button>
            </td>
            <td>
              <router-link :to="`/${username}/${tracker.id}/update`">
                <button class="btn btn-success btn-lg"
                  @click="updateTracker(tracker.id, tracker.name, tracker.description)">
                  Update
                </button>

              </router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
const baseURL = "http://127.0.0.1:5000"
export default {
  name: "DashboardPage",
  data() {
    return {
      username: "",
      auth_token: "",
      tracker_data: {},
      error_txt: "",
      success_msg: "",
    };
  },
  async created() {
    this.auth_token = sessionStorage.getItem("authentication-token");
    this.username = sessionStorage.getItem("username");

    const requsetOptions = {
      methods: "GET",
      headers: {
        "Content-Type": "application/json;charset=utf-8",
        "Authentication-Token": `${this.auth_token}`,
      }
    };
    try {
      if (!!this.auth_token) {
        fetch(`${baseURL}/dashboard/${this.username}`, requsetOptions)
          .then(async response => {
            if (!response.ok) {
              throw Error(response.statusText);
            }
            const myResp = await response.json();
            if (!!myResp) {
              this.success_msg = myResp.msg;
              this.tracker_data = myResp.stuff;
            }
            else {
              throw Error("something went wrong (data not received)");
            }

          })
          .catch(error => {
            this.error_txt = error;
            console.log("Could not create dashboard. Error: ", error);
          });
      }
      else {
        this.logout();
        throw Error("authentication failed");
      }
    }
    catch (error) {
      this.error_txt = error;
      console.log("Error: ", error);
    }
  },

  methods: {
    async deleteTracker(trackerID) {
      const deleteRequestOptions = {
        methods: "GET",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
          "Authentication-Token": `${this.auth_token}`,
        }
      };
      try {
        if (!!this.auth_token) {
          await fetch(`${baseURL}/${this.username}/${trackerID}/delete`, deleteRequestOptions)
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
              console.log("Could not delete tracker. Error: ", error);
            });
          this.$router.go();
        }
        else {
          this.logout();
          throw Error("authentication failed.")
        }
      }
      catch (error) {
        this.error_txt = error;
        console.log("Error: ", error);
      }
    },
    async updateTracker(trackerID, trackerName, trackerDescription) {
      sessionStorage.setItem("trackerID", trackerID);
      sessionStorage.setItem("trackerName", trackerName);
      sessionStorage.setItem("trackerDescription", trackerDescription);
    },
    async addNumTrackerLogs(trackerID) {
      sessionStorage.setItem("trackerID", trackerID);
    },
    async addBoolTrackerLogs(trackerID) {
      sessionStorage.setItem("trackerID", trackerID);
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
    async ExportTrackers() {
      const temp_data = this.tracker_data
      const exportTrackersRequestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
          "Authentication-Token": `${this.auth_token}`,
        },
        body: JSON.stringify(temp_data)
      }
      try {
        if (!!this.auth_token) {
          await fetch(`${baseURL}/${this.username}/export_trackers`, exportTrackersRequestOptions)
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
