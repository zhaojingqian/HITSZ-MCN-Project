<template>
  <v-chart class="shortest_path_chart" :option="updateOption(shortestPathData)" autoresize />
</template>
  
<script setup>
import { computed } from 'vue'
import { use } from 'echarts/core'
import { BarChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent, GridComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'
import VChart from 'vue-echarts'
import { useDataStore } from '../stores/data.js'
use([TitleComponent, TooltipComponent, GridComponent, BarChart, CanvasRenderer])

const dataStore = useDataStore()
const shortestPathData = computed(() => dataStore.getShortestPathData())

const isEmpty = (obj) => {
  if (!obj) return true
  for (let key of Object.keys(obj)) {
    if (obj[key].length !== 0) return false
  }
  return true
}

const updateOption = (shortestPathData) => {
  return {
    title: {
      text: 'Shortest Path Distribution',
      left: 'center',
      top: '5px'
    },
    tooltip: {
      trigger: 'item',
      formatter: '{b} : {c}'
    },
    xAxis: {
      type: 'category',
      name: 'Shortest Path',
      nameLocation: 'middle',
      nameGap: 30,
      data: shortestPathData.shortest_path
    },
    yAxis: {
      type: 'value',
      name: 'Number of Nodes (thousands)',
      nameLocation: 'middle',
      nameGap: 40
    },
    series: [
      {
        name: 'Shortest Path',
        type: 'bar',
        data: (function () {
          let data = []
          if (isEmpty(shortestPathData)) return data
          for (let i = 0; i < shortestPathData.count.length; i++) {
            data.push(shortestPathData.count[i] / 1000)
          }
          console.log(data)
          return data
        })()
      }
    ]
  }
}
</script>
  