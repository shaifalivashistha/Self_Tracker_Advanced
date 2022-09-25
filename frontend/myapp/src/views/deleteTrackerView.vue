<template>
    <div class="delete_Tracker">
        <DeleteTracker></DeleteTracker>
    </div>
</template>
  
<script>
// @ is an alias to /src
import DeleteTracker from "@/components/DeleteTracker.vue";

export default {
    name: "deleteTrackerView",
    components: {
        DeleteTracker,
    },
};
</script>