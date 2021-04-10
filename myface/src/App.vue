<template>
  <div id="app">
    <login v-if="status === 0"  @func="toSignup"></login>
    <signup v-else-if="status === 1" @func="toLogin"></signup>
    <div style="height: 100%" v-else>
      <Header></Header>
      <router-view/>
    </div>
  </div>
</template>

<script>
import Header from './page/header/Header'
import Login from '@/page/user/Login'
import Signup from './page/user/signup.vue'
export default {
  name: 'App',
  components: {
    Header,
    Login,
    Signup
  },
  data () {
    return {
      status: 0
    }
  },
  methods: {
    toLogin: function (data) {
      this.status = data
    },
    toSignup: function (data) {
      this.status = data
    }
  }
}
</script>

<style>
#app{
  height: 100%;
}
html {
  background-color: #2d2d2d;
}
body{
  height: 100%
}
</style>
