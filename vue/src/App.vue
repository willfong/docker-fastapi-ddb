<template>
  <div id="app">
    <h1 class="title">Hello World!</h1>
    <div id="nav">
      <router-link to="/">Home</router-link>|
      <router-link to="/about">About</router-link>
      <facebook-login
        class="button"
        appId="1841024232697094"
        @login="onLogin"
        @logout="onLogout"
        @get-initial-status="getUserData"
        @sdk-loaded="sdkLoaded"
      />
    </div>
    <router-view />
  </div>
</template>

<script>
import facebookLogin from "facebook-login-vuejs";
import { mapGetters } from "vuex";

export default {
  name: "appMain",
  components: {
    facebookLogin
  },
  computed: {
    ...mapGetters(["isConnected", "name", "email", "picture", "personalID"])
  },
  methods: {
    getUserData() {
      this.$store.dispatch("fbGetUserData");
    },
    sdkLoaded(payload) {
      this.$store.dispatch("fbSdkLoaded", payload);
    },
    onLogin() {
      this.$store.dispatch("fbOnLogin");
    },
    onLogout() {
      this.$store.dispatch("fbOnLogout");
    }
  }
};
</script>
