import * as faceapi from 'face-api.js'

function start () {
  console.log('success')
}

export function getModels () {
  return Promise.all([
    // 加载模型
    faceapi.nets.faceRecognitionNet.loadFromUri('/models'),
    faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
    faceapi.nets.ssdMobilenetv1.loadFromUri('/models')
  ]).then(start)
}
