<template>
  <el-upload
    v-model:file-list="fileList"
    class="bar_upload"
    action="http://127.0.0.1:8280/upload"
    method="post"
    accept=".json"
    :show-file-list="false"
    :before-upload="handleBeforeUpload"
    :on-success="handleSuccess"
    :on-error="handleError"
    :limit="1"
  >
    <el-button type="success">UPLOAD</el-button>
  </el-upload>
</template>

<script setup>
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
import { useDataStore } from '../stores/data.js'
const dataStore = useDataStore()
const fileList = ref([])
const handleBeforeUpload = (file) => {
  // 判断文件是否为json类型
  const isJson = file.type === 'application/json'
  if (!isJson) {
    ElMessage.error('上传文件只能是json格式!')
  }
  return isJson
}

const handleSuccess = (_, file) => {
  const data = file.name.split('.')[0]
  ElMessage.success(`${data} 上传成功!`)
  const currentDataList = dataStore.getDataList()
  if (!currentDataList.includes(data)) {
    dataStore.addDataList(data)
    console.log(dataStore.getDataList())
  }
  fileList.value = []
}

const handleError = (_, file) => {
  const data = file.name.split('.')[0]
  ElMessage.error(`${data} 上传失败!请检查文件内容及格式是否正确!`)
}

</script>

<style></style>
