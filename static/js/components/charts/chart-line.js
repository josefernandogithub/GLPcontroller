//
// Charts
//

'use strict';

//
// Sales chart
//

var LineChart = (function() {

	// Variables

	var $chart = $('#chart-line');


	// Methods

	function init($this) {
		var salesChart = new Chart($this, {
			type: 'line',
			options: {
				scales: {
					yAxes: [{
						gridLines: {
							color: Charts.colors.gray[200],
							zeroLineColor: Charts.colors.gray[200]
						},
						ticks: {

						}
					}]
				}
			},
			data: {
				labels: ['Jan','Fev','Mar','Abr','Mai', 'Jun', ],
				datasets: [{
					label: 'valor',
					data: [0, 20, 10, 30, 15, 40, 40, 40, 40, 20, 60, 60]
				}]
			}
		});

		// Save to jQuery object

		$this.data('chart', salesChart);

	}


	// Events

	if ($chart.length) {
		init($chart);
	}

});
