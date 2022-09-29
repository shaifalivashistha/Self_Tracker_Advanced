<template>
    <div class="create_tracker">
        <createTrackerPage></createTrackerPage>
    </div>
</template>
  
<script>
// @ is an alias to /src
import createTrackerPage from "@/components/createTrackerPage.vue";

export default {
    name: "createTrackerView",
    components: {
        createTrackerPage,
    },
};
</script>
  