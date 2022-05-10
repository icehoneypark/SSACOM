import { createStore } from 'vuex'
import createPersistedState from "vuex-persistedstate"

export default createStore({
  plugins: [createPersistedState()],

  state: {
    isLogin: false
  },
  getters: {
  },
  mutations: {
    LOGIN: function(state){
      state.isLogin = true
    },
    LOGOUT: function(state){
      state.isLogin = false
    }
  },
  actions: {
    login: function({commit}){
      commit("LOGIN")
    },
    logout: function({commit}){
      commit("LOGOUT")
    }
  },
  modules: {
  }
})
