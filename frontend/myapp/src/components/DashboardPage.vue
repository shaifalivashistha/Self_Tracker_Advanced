<template>
  <div v-if="!trackers || !trackers.length">
    <div id="dashboard">
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
      <v-if></v-if>
    </div>
  </div>
</template>
<template >
  <div id="dashboard">
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
    <router-link tag="button" :to="`/dashboard/${email}/create_tracker`"
      >Add Tracker</router-link
    >
    <table align="center" class="table table-bordered">
      <thead class="thead-light">
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
            <!-- <button class="ui button" type="button"><a href="`/${}/{{tracker.id}}/logs`">Add
                  logs</a></button> -->
            <router-link tag="button" :to="`/${email}/${tracker.id}/logs`">
              Add Logs</router-link
            >
          </td>
          <td v-else-if="tracker.type === 'boolean'">
            <!-- <button class="ui button" type="button"><a href="/{{this.email}}/{{tracker.id}}/logs">Add
                  logs</a></button> -->
            <router-link tag="button" :to="`/${email}/${tracker.id}/logs`"
              >Add Logs</router-link
            >
          </td>
          <td v-else="tracker.type === 'multiple choice'">
            <router-link tag="button" :to="`/${email}/${tracker.id}/logs`"
              >Add Logs</router-link
            >
            <!-- <button class="ui button" type="button"><a href="/{{this.email}}/{{tracker.id}}/logs">Add
                  logs</a></button> -->
          </td>
          <td>
            <!-- <button><a class="ui red button" href="/{{this.email}}/{{tracker.id}}/delete">Delete</a></button> -->
            <router-link tag="button" :to="`/${email}/${tracker.id}/delete`"
              >Delete</router-link
            >
          </td>
          <td>
            <!-- <button><a class="ui red button" href="/{{this.email}}/{{tracker.id}}/update">Update</a></button> -->
            <router-link tag="button" :to="`/${email}/${tracker.id}/update`"
              >Update</router-link
            >
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
export default {
  name: "DashboardPage",
  data() {
    return {
      email: "",
      auth_token: "",
      trackers: [],
      error_message: "",
      success_message: "",
    };
  },
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
