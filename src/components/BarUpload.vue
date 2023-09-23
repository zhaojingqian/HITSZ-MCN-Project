<template>
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
</template>
