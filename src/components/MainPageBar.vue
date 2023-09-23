<template>
  <el-button type="primary" @click="handleClick1">DATA 1</el-button>
  <el-button @click="handleClick2">DATA 2</el-button>
  <el-upload
    v-model:file-list="fileList"
    class="upload-demo"
    :action="storeData"
    multiple
    :on-preview="handlePreview"
    :on-remove="handleRemove"
    :before-remove="beforeRemove"
    :limit="1"
    :on-exceed="handleExceed"
  >
    <el-button type="primary">Click to upload</el-button>
  </el-upload>
  <el-button type="primary" @click="switchGraphLayout">SWITCH</el-button>
</template>

<script setup>
// import { ref } from 'vue'

import axios from 'axios'
import { useDataStore } from '../stores/data.js'

const dataStore = useDataStore()

const passDataJson = async (data_path) => {
  await axios
    .get(data_path)
    .then((res) => {
      dataStore.setDataJson(res.data)
    })
    .catch((err) => {
      console.log(err)
    })
}

const handleClick1 = () => {
  dataStore.setDataPath('./data/test_data.json')
  passDataJson(dataStore.getDataPath())
}

const handleClick2 = () => {
  dataStore.setDataPath('./data/cora_data.json')
  passDataJson(dataStore.getDataPath())
}

const switchGraphLayout = () => {
  const oldOptionParam = dataStore.getOptionParams()
  if (oldOptionParam.layout === 'force') {
    dataStore.setOptionParams({ layout: 'circular', curveness: 0.3 })
  } else {
    dataStore.setOptionParams({ layout: 'force', curveness: 0 })
  }
}

const storeData = (file) => {
  console.log(file)
}
</script>

<style></style>
