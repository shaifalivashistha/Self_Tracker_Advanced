<template>
    <div class="numericalView">
        <NumLogPage></NumLogPage>
    </div>
</template>
  
<script>
// @ is an alias to /src
import NumLogPage from "@/components/NumLogPage.vue";

export default {
    name: "addNumLogView",
    components: {
        NumLogPage,
    },
};
</script>