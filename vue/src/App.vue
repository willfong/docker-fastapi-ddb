<template>
  <div id="app">
    <h1 class="title">Hello World!</h1>
    <div id="nav">
      <router-link to="/">Home</router-link>|
      <router-link to="/about">About</router-link>
      <!--
      <facebook-login
        class="button"
        appId="1841024232697094"
        @login="onLogin"
        @logout="onLogout"
        @get-initial-status="getUserData"
        @sdk-loaded="sdkLoaded"
      />
      -->
      <v-facebook-login app-id="1841024232697094" v-on:login="fbLogin"></v-facebook-login>
      <button class="button" v-on:click="testAccountLogin">Test Account Login</button>
    </div>
    <router-view />
  </div>
</template>

<script>
//import facebookLogin from "facebook-login-vuejs";
import axios from "axios";
import "regenerator-runtime";
import VFacebookLogin from "vue-facebook-login-component";
import { mapGetters } from "vuex";

export default {
  name: "appMain",
  components: {
    //facebookLogin,
    VFacebookLogin,
  },
  computed: {
    ...mapGetters(["isConnected", "name", "email", "picture", "personalID"])
  },
  methods: {
    fbLogin(r) {
      console.log(r); // eslint-disable-line no-console
    },
    testAccountLogin() {
      var username = prompt("Please enter in a user name:");
      console.log("Logging in with test account: " + username); // eslint-disable-line no-console
      axios.post('/login/test-account', {
        value: username
      })
      .then(response => {
        console.log("Test Account JWT: " + response.data.token); // eslint-disable-line no-console
        this.$store.dispatch("jwtSet", response.data.token);
        // TODO: Save token locally so user won't have to log back in on refresh
      });
    },
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
