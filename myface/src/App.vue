<template>
  <div id="app">
    <Header></Header>
    <router-view/>
  </div>
</template>

<script>
import Header from './page/header/Header'
export default {
  name: 'App',
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
  background-color: #2d2d2d;
}
body{
  height: 100%
}
</style>
