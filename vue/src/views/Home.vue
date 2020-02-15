<template>
  <div class="home">
    <h1>This is the home page</h1>
    <div v-if="isConnected" class="information">
      <h1>My Facebook Information</h1>
      <button v-on:click="testAPI">Hit me</button>
      <input v-model="todo" placeholder="add todo">
      <button v-on:click="testAPI2">Hit me again</button>
      <p>Message is: {{ todo }}</p>
      <div class="well">
        <div class="list-item">
          <img :src="picture" />
        </div>
        <div class="list-item">
          <i>{{name}}</i>
        </div>
        <div class="list-item">
          <i>{{email}}</i>
        </div>
        <div class="list-item">
          <i>{{personalID}}</i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "home",
  data() {
    return {
      todo: '' 
    }
  },
  computed: {
    ...mapGetters(["isConnected", "name", "email", "picture", "personalID"])
  },
  methods: {
    testAPI() {
      axios.get("/todo/").then(function (response) {
        console.log(response); // eslint-disable-line no-console
      });
    },
    testAPI2() {
      axios.post("/todo/add", {'name': this.todo}).then(function (response) {
        console.log(response); // eslint-disable-line no-console
      });
    }

  }
};
</script>
