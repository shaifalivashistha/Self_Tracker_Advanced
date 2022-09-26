<template>
  <div id="dashboard">
    <!-- <div v-if="!trck_result.length">
      <b-navbar fixed="top" toggleable="md" type="dark" variant="info">
        <b-navbar-brand href="/">Home</b-navbar-brand>
        <b-navbar-nav>
          <b-nav-item href="/about">About</b-nav-item>
        </b-navbar-nav>
        <b-nav-item-dropdown right>
          <template #button-content> </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="/login">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar>
      <h1>Welcome to the Self tracker.</h1>
      <h2>Hello.</h2>
      <h4>
        Hi We welcome you to track your routine and manage it. So,
        <strong> Let's Track it!!</strong> with
        <strong> The Self Tracker.</strong>
      </h4>
      <router-link tag="button" :to="`/dashboard/${email}/create_tracker`">Add Tracker</router-link>
    </div> -->

    <div>
      <b-navbar fixed="top" toggleable="md" type="dark" variant="info">
        <b-navbar-brand href="#">Dashboard</b-navbar-brand>
        <b-navbar-nav>
          <b-nav-item href="/about">About</b-nav-item>
          <b-nav-item @click="logout()">Logout</b-nav-item>
        </b-navbar-nav>
      </b-navbar>
      <h1>Welcome to the Self tracker.</h1>
      <h2>Hello.</h2>
      <h4>
        Hi We welcome you to track your routine and manage it. So,
        <strong> Let's Track it!!</strong> with
        <strong> The Self Tracker.</strong>
      </h4>
      <router-link tag="button" :to="`/dashboard/${email}/create_tracker`">Add Tracker</router-link>
      <div>----------x----------</div>
      <table align="center">
        <thead>
          <tr>
            <th>Tracker Name</th>
            <th>Tracker Description</th>
            <th>Tracker Type</th>
            <th>Last Updated at</th>
            <th>Add Logs</th>
            <th>Delete Trackers</th>
            <th>Update Trackers</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="tracker in trck_result">
            <td>{{ tracker.name }}</td>
            <td>{{ tracker.description }}</td>
            <td>
              {{ tracker.type }}
            </td>
            <td>{{ tracker.date_created }}</td>
            <td v-if="tracker.type === 'numeric'">
              <router-link :to="`/user/tracker/numlog`">
                <button type="button" class="btn btn-info btn-lg" @click="addNumTrackerLogs(tracker.id)">
                  Add Logs</button>
              </router-link>
            </td>
            <td v-else="tracker.type === 'boolean'">
              <router-link :to="`/user/tracker/boolean`">
                <button type="button" class="btn btn-info btn-lg" @click="addBoolTrackerLogs(tracker.id)">
                  Add Logs</button>
              </router-link>
            </td>
            <td>
              <button type="button" class="btn btn-danger btn-lg" @click="deleteTracker(tracker.id)">Delete</button>
            </td>
            <td>
              <!-- <button class="btn btn-success" @click="updateTracker(tracker.id)">
                <router-link style="text-decoration: none; color: inherit" :to="`/${email}/update/${tracker.id}`">
                  Update
                </router-link>
              </button> -->

              <router-link :to="`/${email}/update/${tracker.id}`">
                <button class="btn btn-success btn-lg" @click="updateTracker(tracker.id)">
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
      email: "",
      auth_token: "",
      trck_result: {},
      err_case: "",
      pass_case: "",
      username: ""
    };

  },
  async created() {
    this.auth_token = sessionStorage.getItem("authentication-token"),
      this.email = sessionStorage.getItem("email")
    console.log(this.email)
    console.log(this.auth_token)

    const req_opt = {
      methods: "GET",
      headers: {
        "Content-Type": "application/json;charset=utf-8",
        "Authentication-Token": `${this.auth_token}`,
      }
    }
    try {
      const res = await fetch(`${baseURL}/dashboard/${this.email}`, req_opt)
      if (this.auth_token) {

        if (res) {
          // console.log(res)
          if (res.ok) {
            // console.log("res.ok")
            // console.log(res.json())
            // const data = await res
            const data = await res.json().catch(() => {
              throw Error("Something Went Wrong")
            })
            if (data) {
              // console.log("data block")
              // console.log(data)
              this.trck_result = data
              console.log(this.trck_result)
              // console.log(data)
            }
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
      console.log("Error in create", err)
    }

  },

  methods: {
    async deleteTracker(id) {
      console.log(id)
      const del_req_opt = {
        methods: "GET",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
          "Authentication-Token": `${this.auth_token}`,
        }
      }
      try {
        console.log("delete trying before fetch")
        const res = await fetch(`${baseURL}/${this.email}/${id}/delete`, del_req_opt)
        console.log("delete trying after fetch")
        if (this.auth_token) {
          console.log("auth token check")
          if (res) {
            console.log("have response")
            if (res.ok) {
              console.log("Tracker Deleted Successfully")
              this.$router.go("dashboard", this.email)
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
    async updateTracker(id) {
      console.log("its update tracker method", id)
      console.log(id)
      sessionStorage.setItem("id", id)
    },
    async addNumTrackerLogs() {
      console.log("Logs Added to Tracker Successfully")
      return ""
    },
    async addBoolTrackerLogs() {
      console.log("Logs Added to Tracker Successfully")
      return ""
    },
    async logout() {
      sessionStorage.removeItem("authentication-token")
      this.$router.go("login")
    }

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
