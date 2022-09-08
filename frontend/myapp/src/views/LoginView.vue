<template>
    <div>
        <LoginVue></LoginVue>
    </div>
</template>
  
  <script>
  // @ is an alias to /src
  import LoginVue from "@/components/LoginVue.vue";
  
  export default {
      name: "LoginView",
      components: {
          LoginVue,
      },
  };
  </script>
  