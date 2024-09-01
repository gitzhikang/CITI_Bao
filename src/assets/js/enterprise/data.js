let pieChart = {
    // backgroundColor: '#2c343c',

    title: {
        text: 'Customized Pie',
        left: 'center',
        top: 20,
        textStyle: {
            color: '#ccc'
        }
    },

    tooltip: {
        trigger: 'item'
    },

    // visualMap: {
    //     show: false,
    //     min: 80,
    //     max: 600,
    //     inRange: {
    //         colorLightness: [0, 1]
    //     }
    // },
    series: [
        {
            name: '',
            type: 'pie',
            radius: '55%',
            center: ['50%', '50%'],
            data: [{value: 335, name: 'E'},
            {value: 301, name: 'S'},
            {value: 274, name: 'G'},].sort(function (a, b) { return a.value - b.value; }),
            roseType: 'radius',
            label: {
                color: 'rgba(0, 0, 0, 0.6)',
                textStyle : {
                    fontWeight : 600 ,
                    fontSize : 20,   //文字的字体大小,
                    color: "#B4CDCD"
                },
            },
            labelLine: {
                lineStyle: {
                    color: 'rgba(0, 0, 0, 0.6)'
                },
                smooth: 0.2,
                length: 10,
                length2: 20
            },
            // itemStyle: {
            //     normal: {
            //         color: function(colors) {
            //             var colorList = [
            //                 '#45C2E0', '#FFC851','#5A5476'
            //             ];
            //         return colorList[colors.dataIndex]
            //         }
            //     },
            //     shadowBlur: 200,
            //     shadowColor: 'rgba(0, 0, 0, 0.5)'
            // },

            animationType: 'scale',
            animationEasing: 'elasticOut',
            animationDelay: function (idx) {
                return Math.random() * 200;
            }
        }
    ]
};

let lineChart = {

    title: {
        text: 'Customized Line',
        left: 'center',
        top: 20,
        textStyle: {
            color: '#ccc'
        }
    },

    // Setup grid
    grid: {
        zlevel: 0,
        x: 50,
        x2: 50,
        y: 30,
        y2: 30,
        borderWidth: 0,
        backgroundColor: 'rgba(0,0,0,0)',
        borderColor: 'rgba(0,0,0,0)',
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'],
        axisLine: {
            lineStyle: {
                color: '#8791af'
            },
        },
    },
    yAxis: {
        type: 'value',
        axisLine: {
            lineStyle: {
                color: '#8791af'
            },
        },
        splitLine: {
            lineStyle: {
                color: "rgba(166, 176, 207, 0.1)"
            }
        }
    },
    
    series: [{
        name: 'E',
        type: 'line',
        stack: 'yes',
        data: [120, 132, 101, 134, 90, 230, 210, 120, 132, 101, 134, 90],
        lineStyle:{ 
            color:'#45C2E0' //改变折线颜色
        } ,
    },
    {
        name: 'S',
        type: 'line',
        stack: 'yes',
        data: [220, 182, 191, 234, 290, 330, 310, 220, 182, 191, 234, 290, 330],
        lineStyle:{ 
            color:'#FFC851' //改变折线颜色
        } ,
    },
    {
        name: 'G',
        type: 'line',
        stack: 'yes',
        data: [150, 232, 201, 154, 190, 330, 410, 220, 182, 191, 234, 290, 330],
        lineStyle:{ 
            color:'#5A5476' //改变折线颜色
        } ,
    },
    ]
};

export {  pieChart, lineChart };
