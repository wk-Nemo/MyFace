<template>
  <div class="header">
    <div class="header-left">MyFace</div>
    <div class="header-right">
      <router-link class="header-right-item" to='/home'>首页</router-link>
      <router-link class="header-right-item" to='/facephoto'>照片录取</router-link>
      <router-link class="header-right-item" to='/facevideo'>视频录取</router-link>
      <router-link class="header-right-item" to='/facerecognize'>信息</router-link>
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
    height: 100%;
    a{
      height:34px;
      display: inline-block;
      line-height: 34px;
      color:white;
      margin: 0 10px;
    }
    .router-link-active{
      border-bottom: 1px solid white;
    }
  }
}

@media screen and (max-width: 700px){
  .header{
    display: flex;
    justify-content: left;
    .header-left{
      width: 53%;
      padding:0;
      text-align: center;
    }
    .header-right{
      width:80%;
    }
  }
}
</style>
