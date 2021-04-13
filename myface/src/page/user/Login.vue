<template>
  <div class="container">
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
          this.$emit('func', 3)
          console.log(response.data)
        })
      }
    },
    sendLoginMsg: function () {
      this.$emit('func', 1)
    }
  }
}
</script>

<style lang="scss" scoped>
.container{
  height: 100%;
  // background:url("../../assets/1.jpg");
  // background-repeat: no-repeat;
  // background-size: auto 28%;
}

.login-wrapper{
  box-shadow: 0 0 5px 5px rgba(0, 0, 0, 0.4);
  width: 5rem;
  height: 9rem;
  border-radius: 15px;
  padding: 25px 50px;
  position: relative;
  left:50%;
  top:50%;
  transform: translate(-50%,-50%);
}

.login-wrapper .header{
  color: white;
  font-size: 50px;
  font-weight: bold;
  text-align: center;
  line-height: 150px;
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
  color: white;
  text-align: center;
  font-size: larger;
  line-height: 105px;
}
</style>
