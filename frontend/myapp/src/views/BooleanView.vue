<template>
    <div class="booleanView">
        <BooleanLog></BooleanLog>
    </div>
</template>
  
<script>
// @ is an alias to /src
import BooleanLog from "@/components/BooleanLog.vue";

export default {
    name: "BooleanView",
    components: {
        BooleanLog,
    },
};
</script>