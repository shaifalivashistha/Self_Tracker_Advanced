<template>
    <div class="add_logs">
        <AddLogs></AddLogs>
    </div>
</template>
  
<script>
// @ is an alias to /src
import AddLogs from "@/components/LogPage.vue";

export default {
    name: "addLogView",
    components: {
        AddLogs,
    },
};
</script>