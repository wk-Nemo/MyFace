<template>
  <div class="header">
    <div class="header-left">MyFace</div>
    <div class="header-right">
      <router-link to='/'>首页</router-link>
      <router-link to='/facephoto'>照片录取</router-link>
      <router-link to='/facevideo'>视频录取</router-link>
      <router-link to='/facerecognize'>信息</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style lang="scss" scoped>
.header{
  height: 40px;
  width: 100%;
  background: rgb(51,51,51);
  color: white;
  display: flex;
  justify-content: center;

  line-height: 40px;
  // padding: 0 50px 0 50px;
  .header-left{
    width: 40%;
    padding: 0 0 0 20%;
    font-size: 16px;
    font-weight: 600;
  }
  .header-right{
    width: 35%;
    font-size: 12px;
    font-weight: 600;
    a{
      color:white;
      margin: 0 10px;
    }
  }
}
</style>
