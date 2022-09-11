<template>
    <div id="dash">
        <h1> Welcome to the Self tracker.</h1>
        <h2> Hello</h2>
        <DashboardPage></DashboardPage>
    </div>
</template>
<script>
import DashboardPage from "@/components/DashboardPage.vue"

export default {
    name: "dashboard",
    components: {
        DashboardPage,
    },
};
</script>
<style>
h1 {
    text-align: center;
}
</style>