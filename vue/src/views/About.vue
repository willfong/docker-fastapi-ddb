<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>


<script>
//import axios from "axios";
//import SomeComponent from "@/components/somecomponent";
//import { mapGetters } from "vuex";

function ymd(date) {
  var y = date.getFullYear();
  var m = date.getMonth() + 1;
  var d = date.getDate();
  var mm = m < 10 ? '0' + m : m;
  var dd = d < 10 ? '0' + d : d;
  return `${y}-${mm}-${dd}`;
}

export default {
  name: "about",
  /*
  components: {
  },
  computed: {
    ...mapGetters([
      "jwt",
    ])
  },
  data() {
    return {
      someText: ""
    };
  },
  methods: {
    someFun() {
      console.log("Have some fun"); // eslint-disable-line no-console
      axios.post('/some/url', {key: value}).then(response => {
        this.$store.dispatch("someAction", response.data);
      });
      axios.get('/some/other/url', {params: {id: 123}}).then(response => {
        this.$store.dispatch("someAction", response.data);
      });
    },
  },
  mounted() {
  },
  */
};
</script>
