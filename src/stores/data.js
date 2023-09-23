import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useDataStore = defineStore('data', () => {
  // ---------------------------
  const dataPath = ref('')
  const setDataPath = (path) => {
    dataPath.value = path
  }
  const getDataPath = () => {
    return dataPath.value
  }
  // ---------------------------

  // ---------------------------
  const dataJson = ref({})
  const setDataJson = (data) => {
    dataJson.value = data
  }
  const getDataJson = () => {
    return dataJson.value
  }
  // ---------------------------

  // ---------------------------
  const optionParams = ref({
    layout: 'force',
    curveness: 0
  })
  const setOptionParams = (params) => {
    optionParams.value = params
  }
  const getOptionParams = () => {
    return optionParams.value
  }
  // ---------------------------

  // ---------------------------
  const dataList = ref([])
  const resetDataList = (list) => {
    dataList.value = list
  }
  const addDataList = (data) => {
    dataList.value.push(data)
  }
  const delDataList = (dataName) => {
    // dataList.value.splice(index, 1)
    dataList.value.forEach((item, i) => {
      if (item === dataName) {
        dataList.value.splice(i, 1)
        return true
      }
    })
    return false
  }
  const getDataList = () => {
    return dataList.value
  }
  // ---------------------------

  return {
    dataPath,
    dataJson,
    optionParams,
    dataList,

    setDataPath,
    getDataPath,

    setDataJson,
    getDataJson,

    setOptionParams,
    getOptionParams,

    resetDataList,
    addDataList,
    delDataList,
    getDataList
  }
})
