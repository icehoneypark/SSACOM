import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    posts: []
  },
  getters: {
  },
  mutations: {
    CREATE_NOTICE: function (state, res) {
      state.posts.push(res)
    },
  },
  actions: {
    createNotice: function ({commit}, res) {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/notices/',
        data: res,
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
      commit('CREATE_NOTICE', res)
    },
  },
  modules: {
  }
})
