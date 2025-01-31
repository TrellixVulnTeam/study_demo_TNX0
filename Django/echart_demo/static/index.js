
$(function(){
	var myChart = echarts.init(document.getElementById('map'));
	var myjson = {
	"type": "FeatureCollection",
	"features": [{
		"type": "Feature",
		"properties": {
			"name": "广安门外"
		},
		"geometry": {
			"type": "MultiPolygon",
			"coordinates": [
				[
					[
						[116.3223620605466, 39.893801838256],
						[116.34075164794922, 39.8936701335924],
						[116.34143829345703, 39.875317920188344],
						[116.317324492188, 39.8769472480469],
						[116.317324492188, 39.8819472480469],
						[116.319324492188, 39.8819472480469],
						[116.320324492188, 39.8869472480469],
						[116.321824492188, 39.8869472480469]
					]
				]
			]
		}
	}, {
		"type": "Feature",
		"properties": {
			"name": "广安门内"
		},
		"geometry": {
			"type": "MultiPolygon",
			"coordinates": [
				[
					[
						[116.34109497070311, 39.87983973554458],
						[116.36993408203125, 39.87970800405549],
						[116.3697624206543, 39.8951188709751],
						[116.35293960571288, 39.894723763816785],
						[116.34984970092775, 39.89380183825623],
						[116.34830474853514, 39.89643587838578],
						[116.3419532775879, 39.896699276830915],
						[116.34178161621092, 39.89393354266699],
						[116.34075164794922, 39.8936701335924]
					]
				]
			]
		}
	}, {
		"type": "Feature",
		"properties": {
			"name": "陶然亭"
		},
		"geometry": {
			"type": "MultiPolygon",
			"coordinates": [
				[
					[
						[116.36993408203125, 39.88721629504685],
						[116.37937545776366, 39.88734801211131],
						[116.3792037963867, 39.88036665897025],
						[116.38195037841795, 39.880630119164756],
						[116.38195037841795, 39.878522409266346],
						[116.38383865356444, 39.878390675246706],
						[116.38401031494139, 39.868755941712825],
						[116.34143829345703, 39.869417920188344],
						[116.34109497070311, 39.87983973554458],
						[116.36993408203125, 39.87970800405549]
					]
				]
			]
		}
	}, {
		"type": "Feature",
		"properties": {
			"name": "大栅栏"
		},
		"geometry": {
			"type": "MultiPolygon",
			"coordinates": [
				[
					[
						[116.3697624206543, 39.8951188709751],
						[116.39104843139647, 39.895250572855026],
						[116.394345, 39.868843],

						[116.38401031494139, 39.868755941712825],
						[116.38383865356444, 39.878390675246706],
						[116.38195037841795, 39.878522409266346],
						[116.38195037841795, 39.880630119164756],
						[116.3792037963867, 39.88036665897025],
						[116.37937545776366, 39.88734801211131],


						[116.36993408203125, 39.88721629504685]
					]
				]
			]
		}
	}, {
		"type": "Feature",
		"properties": {
			"name": "月坛"
		},
		"geometry": {
			"type": "MultiPolygon",
			"coordinates": [
				[
					[
						[116.32736206054686, 39.91737289576941],
						[116.35036468505858, 39.91763621372854],
						[116.35053634643556, 39.899728286187894],
						[116.35276794433594, 39.89485546645597],

						[116.34984970092775, 39.89380183825623],
						[116.34830474853514, 39.89643587838578],
						[116.3419532775879, 39.896699276830915],
						[116.34178161621092, 39.89393354266699],
						[116.34075164794922, 39.8936701335924],

						[116.32736206054686, 39.89380183825623]
					]
				]
			]
		}
	}, {
		"type": "Feature",
		"properties": {
			"name": "金融街"
		},
		"geometry": {
			"type": "MultiPolygon",
			"coordinates": [
				[
					[
						[
							116.35036468505858,
							39.91363621372854
						],
						[
							116.35036468505858,
							39.92085170443116
						],
						[
							116.36632919311523,
							39.92098334531233
						],
						[
							116.36615753173827,
							39.8951188709751
						],
						[116.35276794433594, 39.89485546645597],
						[116.35053634643556, 39.899728286187894]

					]
				]
			]
		}
	}, {
		"type": "Feature",
		"properties": {
			"name": "西长安街"
		},
		"geometry": {
			"type": "MultiPolygon",
			"coordinates": [
				[
					[
						[
							116.36632919311523,
							39.92066429748714
						],
						[
							116.38778686523436,
							39.92079595026529
						],
						[116.39104843139647, 39.895250572855026],
						[
							116.36615753173827,
							39.8951188709751
						]
					]
				]
			]
		}
	}, {
		"type": "Feature",
		"properties": {
			"name": "展览路"
		},
		"geometry": {
			"type": "MultiPolygon",
			"coordinates": [
				[
					[
						[
							116.34419302368164,
							39.94423128816934
						],
						[
							116.34419302368164,
							39.94883128816934
						],
						[
							116.35019302368164,
							39.94883128816934
						],
						[
							116.35036468505858,
							39.91763621372854
						],
						[116.32736206054686, 39.91737289576941],
						[116.327345, 39.933843],
						[116.327345, 39.936843],
						[116.321345, 39.941843],
						[116.321345, 39.944543]
					]
				]
			]
		}
	}, {
		"type": "Feature",
		"properties": {
			"name": "新街口"
		},
		"geometry": {
			"type": "MultiPolygon",
			"coordinates": [
				[
					[
						[
							116.36735916137694,
							39.94383128816934
						],
						[
							116.36632919311523,
							39.92098334531233
						],
						[
							116.35036468505858,
							39.92085170443116
						],
						[
							116.35019302368164,
							39.94383128816934
						]
					]
				]
			]
		}
	}, {
		"type": "Feature",
		"properties": {
			"name": "什刹海"
		},
		"geometry": {
			"type": "MultiPolygon",
			"coordinates": [
				[
					[
						[
							116.36735916137694,
							39.9436996796908
						],
						[
							116.38486862182617,
							39.94383128816934
						],

						[
							116.38486862182617,
							39.93663128816934
						],
						[
							116.38886862182617,
							39.93463128816934
						],

						[
							116.38926686523436,
							39.92079595026529
						],
						[
							116.36632919311523,
							39.92066429748714
						]
					]
				]
			]
		}
	}, {
		"type": "Feature",
		"properties": {
			"name": "德胜门"
		},
		"geometry": {
			"type": "MultiPolygon",
			"coordinates": [
				[
					[
						[
							116.3671875,
							39.94383128816934
						],
						[
							116.36529922485352,
							39.957911932580835
						],
						[
							116.3730239868164,
							39.95804351371704
						],
						[
							116.3730239868164,
							39.96172768273857
						],
						[
							116.38349533081055,
							39.96212240336062
						],
						[
							116.37971878051758,
							39.9500166010947
						],
						[
							116.38435363769531,
							39.9500166010947
						],
						[
							116.38492529907225,
							39.94383128816934
						]
					]
				]
			]
		}
	}]
}
		echarts.registerMap('xicheng',myjson,{});
		var option = {
		    tooltip: {
		        trigger: 'item',
            	formatter: '{b}<br/>{c} (p / km2)'
		    },
		    visualMap: {
	            min: 500,
	            max: 50000,
	            text:['High','Low'],
	            left: 'right',
	            realtime: false,
	            calculable: true,
	            inRange: {
	                color: ['#313695','#4575b4', '#74add1','#abd9e9','#e0f3f8']
	            }
	        },
		    series: [
		        {
		        	name: '西城',
		            type: 'map',
		            mapType: 'xicheng',
		            aspectScale: 0.85,  //地图长度比
		            label: {
		                normal: {
		                    show: true,
		                    textStyle: {
		                        color: '#fff'
		                    }
		                },
		                emphasis: {
		                    show: true,
		                    textStyle: {
		                        color: '#333'
		                    }
		                }
		            },
		            data: [
		            	{name: '德胜门', value: 17000},
	                    {name: '什刹海', value: 1000},
	                    {name: '新街口', value: 5000},
	                    {name: '展览路', value: 20000},
	                    {name: '月坛', value: 25000},
	                    {name: '金融街', value: 30000},
	                    {name: '西长安街', value: 18000},
	                    {name: '广安门外', value: 2300},
	                    {name: '广安门内', value: 20000},
	                    {name: '大栅栏', value: 16000},
	                    {name: '陶然亭', value: 28000}
		            ]
		        }
		    ]
		};
		myChart.setOption(option);
	});
