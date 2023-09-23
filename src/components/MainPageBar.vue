<template>
  <barSelect />
  <barUpload />
  <el-button type="primary" @click="switchGraphLayout">SWITCH</el-button>
  <el-button type="danger" @click="deleteDataJsonFromList">DELETE</el-button>
</template>

<script setup>

import barUpload from './BarUpload.vue'
import barSelect from './BarSelect.vue'

import { useDataStore } from '../stores/data.js'
import { ElMessageBox } from 'element-plus'
const dataStore = useDataStore()

const switchGraphLayout = () => {
  const oldOptionParam = dataStore.getOptionParams()
  if (oldOptionParam.layout === 'force') {
    dataStore.setOptionParams({ layout: 'circular', curveness: 0.3 })
  } else {
    dataStore.setOptionParams({ layout: 'force', curveness: 0 })
  }
}

const deleteDataJsonFromList = () => {
  const currentDataPath = dataStore.getDataPath()
  const currentDataName = currentDataPath.split('/')[2].split('.')[0]
  ElMessageBox.confirm('Are you sure to delete this data?', 'Warning', {
    confirmButtonText: 'OK',
    cancelButtonText: 'Cancel',
    type: 'warning'
  })
    .then(() => {
      dataStore.delDataList(currentDataName)
      dataStore.setDataPath('')
      dataStore.setDataJson({})
    })
    .catch(() => {})
  console.log(dataStore.getDataList())
}
</script>

<style></style>
