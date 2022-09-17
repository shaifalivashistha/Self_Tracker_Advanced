<template>
    <div id="dashboard">
        <b-navbar fixed="top" toggleable="md" type="dark" variant="info">
            <b-navbar-brand href="/">Home</b-navbar-brand>
            <b-navbar-nav>
                <b-nav-item href="/about">About</b-nav-item>
            </b-navbar-nav>
            <b-nav-item-dropdown right>
                <template #button-content>
                    User
                </template>
                <b-dropdown-item href="/dashboard">Dashboard</b-dropdown-item>
                <b-dropdown-item href="/login">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown>
        </b-navbar>
        <h1> Welcome to the Self tracker.</h1>
        <h2>Hello.</h2>
        <h4> Hi We welcome you to track your routine and manage it. So, <strong> Let's Track
                it!!</strong> with <strong> The Self Tracker.</strong> </h4>
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
  