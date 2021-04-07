<template>
  <div class='facerecognize'>
    <h2>信息</h2>
    <p>用户ID：{{ userId }}</p>
    <!-- <h2>用户头像</h2> -->
    <h2>识别对比（密文）</h2>
    <hr />
    <div class='upload-area'>
      <p class='info'>
        请限制照片大小在6M之内<span>{{ num }}/1</span>
      </p>
      <div class='img-area'>
        <img src='' alt='' />
        <input type='file' class='img-input' @change='loadImg' /><br />
      </div>
    </div>
    <hr />
    <button @click='uploadImg'>上传</button>
    <h2>原始脸型数据:</h2>
    <p class='data-desc'>{{ originData }}</p>
    <button @click='getOriginData'>点击获取</button>
    <h2>加密脸型数据:</h2>
    <p class='data-desc'>{{ encryptData }}</p>
    <button @click='getEncryptData'>点击获取</button>
  </div>
</template>

<script>
export default {
  name: 'FaceRecognize',
  data () {
    return {
      num: 0,
      userId: '66ccff',
      originData: '',
      encryptData: ''
    }
  },
  methods: {
    loadImg: function () {
      let that = this
      var preview = document.querySelector('img')
      var file = document.querySelector('input[type=file]').files[0]
      var reader = new FileReader()

      reader.addEventListener(
        'load',
        function () {
          preview.src = reader.result
          preview.style.visibility = 'visible'
          that.num = 1
        },
        false
      )

      if (file) {
        reader.readAsDataURL(file)
      }
    },
    uploadImg: function () {
      var file = document.querySelector('input[type=file]').files[0]

      console.log('uploadImg', file)
      if (file) {
      } else {
        alert('请先选择图片!')
      }
    },
    getOriginData: function () {
      var file = document.querySelector('input[type=file]').files[0]

      if (file) {
        this.originData = '66ccff'
      } else {
        this.originData = '请先选择图片!'
      }
    },
    getEncryptData: function () {
      var file = document.querySelector('input[type=file]').files[0]

      if (file) {
        this.encryptData = '66ccff'
      } else {
        this.encryptData = '请先选择图片!'
      }
    }
  }
}
</script>

<style lang='scss' scoped>
.facerecognize {
  background: rgb(51, 51, 51);
  height: 100%;
  color: white;
  max-width: 800px;
  margin: 0 auto;
}
h2 {
  font-size: x-large;
  padding: 0.5rem;
}
p {
  margin: 0.5rem;
}
button {
  text-align: center;
  padding: 0.5em 1em;
  margin: auto;
  display: block;
  background-color: rgb(51, 51, 51);
  border: 2px solid white;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

.info {
  text-align: center;
}

.info span {
  float: right;
}

.upload-area {
  margin: 0.5rem;
}

.img-input {
  width: 100%;
  height: 100%;
  opacity: 0;
  cursor: pointer;
}

.img-area {
  width: 100px;
  height: 100px;
  border: 5px solid white;
  margin: auto;
  cursor: pointer;
  position: relative;
}

.img-area img {
  width: 100%;
  height: 100%;
  top: 0;
  position: absolute;
  visibility: hidden;
}

.data-desc {
  text-align: center;
  margin: auto;
  min-height: 50px;
}
</style>
