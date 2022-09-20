<template>
  <div id="tracker">
    <b-navbar toggleable="md" type="dark" variant="info">
      <b-navbar-brand href="/register">Trackers</b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item href="/dashboard/">Dashboard</b-nav-item>
        <b-nav-item href="/logout">Login</b-nav-item>
        <b-nav-item href="/about">About</b-nav-item>
      </b-navbar-nav>
    </b-navbar>

    <body class="container">
      <div>
        <h3 class="form text-center mt-2 mb-4">Create Your Tracker here</h3>
        <div class="form-group">
          <label>Tracker Name</label>
          <input
            id="tracker_name"
            type="text"
            v-model="tracker_name"
            ref="tracker_name"
            class="form-control form-control-lg"
            placeholder="Tracker Name"
            required
            autocomplete="off"
          />
        </div>
        <div class="form-group">
          <label>Tracker Description</label>
          <input
            id="tracker_des"
            type="email"
            v-model="tracker_des"
            ref="tracker_des"
            class="form-control form-control-lg"
            placeholder="Description"
            required
            autocomplete="off"
          />
        </div>
        <div class="form-group">
          <label>Tracker Type</label>
          <div>
            <b-dropdown
              id="tracker_type"
              text="Select Tracker Type"
              class="m-md-2"
            >
              <b-dropdown-item>Numeric Tracker</b-dropdown-item>
              <b-dropdown-item>Boolean Tracker</b-dropdown-item>
              <b-dropdown-item>Multiplechoice Tracker</b-dropdown-item>
            </b-dropdown>
          </div>
        </div>
        <button
          id="submit"
          @click="register"
          type="submit"
          class="btn btn-dark btn-lg btn-block"
        >
          Sign Up
        </button>
      </div>
    </body>
  </div>
</template>

<script>
export default {
  name: "HomePage",
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
