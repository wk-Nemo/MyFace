<template>
  <div class="facephoto">
    <div class="banner">
      <div class="banner-text">
        <div class="banner-title">MyFace</div>
        <div class="banner-content">保护你的个人隐私</div>
      </div>
      <a href="#photo" class="arrows">
        <div class="arrows-container"></div>
      </a>
    </div>
    <div class="wraper">
      <div id="photo">
        <h3 class="photo-title">请选择你的照片</h3>
        <div
          class="container"
        >
          <img v-if="hasImg" src="https://cdn.ai.qq.com/ai/page/product/face/img/banner-ico-7706573879.png">
          <img
            id="Img"
          >
        </div>
      </div>
      <div class="inputwrap">
        <div class="upload">
          上传照片
          <input
            type="file"
            id="imageUpload"
            @change="onImgchange"
          >
        </div>
        <!-- 负数据加密 -->
        <div
          class="upload"
          @click="getNDB"
        >
          负数据库
        </div>
        <!-- 局部排序加密 -->
        <div class="upload"
          @click="getOrderingEncrypt"
        >
          局部排序
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as faceapi from 'face-api.js'
import '../../util/jquery'
import axios from 'axios'
import { getModels } from '../../util/getface.js'
import { MyNDB } from '../../util/getNDB.js'
const encrypt = require('ordering-encrypt')

export default {
  name: 'FacePhoto',
  data () {
    return {
      imgUrl: '',
      hasImg: true,
      descriptor: [],
      before_s: '',
      data: {
        userID: '',
        NDB: '',
        flag: [],
        specific: ''
      }
    }
  },
  methods: {
    onImgchange: async function (e) {
      // 获取照片
      const image = await faceapi.bufferToImage(e.target.files[0])
      this.$store.state.userPic = image.src

      // 判断是否上传了照片
      var flag
      if (this.hasImg === true) {
        flag = true
        this.hasImg = false
      } else {
        flag = false
      }

      // 获取img元素
      const img = document.querySelector('#Img')
      img.setAttribute('src', image.src)

      // 创建画布
      const canvas = faceapi.createCanvasFromMedia(img)
      const displaySize = {
        width: img.width,
        height: img.height
      }
      // canvas.setAttribute('class', 'mycanvas')
      canvas.style = `position:absolute; left:50%; top:0; transform: translate(-50%)`
      const photodiv = document.querySelector('#photo .container')
      // console.log(photodiv)
      if (flag === false) {
        document.querySelector('#photo .container').removeChild(document.querySelector('#photo .container').children[1])
      }
      photodiv.append(canvas)
      // 设置面部特征点和画布匹配
      faceapi.matchDimensions(canvas, displaySize)

      // 获取照片上的所有人脸并存入数组
      const detections = await faceapi.detectAllFaces(image).withFaceLandmarks().withFaceDescriptors()

      // 匹配画布尺寸
      const resizedDetections = faceapi.resizeResults(detections, displaySize)
      resizedDetections.forEach(detection => {
        const box = detection.detection.box
        const drawBox = new faceapi.draw.DrawBox(box, {
          label: 'face'
        })
        drawBox.draw(canvas)
        faceapi.draw.drawDetections(canvas, resizedDetections)
        faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
        this.descriptor.push(detection.descriptor)
      })
    },
    getNDB: function () {
      if (this.descriptor[0] === undefined) {
        alert('请先上传照片')
      } else {
        if (this.$store.state.userID === '') {
          alert('请先登录账号')
          return
        }
        this.data.userID = this.$store.state.userID
        let ndb = new MyNDB(this.descriptor[0])
        this.data.NDB = ndb.NDB
        this.data.flag = ndb.flag
        this.data.specific = ndb.specific
        this.postNDB()
      }
    },
    postNDB: function () {
      axios({
        method: 'post',
        url: 'http://myface.kingfish404.cn/getface_native/',
        dataType: 'json',
        data: JSON.stringify(this.data)
      }).then((response) => {
        console.log(response)
        localStorage.setItem('NDB_userID', response.data.userID)
        alert('负数据库注册成功')
        this.$router.push('/facerecognize')
      })
    },
    getOrderingEncrypt: function () {
      if (this.descriptor[0] === undefined) {
        alert('请先上传照片')
      } else {
        let ndb = new MyNDB(this.descriptor[0])
        // let origin_data = this.descriptor[0]
        let data = String(ndb.before_s).split('').map(a => { return Number(a) })
        let p = new Array(data.length).fill(0)
        let final = encrypt.decode(data, p)
        // console.log('encrypt data:', final.join(''), 'keydata:', p.join(''))
        // final为人脸加密后的结果，p为密钥
        let saveData = {
          username: 'hansome-person',
          part: final.join(''),
          p: p.join('')
        }
        axios({
          method: 'post',
          url: 'http://myface.kingfish404.cn/getface_part/',
          dataType: 'json',
          data: {
            'userID': this.$store.state.userID,
            'part': JSON.stringify(saveData),
            'p': p.toString()
          }
        }).then((response) => {
          console.log(response)
          localStorage.setItem('ordering_userID', response.data.userID)
          alert('局部排序注册成功')
          this.$router.push('/facerecognize')
        }).catch((error) => {
          console.log(error)
          alert('上传失败')
        })
      }
    }
  },
  mounted () {
    getModels()
  }
}
</script>

