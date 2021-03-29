<template>
  <div class="facephoto">
    <div id="photo">
      <h3 class="photo-title">请选择你的照片</h3>
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
      <div class="upload">
        局部排序
      </div>
    </div>
  </div>
</template>

<script>
import * as faceapi from 'face-api.js'
import { getModels } from '../../util/getface.js'
import { MyNDB } from '../../util/getNDB.js'
export default {
  name: 'FacePhoto',
  data () {
    return {
      imgUrl: '',
      descriptor: [],
      before_s: ''
    }
  },
  methods: {
    onImgchange: async function (e) {
      const image = await faceapi.bufferToImage(e.target.files[0])
      const img = document.getElementById('Img')
      img.setAttribute('src', image.src)
      const canvas = faceapi.createCanvasFromMedia(img)
      const displaySize = {
        width: img.width,
        height: img.height
      }
      canvas.setAttribute('class', 'mycanvas')
      canvas.style = `position:absolute; left:50%; top:70px; margin-left:${-img.width / 2}px`
      document.getElementById('photo').append(canvas)
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
        console.log(ndb.before_s)
        for (let i = 0; i < 128; i++) {
          console.log(this.descriptor[0][i])
          console.log(ndb.trueGen[i])
        }
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
  background:  rgb(51,51,51);
  height: 93.6%;
  color:white;
  #photo {
    height: 370px;
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
      height: 280px;
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
    .input-upload:hover{
      color: #444;
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
