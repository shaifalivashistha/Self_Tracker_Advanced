<template>
  <div class="about">
    <AboutPage></AboutPage>
    <h1>This is all about Tracker application</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import AboutPage from "@/components/AboutPage.vue";

export default {
  name: "AboutView",
  components: {
    AboutPage,
  },
};
</script>
