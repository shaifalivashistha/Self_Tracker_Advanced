<template>
    <div class="numerical_view">
        <addNumLogPage></addNumLogPage>
    </div>
</template>
  
<script>
// @ is an alias to /src
import addNumLogPage from "@/components/addNumLogPage.vue";

export default {
    name: "addNumLogView",
    components: {
        addNumLogPage,
    },
};
</script>