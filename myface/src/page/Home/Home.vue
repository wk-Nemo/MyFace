<template>
  <div class="home">
    <Header></Header>
    <Content></Content>
  </div>
</template>

<script>
import Header from './components/Header'
import Content from './components/Content'
export default {
  name: 'Home',
  components: {
    Header,
    Content
  }
}
</script>

<style lang="scss" scoped>
.home{
  color:white;
  position: relative;
  .home-message{
    height: 100%;
    .home-title{
      height: 35%;
      position: relative;
      p {
        width: 100%;
        position: absolute;
        bottom: 0;
        text-align: center;
        font-size: 20px;
        font-weight: 900;
        padding: 25px 0;
      }
    }
    .home-content{
      p{
        width:100%;
        text-align: center;
        margin: 10px 0;
        font-weight: 900;
      }
    }
  }
  .home-btn{
    background:white;
    height: 35px;
    width: 180px;
    position: absolute;
    left: 50%;
    margin-left: -90px;
    margin-top: 20px;
    border-radius: 10px;
    font-weight: 900;
    color:rgb(102,102,102);
    text-align: center;
    line-height: 35px;
  }
  .home-btn:hover{
    color: rgb(200, 22, 35);
    cursor: pointer;
  }
}
</style>
