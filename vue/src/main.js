import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bulma/css/bulma.css'
import GSignInButton from 'vue-google-signin-button'

Vue.config.productionTip = false
Vue.config.devtools = true
Vue.use(GSignInButton)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
