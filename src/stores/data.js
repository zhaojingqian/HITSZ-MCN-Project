import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useDataStore = defineStore('data', () => {
  const dataPath = ref('')
  const setDataPath = (path) => {
    dataPath.value = path
  }
  const getDataPath = () => {
    return dataPath.value
  }

  const dataJson = ref({})
  const setDataJson = (data) => {
    dataJson.value = data
  }
  const getDataJson = () => {
    return dataJson.value
  }

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

  return {
    dataPath,
    dataJson,
    optionParams,

    setDataPath,
    getDataPath,
    setDataJson,
    getDataJson,
    setOptionParams,
    getOptionParams
  }
})
