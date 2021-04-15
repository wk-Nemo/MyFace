<template>
  <div id="app">
    <div style="height: 100%">
      <Header></Header>
      <router-view/>
    </div>
  </div>
</template>

<script>
import Header from './page/header/Header'

export default {
  name: 'App',
  data () {
    return {
      userID: ''
    }
  },
  components: {
    Header
  }
}
</script>

<style>
#app{
  height: 100%;
}
html {
  /* background-color: #2d2d2d; */
  scroll-behavior: smooth;
}
body{
  height: 100%
}
</style>
