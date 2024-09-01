<template>
  <div id="enterprise">
    <header>
      <nav-bar></nav-bar>
    </header>
    <!-- 内容 -->
    <el-row class="mains">
      <el-col :span="5">
        <div style="opacity: 0;">1</div>
      </el-col>
      <el-col :span="12">
        <div style="width: 100%;">
          <el-input placeholder="请输入关键字" prefix-icon="el-icon-search" v-model="input1">
          </el-input>
        </div>
        <!-- 列表 -->
        <div class="zhongbu" style="padding-top: 20px;">
          <div class="flex align_center align_center" style="padding: 20px 0;">
            <span style="margin-right: 10px;font-weight: bold;color: #333;font-size: 20px;">请输入权重值</span>
          </div>
          <div class="flex">
            <el-input style="margin-right: 15px;" placeholder="请输入" type="number" v-model="e1">
              <template slot="prepend">E</template>
            </el-input>
            <el-input style="margin-right: 15px;" placeholder="请输入" type="number" v-model="s1">
              <template slot="prepend">S</template>
            </el-input>
            <el-input style="margin-right: 15px;" placeholder="请输入" type="number" v-model="g1">
              <template slot="prepend">G</template>
            </el-input>
            <el-button type="success" plain>确定</el-button>
          </div>
          <div>
            <el-table :data="tableData" style="width: 100%" :default-sort="{prop: 'date', order: 'descending'}">
              <el-table-column prop="xuhao" label="序号" sortable width="180">
              </el-table-column>
              <el-table-column prop="title" label="名称">
              </el-table-column>
              <el-table-column prop="type" label="所属行业">
              </el-table-column>
              <el-table-column prop="level" label="ESG评级">
              </el-table-column>
            </el-table>
          </div>
        </div>
      </el-col>
    </el-row>
    <Footer></Footer>
  </div>
</template>

<script>
  import NavBar from "../components/NavBar.vue"
  import Footer from "../components/Footer.vue"

  export default {
    data() {
      return {
        input1: '',
        e1: '',
        s1: '',
        g1: '',
        radio: 'x',
        banner: [{
            img: require('../assets/images/img/news-1.jpg')
          },
          {
            img: require('../assets/images/img/news-2.jpg')
          },
          {
            img: require('../assets/images/img/news-3.jpg')
          }
        ],
        tableData: [{
          xuhao: '1',
          title: '移城房产',
          type: '房地产',
          level: 'AAA'
        }, {
          xuhao: '2',
          title: '移城房产',
          type: '房地产',
          level: 'AAA'
        }, {
          xuhao: '3',
          title: '移城房产',
          type: '房地产',
          level: 'AAA'
        }, {
          xuhao: '4',
          title: '移城房产',
          type: '房地产',
          level: 'BB '
        }],
        pingjiList: [{
            value: 'all',
            label: '全部'
          }, {
            value: 'AAA',
            label: 'AAA'
          }, {
            value: 'AA',
            label: 'AA'
          }, {
            value: 'A',
            label: 'A'
          }, {
            value: 'BBB',
            label: 'BBB'
          },
          {
            value: 'BB',
            label: 'BB'
          },
          {
            value: 'B',
            label: 'B'
          },
          {
            value: 'C',
            label: 'C'
          }
        ],
        hangyeList: [{
          value: '选项1',
          label: '工业'
        }, {
          value: '选项2',
          label: '材料'
        }, {
          value: '选项3',
          label: '医疗保健'
        }, {
          value: '选项4',
          label: '金融'
        }, {
          value: '选项5',
          label: '房地产'
        }],
        pingji: 'all',
        hangye: '',
        value1: [new Date(2000, 10, 10, 10, 10), new Date(2000, 10, 11, 10, 10)],
      };
    },
    components: {
      NavBar,Footer
    },
    mounted() {

    },
    methods: {
      formatter(row, column) {
        return row.address;
      }
    }
  };
</script>

<style scoped>
  .mains {
    padding: 40px;
    min-height: 500px;
  }

  .zhongbu {
    /* padding-left: 40px; */
  }
</style>
