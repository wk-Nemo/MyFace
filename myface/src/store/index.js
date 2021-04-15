import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userID: '',
    username: '',
    userPci: '',
    isLogin: false
  },
  mutations: {
    changeUserID (state, userID) {
      state.userID = userID
    },
    changeUserName (state, username) {
      state.username = username
    },
    changeLogStatus (state, status) {
      state.isLogin = status
    },
    changeUserPic (state, userPic) {
      state.userPci = userPic
    }
  }
})
