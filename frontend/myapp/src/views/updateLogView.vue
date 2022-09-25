<template>
    <div class="update_log">
        <UpdateTracker></UpdateTracker>
    </div>
</template>
  
<script>
import UpdateLog from "@/components/updateLog.vue";

export default {
    name: "updateLogView",
    components: {
        UpdateLog
    },
};
</script>