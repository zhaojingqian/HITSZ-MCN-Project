import { ref, computed } from 'vue'
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
  const currentData = computed(() => {
    if (!dataPath.value) {
      console.log('dataPath is empty')
      return ''
    }
    return dataPath.value.split('/')[2].split('.')[0]
  })
  const getCurrentData = () => {
    return currentData.value
  }

  // ---------------------------
  const dataJson = ref({})
  const setDataJson = (data) => {
    dataJson.value = data
  }
  const getDataJson = () => {
    return dataJson.value
  }

  // ---------------------------
  const optionParams = ref({
    layout: 'force',
    symbolSize: 10,
    curveness: 0
  })
  const setOptionParams = (params) => {
    optionParams.value = params
  }
  const getOptionParams = () => {
    return optionParams.value
  }

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
        currentData.value = ''
        return true
      }
    })
    return false
  }
  const getDataList = () => {
    return dataList.value
  }

  // ---------------------------
  const featureData = ref({
    degree: {},
    coreness: {},
    triangle: {}
  })
  const setFeatureData = (data) => {
    featureData.value = data
  }
  const getFeatureData = () => {
    return featureData.value
  }

  //
  // const degreeData = computed(() => { return getFeatureData().degree })
  // const corenessData = computed(() => { return getFeatureData().coreness })
  // const triangleData = computed(() => { return getFeatureData().triangle })
  const getDegreeData = () => { 
    return getFeatureData().degree 
  }
  const getCorenessData = () => { 
    return getFeatureData().coreness 
  }
  const getTriangleData = () => { 
    return getFeatureData().triangle 
  }
  const getShortestPathData = () => {
    return getFeatureData().shortest_path
  }

  return {
    dataPath,
    currentData,
    dataJson,
    optionParams,
    dataList,
    featureData,

    setDataPath,
    getDataPath,

    setDataJson,
    getDataJson,

    setOptionParams,
    getOptionParams,

    resetDataList,
    addDataList,
    delDataList,
    getDataList,

    getCurrentData,

    setFeatureData,

    getDegreeData,
    getCorenessData,
    getTriangleData,
    getShortestPathData
  }
})
