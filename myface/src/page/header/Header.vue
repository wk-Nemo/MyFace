<template>
  <div class="header">
    <div class="header-left">
      <div class="logo">MyFace</div>
      <router-link class="header-right-item" to='/home'>首页</router-link>
      <router-link class="header-right-item" to='/facephoto'>照片录取</router-link>
      <router-link class="header-right-item" to='/facerecognize'>信息</router-link>
    </div>
    <div class="header-right" v-if="!this.$store.state.isLogin">
      <router-link class="header-right-item" to="/login">登录</router-link>
      <div> | </div>
      <router-link class="header-right-item" to="/signup">注册</router-link>
    </div>
    <div class="header-right" v-else>
      <div class="username">
        用户: {{ this.$store.state.username }}
        <div class="userlist">
          <div @click="goToFacePhoto" class="userlist-item">个人中心</div>
          <div @click="logout" class="userlist-item">退出登录</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Header',
  methods: {
    goToFacePhoto: function () {
      this.$router.push('/facephoto')
    },
    logout: function () {
      this.$store.commit('changeUserID', '')
      this.$store.commit('changeUserName', '')
      this.$store.commit('changeLogStatus', false)
      this.$router.push('/home')
    }
  }
}
</script>

<style lang="scss" scoped>
.header{
  height: 1rem;
  width: 100%;
  // background: rgb(51,51,51);
  background: rgb(16,23,29);
  color: white;
  display: flex;
  justify-content: center;
  line-height: 1rem;
  font-size: 0.5rem;
  // padding: 0 50px 0 50px;
  .header-left{
    width: 60%;
    padding: 0 0 0 7rem;
    font-weight: 600;
    display: flex;
    height: 100%;
    .logo {
      margin-right: 50px;
    }
    a{
      font-size: 0.32rem;
      display: inline-block;
      line-height: 1rem;
      color:white;
      margin: 0 10px;
    }
    .router-link-active{
      border-bottom: 1px solid white;
    }
  }
  .header-right{
    font-size: 0.32rem;
    width: 35%;
    font-weight: 600;
    height: 100%;
    display: flex;
    position: relative;
    a{
      display: inline-block;
      line-height: 1rem;
      color:white;
      margin: 0 10px;
    }
    .router-link-active{
      border-bottom: 1px solid white;
    }
    .userlist {
      display: none;
      text-align: center;
      width: 115px;
      position: absolute;
      bottom: 0;
      left: 0;
      transform: translate(-25%, 100%);
      z-index: 10;
      background: white;
      font-weight: 100;
      line-height: 30px;
      padding: 10px 0;
      box-shadow: 0 6px 24px 0 rgb(31,35, 41);
      .userlist-item {
        color: black;
      }
      .userlist-item:hover {
        cursor: pointer;
        background: rgb(245,246,247);
      }
    }
    .username:hover {
      cursor: pointer;
      .userlist {
        display: block;
      }
    }
  }
}
</style>
