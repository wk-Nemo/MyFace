<template>
  <div class="container">
    <div class="left">
      <div class="left-title">用科技</div>
      <div class="left-content">让复杂的世界更简单</div>
    </div>
    <div class="right">
      <div class="login-wrapper">
          <div class="header">SignUp</div>
          <div class="form-wrapper">
              <input
                type="text"
                placeholder="username"
                class="input-item"
                v-model="username"
              >
              <input
                type="password"
                placeholder="password"
                class="input-item"
                v-model="password"
              >
              <input
                type="password"
                placeholder="configpassword"
                class="input-item"
                v-model="configpassword"
              >
              <div class="btn">
                <button
                  id="in"
                  class="buttons color-control"
                  @click="Signup"
                >SignUp</button>
              </div>
          </div>
          <div class="msg">Already has account? <a href='#' @click="sendSingnupMsg">Login</a></div>
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
      username: '',
      password: '',
      configpassword: ''
    }
  },
  methods: {
    Signup: function () {
      if (this.username !== '' && this.password !== '') {
        if (this.password !== this.configpassword) {
          alert('两次密码不一致')
        }
        let data = {
          username: this.username,
          password: this.password
        }
        axios({
          method: 'post',
          url: 'http://myface.kingfish404.cn/sign_in/',
          dataType: 'json',
          data: JSON.stringify(data)
        }).then((response) => {
          this.$router.push('login')
          alert('注册成功，你的ID是: ' + response.data.userID)
        })
      } else {
        alert('用户名或密码不能为空')
      }
    },
    sendSingnupMsg: function () {
      this.$router.push('login')
    }
  }
}
</script>

<style lang="scss" scoped>
.container{
  height: 93.6%;
  background:url("../../assets/3.jpg");
  background-repeat: no-repeat;
  background-size: cover;
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
      line-height: 100px;
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
