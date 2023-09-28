<template>
  <el-dropdown @command="handleCommand">
    <el-button>
      {{ currentJson }}<el-icon class="el-icon--right"><arrow-down /></el-icon>
    </el-button>
    <template #dropdown>
      <el-dropdown-menu>
        <el-dropdown-item v-for="data in dataList" :key="data" :command="data">{{
          data
        }}</el-dropdown-item>
      </el-dropdown-menu>
    </template>
  </el-dropdown>
</template>

<script setup>
import { ref, computed } from 'vue'
import { ArrowDown } from '@element-plus/icons-vue'
import { useDataStore } from '../stores/data.js'
import axios from 'axios'
const dataStore = useDataStore()
const currentJson = ref('Selecte Data')
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

const getChartInfo = async () => {
  await axios
    .get('http://10.249.46.195:8280/algorithm', {
      params: {
        data_name: dataStore.getCurrentData()
      }
    })
    .then((res) => {
      console.log(res.data)
      dataStore.setFeatureData(res.data)
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

  getChartInfo()
}
</script>

<style></style>
