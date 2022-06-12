<script lang="ts" setup>
const products = ref([])
</script>
<template>
  <div class="category">
    <h2 class="text-title">
      {{ $route.params.category }}
    </h2>
    <el-row>
      <el-col :span="4">
        <category-filter />
      </el-col>
      <el-col :span="20">
        <el-row>
          <el-col :span="3">
            <category-product />
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>