<style lang="scss" scoped>
.facephoto{
  // background:  rgb(51,51,51);
  color:white;
  height: 100%;
  .banner {
    height: 93.6%;
    background:url("../../assets/7.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    position: relative;
    .banner-text {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      .banner-title {
        font-size: 1.8rem;
        letter-spacing: 0;
        font-weight: 700;
        margin-bottom: 10px;
      }
      .banner-content {
        font-size: 0.6rem;
        letter-spacing: 3.81px;
        font-weight: 300;
      }
    }
    .arrows {
      height: 1rem;
      width: 1rem;
      border: 2px solid white;
      border-radius: 50%;
      position: absolute;
      bottom: 50px;
      left: 50%;
      transform: translate(-50%);
      display: flex;
      align-items: center;
      justify-content: center;
      .arrows-container {
        position: absolute;
        bottom: 16px;
        width: 15px;
        height: 15px;
        border-right: 2px solid white;
        border-top: 2px solid white;
        // -webkit-transform: rotate(135deg);
        // transform: rotate(135deg);
        animation: dong 1s infinite;
      }
      @keyframes dong {
        0%{
          transform: rotate(135deg) translate(0px, 0px);
        }
        50% {
          transform: rotate(135deg) translate(3px, -3px);
        }
        100% {
          transform: rotate(135deg) translate(0px, 0px);
        }
      }
    }
  }
  .wraper {
    background: rgb(17, 28, 34);
    height: 100%;
    #photo {
      position: relative;
      text-align: center;
      height: 88%;
      .photo-title{
        padding: 0.7rem 0 0.5rem 0;
        font-size: 0.7rem;
        font-weight: 900;
        line-height: 70px;
      }
      .container {
        width: 80%;
        top: 40%;
        transform: translate(0, -50%);
        height: 400px;
        overflow: auto;
        display: block;
        margin: 0 auto;
        position: relative;
        #Img {
          height: 100%;
        }
      }
    }
    .inputwrap{
      background: rgb(17, 28, 34);
      display: flex;
      justify-content: center;
      align-items: center;
      // height: 120px;
      .upload{
        padding: 4px 10px;
        margin: 10px 45px;
        height: 0.6rem;
        font-size: 0.4rem;
        line-height: 0.6rem;
        position: relative;
        cursor: pointer;
        color: #888;
        background: #fafafa;
        border: 1px solid #ddd;
        border-radius: 4px;
        overflow: hidden;
        display: inline-block;
        *display: inline;
        *zoom: 1;
        width: auto;
        #imageUpload {
          position: absolute;
          font-size: 100px;
          right: 0;
          top: 0;
          opacity: 1;
          filter: alpha(opacity=0);
          cursor: pointer
        }
      }
      .upload:hover{
        color: rgb(200, 22, 35);
        background: #eee;
        border-color: #ccc;
        text-decoration: none;
        cursor: pointer;
      }
    }
  }
}
</style>
