<template>
  <div id="app">
    <h1>Welcome to POC-vue-facebook</h1>
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

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
