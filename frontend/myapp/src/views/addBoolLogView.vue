<template>
    <div class="boolean_view">
        <addBoolLogPage></addBoolLogPage>
    </div>
</template>
  
<script>
// @ is an alias to /src
import addBoolLogPage from "@/components/addBoolLogPage.vue";

export default {
    name: "addBoolLogView",
    components: {
        addBoolLogPage,
    },
};
</script>