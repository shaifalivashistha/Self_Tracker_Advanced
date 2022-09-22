<template>
  <div id="dashboard">
    <div v-if="!trackers || !trackers.length">
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
    </div>
    <div v-else>
      <b-navbar fixed="top" toggleable="md" type="dark" variant="info">
        <b-navbar-brand href="/">Home</b-navbar-brand>
        <b-navbar-nav>
          <b-nav-item href="/about">About</b-nav-item>
        </b-navbar-nav>
        <b-nav-item-dropdown right>
          <template #button-content>
            {{ this.username }}
          </template>
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
      <router-link :to="`/dashboard/${email}/create_tracker`">Add Tracker</router-link>
      <table align="center">
        <thead>
          <tr>
            <th>Tracker Name</th>
            <th>Tracker Type</th>
            <th>Last Updated at</th>
            <th>Add Logs</th>
            <th>Delete Trackers</th>
            <th>Update Trackers</th>
          </tr>
        </thead>
        <tbody></tbody>
        <tbody>
          <tr v-for="tracker in trackers" :key="tracker.id">
            <td>{{ tracker.name }}</td>
            <td>
              {{ tracker.type }}
            </td>
            <td>{{ tracker.date_created.date() }}</td>
            <td v-if="tracker.type === 'numeric'">

              <router-link tag="button" :to="`/${email}/${tracker.id}/logs`">
                Add Logs</router-link>
            </td>
            <td v-else-if="tracker.type === 'boolean'">

              <router-link tag="button" :to="`/${email}/${tracker.id}/logs`">Add Logs</router-link>
            </td>
            <td v-else="tracker.type === 'multiple choice'">
              <router-link tag="button" :to="`/${email}/${tracker.id}/logs`">Add Logs</router-link>

            </td>
            <td>

              <router-link tag="button" :to="`/${email}/${tracker.id}/delete`">Delete</router-link>
            </td>
            <td>
              <router-link tag="button" :to="`/${email}/${tracker.id}/update`">Update</router-link>
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
      trackers: [],
      err_case: "",
      pass_case: "",
    };

  },
  async created() {
    this.auth_token = sessionStorage.getItem("authentication-token"),
      this.email = sessionStorage.getItem("email")
    console.log(this.email)
    console.log(this.auth_token)
    try {

      const res = await fetch(`${baseURL}/dashboard/${this.email}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
          "Authentication-Token": `${this.auth_token}`,
        },
      })
      if (res) {
        console.log(res)
        if (res.ok) {
          console.log("res.ok")
          // console.log(res.json())
          // const data = await res
          const data = await res.json().catch(() => {
            throw Error("Something Went Wrong")
          })
          if (data) {
            console.log(data)
            this.trackers = data
            // console.log(this.trackers)
          }
        }
      }
      else {
        throw Error(res.statusText)
      }
    }
    catch (err) {
      console.log("Error", err)
    }

  },

  methods: {

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
</style>
