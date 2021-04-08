<template>
  <div class="facephoto">
    <div id="photo">
      <h3 class="photo-title">请选择你的照片</h3>
      <div
        class="container"
        v-if="hasImg"
      >
          <div class="eyebox">
            <div class="eye EL">
              <div
                class="pupil"
              ></div>
            </div>
            <div class="eye ER">
              <div
                class="pupil"
              ></div>
            </div>
          </div>
          <div class="smile">
            <div class="teeth"></div>
            <div class="tongue"></div>
          </div>
      </div>
      <img
        id="Img"
        :src=imgUrl
      >
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
        username: 'wk',
        NDB: ''
      }
    }
  },
  methods: {
    onImgchange: async function (e) {
      const image = await faceapi.bufferToImage(e.target.files[0])
      const img = document.getElementById('Img')
      img.setAttribute('src', image.src)
      var flag
      if (this.hasImg === true) {
        flag = true
        this.hasImg = false
      } else {
        flag = false
      }
      const canvas = faceapi.createCanvasFromMedia(img)
      const displaySize = {
        width: img.width,
        height: img.height
      }
      canvas.setAttribute('class', 'mycanvas')
      canvas.style = `position:absolute; left:50%; top:70px; margin-left:${-img.width / 2}px`
      const photodiv = document.getElementById('photo')
      if (flag === false) {
        document.getElementById('photo').removeChild(document.getElementById('photo').children[2])
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
        let ndb = new MyNDB(this.descriptor[0])
        // console.log(ndb.before_s)
        // for (let i = 0; i < 128; i++) {
        //   console.log(this.descriptor[0][i])
        //   console.log(ndb.trueGen[i])
        // }
        // JSON.stringify(ndb.NDB)
        this.data.NDB = ndb.NDB
        console.log(ndb.NDB)
        console.log(JSON.stringify(this.data))
        this.postNDB()
      }
    },
    postNDB: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/getface_native/',
        dataType: 'json',
        data: JSON.stringify(this.data)
      }).then((response) => {
        console.log(response)
      })
    },
    getOrderingEncrypt: function () {
      if (this.descriptor[0] === undefined) {
        alert('请先上传照片')
      } else {
        let ndb = new MyNDB(this.descriptor[0])
        // console.log(ndb.before_s);
        let data = String(ndb.before_s).split('').map(a => { return Number(a) })
        let p = new Array(data.length).fill(0)
        let final = encrypt.decode(data, p)
        // console.log('encrypt data:', final.join(''), 'keydata:', p.join(''))
        // final为人脸加密后的结果，p为密钥
        let saveData = {
          username: '12312313',
          part: final.join(''),
          p: p.join('')
        }
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/getface_part/',
          dataType: 'json',
          data: JSON.stringify(saveData)
        }).then((response) => {
          console.log(response)
        }).catch((error) => {
          console.log(error)
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
.container {
  width: 80%;
  height: 350px;
  background-color:rgb(51,51,51);
  overflow: auto;
  display: block;
  margin: 0 auto;
  .eyebox {
    width: 400px;
    display: block;
    margin: 0 auto;
    text-align: center;
    margin-top: 50px;
    margin-bottom: 25px;
    .eye {
      height: 100px;
      width: 100px;
      background-color: rgb(51,51,51);
      border: 4px solid white;
      border-radius: 100%;
      display: inline-block;
      margin: 0 20px;
      position: relative;
      padding: 20px;
      overflow: hidden;
      .pupil {
        height: 25px;
        width: 25px;
        border-radius: 100%;
        display: inline-block;
        background-color: white;
        position: absolute;
        margin-left: -10px;
        left: 50%;
        margin: 10px;
      }
    }
  }
}
.smile {
  height: 100px;
  width: 200px;
  border-radius: 0 0 200px 200px;
  background: #770f1a;
  margin: 0 auto;
  overflow: hidden;
  transition: all .4s;
  transform-origin: center;
  .teeth {
    background-color: #fff;
    transition: all .4s;
    height: 33.33333px;
    width: 33.33333px;
    margin-left: 56.66667px;
    position: relative;
  }
  .teeth:after {
    content: "";
    background-color: #fff;
    height: 33.33333px;
    width: 33.33333px;
    position: absolute;
    left: 50px;
    top: 0;
    z-index: 10000;
  }
  .tongue {
    transition: all .4s;
    height: 100px;
    width: 100px;
    background-color: pink;
    border-radius: 100%;
    margin-top: 40px;
    margin-left: 15px;
    display: inline-block;
    position: relative;
  }
  .tongue:after {
    content: '';
    height: 100px;
    width: 100px;
    background-color: pink;
    border-radius: 100%;
    display: inline-block;
    position: absolute;
    left: 50px;
    /*margin-top: 0;
      margin-left: -($tongueDimensions/3);*/
  }
}
.smile:hover {
  transition: all .4s;
  height: 33.33333px;
  width: 33.33333px;
  border-radius: 100%;
  margin-top: 50px;
}
.smile:hover .teeth {
  margin-left: -25px;
  margin-top: -40px;
  transition: all .4s;
}
.smile:hover .tongue {
  transition: all .4s;
  margin-left: -50px;
  /*margin-top: $tongueDimensions*2;*/
}

.facephoto{
  background:  rgb(51,51,51);
  color:white;
  max-width: 55%;
  margin: 35px auto;
  border-radius: 10px;
  padding: 10px 0 20px 0;
  #photo {
    position: relative;
    text-align: center;
    .photo-title{
      padding: 20px 0 10px 0;
      font-size: 20px;
      font-weight: 900;
      line-height: 20px;
    }
    #Img {
      margin: 20px 0;
      height: 350px;
    };
  }
  .inputwrap{
    display: flex;
    justify-content: center;
    align-items: center;
    .upload{
      padding: 4px 10px;
      margin: 10px 45px;
      height: 20px;
      line-height: 20px;
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

@media screen and (max-width: 700px){
  .upload{
    margin: 10px 20px;
  }
}
</style>
