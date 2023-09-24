<template>
  <v-chart
    class="degree_chart"
    :option="updateOption(degreeData)"
    autoresize
  />
</template>

<script setup>
import {computed} from 'vue'
import { use } from 'echarts/core'
import { BarChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent, GridComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'
import VChart from 'vue-echarts'
import { useDataStore } from '../stores/data.js'
use([TitleComponent, TooltipComponent, GridComponent, BarChart, CanvasRenderer])

const dataStore = useDataStore()
const degreeData = computed(() => dataStore.getDegreeData())

const updateOption = (degreeData) => {
  console.log(degreeData)
  return {
    title: {
      text: 'Degree Distribution',
      left: 'center',
      top: '5px'
    },
    tooltip: {
      trigger: 'item',
      formatter: '{b} : {c}'
    },
    xAxis: {
      type: 'category',
      name: 'Degree',
      nameLocation: 'middle',
      nameGap: 30,
      data: degreeData.degree
    },
    yAxis: {
      type: 'value',
      name: 'Number of Nodes',
      nameLocation: 'middle',
      nameGap: 40
    },
    series: [
      {
        name: 'Degree',
        type: 'bar',
        data: degreeData.count
      }
    ]
  }
}
</script>
