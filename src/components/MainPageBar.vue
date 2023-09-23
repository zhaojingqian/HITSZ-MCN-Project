<template>
  <el-dropdown @command="handleCommand">
    <el-button type="primary">
      {{ currentJson }}<el-icon class="el-icon--right"><arrow-down /></el-icon>
    </el-button>
    <template #dropdown>
      <el-dropdown-menu>
        <!--循环 dataList -->
        <el-dropdown-item v-for="data in dataList" :key="data" :command="data">{{
          data
        }}</el-dropdown-item>
      </el-dropdown-menu>
    </template>
  </el-dropdown>
  <barUpload />
  <el-button type="primary" @click="switchGraphLayout">SWITCH</el-button>
</template>

<script setup>
import { ref, computed } from 'vue'
import barUpload from './BarUpload.vue'
import { ArrowDown } from '@element-plus/icons-vue'
import axios from 'axios'
import { useDataStore } from '../stores/data.js'
const currentJson = ref('Selecte Data')
const dataStore = useDataStore()
const dataList = computed(() => dataStore.getDataList())

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

const handleCommand = (data_name) => {
  currentJson.value = data_name
  const dataPath = 'database/data/' + data_name + '.json'
  dataStore.setDataPath(dataPath)
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
</script>

<style></style>
