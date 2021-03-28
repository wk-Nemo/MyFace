import * as faceapi from 'face-api.js'

function start () {
  console.log('success')
}

export function getModels () {
  return Promise.all([
    // 加载模型
    faceapi.nets.faceRecognitionNet.loadFromUri('/static/models'),
    faceapi.nets.faceLandmark68Net.loadFromUri('/static/models'),
    faceapi.nets.ssdMobilenetv1.loadFromUri('/static/models')
  ]).then(start).catch((error) => {
    console.log('getface>getModels:', error)
  })
}
