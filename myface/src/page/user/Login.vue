<template>
  <div class="container">
    <div class="left">
      <div class="left-title">用科技</div>
      <div class="left-content">让复杂的世界更简单</div>
    </div>
    <div class="right">
      <div class="login-wrapper">
          <div class="header">Login</div>
          <div class="form-wrapper">
              <input
                type="text"
                placeholder="userID"
                class="input-item"
                v-model="userID"
              >
              <input
                type="password"
                placeholder="password"
                class="input-item"
                v-model="password"
              >
              <div class="btn">
                <button
                  id="in"
                  class="buttons color-control"
                  @click="login"
                >Login</button>
              </div>
          </div>
          <div class="msg">Don't have account? <a href="#" @click="sendLoginMsg">Sign up</a></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'login',
  data () {
    return {
      userID: '',
      password: ''
    }
  },
  methods: {
    login: function () {
      if (this.userID !== '' && this.password !== '') {
        let data = {
          userID: this.userID,
          password: this.password
        }
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/login/',
          dataType: 'json',
          data: JSON.stringify(data)
        }).then((response) => {
          this.$store.commit('changeUserID', this.userID)
          this.$store.commit('changeUserName', response.data.username)
          this.$store.commit('changeLogStatus', true)
          this.$router.push('home')
        })
      }
    },
    sendLoginMsg: function () {
      this.$router.push('signup')
    }
  }
}
</script>

<style lang="scss" scoped>
.container{
  height: 93.6%;
  background:url("../../assets/3.jpg");
  background-repeat: no-repeat;
  background-size: 100% auto;
  position: relative;
  .left {
    position: absolute;
    color: white;
    top: 40%;
    left: 30%;
    transform: translate(-50%);
    .left-title {
      font-size: 54px;
      letter-spacing: 0;
      font-weight: 700;
      margin-bottom: 10px;
    }
    .left-content {
      font-size: 32px;
      letter-spacing: 3.81px;
      font-weight: 300
    }
  }
  .login-wrapper {
    width: 5rem;
    height: 9rem;
    border-radius: 15px;
    padding: 25px 50px;
    position: absolute;
    top: 50%;
    left: 80%;
    transform: translate(-50%, -50%);
    background: rgba(255,255,255,.9);
    color: black;
    .header{
      font-size: 50px;
      font-weight: bold;
      text-align: center;
      line-height: 150px;
    }
  }
}

.login-wrapper .form-wrapper .input-item{
  display: block;
  width:100%;
  margin-bottom: 40px;
  border:0;
  padding:10px;
  border-bottom: 2px solid rgb(122, 121, 121);
  border-radius: 10px;
  font-size: 15px;
}

.login-wrapper .form-wrapper .input-item::placeholder{
  text-transform: uppercase;
}

.login-wrapper .form-wrapper .btn{
  text-align: center;
  line-height: 50px;
}

.login-wrapper .form-wrapper .btn .buttons{
  background-color:white;
  font-size: large;
  border:0;
  border-radius: 5px;
  cursor: pointer;
  box-shadow:blanchedalmond;
  width: 80%;
  height:100%;
}

#in:hover{
  background-image:linear-gradient(to right,#585f5f,#151418);
}

.login-wrapper .msg{
  text-align: center;
  font-size: larger;
  line-height: 105px;
}
</style>
