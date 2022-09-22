<template>
    <div class="create_tracker">
        <TrackerPage></TrackerPage>
    </div>
</template>
  
<script>
// @ is an alias to /src
import TrackerPage from "@/components/TrackerPage.vue";

export default {
    name: "createTrackerView",
    components: {
        TrackerPage,
    },
};
</script>
  