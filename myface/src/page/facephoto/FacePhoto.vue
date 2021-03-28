<template>
  <div class="facephoto">
    <div id="photo">
      <h3>请选择你的照片</h3>
      <img
        id="Img"
        :src=imgUrl
      >
    </div>
    <div class="inputwrap">
        <div class="inputbox">
            <input
              type="file"
              id="imageUpload"
              @change="onImgchange"
            >
            <!-- 负数据加密 -->
            <div class="upload">
                <a href="javascript:;" id="get_ndb">负数据库</a>
            </div>
            <button id="getNDB" style="display: none;"></button>

            <!-- 局部排序加密 -->
            <div class="upload">
                <a href="javascript:;">局部排序</a>
            </div>
            <button id="" style="display: none;"></button>
        </div>
    </div>
  </div>
</template>

<script>
import * as faceapi from 'face-api.js'
import { getModels } from '../../util/getface.js'
export default {
  name: 'FacePhoto',
  data () {
    return {
      imgUrl: '',
      descriptor: []
    }
  },
  methods: {
    onImgchange: async (e) => {
      const image = await faceapi.bufferToImage(e.target.files[0])
      const img = document.getElementById('Img')
      img.setAttribute('src', image.src)
      const canvas = faceapi.createCanvasFromMedia(img)
      const displaySize = {
        width: img.width,
        height: img.height
      }
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
    }
  },
  mounted () {
    // Promise.all([
    //   faceapi.nets.faceRecognitionNet.loadFromUri('../../models'),
    //   faceapi.nets.faceLandmark68Net.loadFromUri('../../models'),
    //   faceapi.nets.ssdMobilenetv1.loadFromUri('../../models')
    // ]).then(async () => {
    //   console.log('success')
    // })
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
    height: 300px;
    #Img {
      height: 100%;
    }
  }
}
</style>
