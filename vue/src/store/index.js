import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isConnected: false,
    name: '',
    email: '',
    personalID: '',
    picture: '',
    access_token: '',
    jwt: '',
    FB: undefined,
    messages: [],
    userCache: {},
    
  },
  mutations: {
    FB_IS_CONNECTED(state, isConnected) {
      state.isConnected = isConnected;
    },
    FB_SDK(state, FB) {
      state.FB = FB;
    },
    FB_USER(state, user) {
      state.name = user.name;
      state.email = user.email;
      state.personalID = user.id;
      state.picture = user.picture.data.url;
    },
    FB_ACCESS_TOKEN(state, token) {
      state.access_token = token;
    },
    JWT_SET(state, jwt) {
      state.jwt = jwt;
    },
    MESSAGES_UPDATE(state, messages) {
      state.messages = messages;
    },
    USER_CACHE_UPDATE(state, users) {
      state.userCache = users;
    },
  },
  actions: {
    testAccountLogin({dispatch}, username) {
      axios.post('/login/test-account', {
        value: username
      })
      .then(function (response) {
        console.log("Test Account JWT: " + response.data.token); // eslint-disable-line no-console
        axios.defaults.headers.common['Authorization'] = response.data.token;
        dispatch('jwtSet', response.data.token);
        // TODO: Save token locally so user won't have to log back in on refresh
      })
    },

    fbGetUserData({ commit, getters, dispatch }) {
      if (getters.FB) {
        getters.FB.api('/me', 'GET', { fields: 'id,name,email,picture' },
          user => commit('FB_USER', user)
        )
        getters.FB.getLoginStatus(function(response) {
          if (response.status === 'connected') {
            commit('FB_ACCESS_TOKEN', response.authResponse.accessToken);
            axios.post('/login/facebook', {
              value: response.authResponse.accessToken
            })
            .then(function (response) {
              axios.defaults.headers.common['Authorization'] = response.data.token;
              dispatch('jwtSet', response.data.token);
              // TODO: Save token locally so user won't have to log back in on refresh
            })
          }
        });
      }
    },
    fbSdkLoaded({ commit, dispatch }, payload) {
      commit('FB_IS_CONNECTED', payload.isConnected);
      commit('FB_SDK', payload.FB)
      if (payload.isConnected) dispatch('fbGetUserData');
    },
    fbOnLogin({ commit, dispatch }) {
      commit('FB_IS_CONNECTED', true);
      dispatch('fbGetUserData');
    },
    fbOnLogout({ commit }) {
      commit('FB_IS_CONNECTED', false);
    },
    jwtSet({commit}, jwt) {
      axios.defaults.headers.common['Authorization'] = jwt;
      commit('JWT_SET', jwt);
    },
    messageGet({getters, dispatch, commit}) {
      axios.get("/messages/").then(function(response) {
        let x;
        for (x of response.data){
          if (!getters.userCache[x.user_id]) {
            // TODO: This is async, so repeated messages will be fetched multiple times
            dispatch('userCacheLookup', x.user_id);
          }
        }
        commit('MESSAGES_UPDATE', response.data);
      });
    },
    messageAdd({dispatch}, text) {
      axios.post('/messages/add', {text}).then(function() {
        dispatch('messageGet');
      });
    },
    userCacheLookup({dispatch}, userId) {
      axios.get("/login/lookup", {params: {id: userId} }).then(function(response) {
        let user = {}
        user[userId] = response.data
        dispatch('userCacheAdd', user);
      });
    },
    userCacheAdd({commit, getters}, user) {
      commit('USER_CACHE_UPDATE', {...getters.userCache, ...user});
    },
  },
  getters: {
    isConnected: state => state.isConnected,
    name: state => state.name,
    email: state => state.email,
    personalID: state => state.personalID,
    picture: state => state.picture,
    access_token: state => state.access_token,
    jwt: state => state.jwt,
    FB: state => state.FB,
    messages: state => state.messages,
    userCache: state => state.userCache,
  }
})
