<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>jQuery UI Datepicker - Format date</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
  <link rel="stylesheet" href="/resources/demos/style.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  <script>
	$( function() {
		$( "#datepicker_Start" ).datepicker();
		$( "#datepicker_Start" ).datepicker( "option", "dateFormat", "yy-mm-dd" );		
		$( "#datepicker_End" ).datepicker();
		$( "#datepicker_End" ).datepicker( "option", "dateFormat", "yy-mm-dd" );
		
		 var tooltips = $( "[title]" ).tooltip({
			  position: {
				my: "left top",
				at: "right+5 top-5",
				collision: "none"
		  }
    });
		
	 } );
  </script>
  
  <script>
   
  $(document).ready(function(){
  	$("button").click(function(){
		var a = "SQLAPIForIndex.php?";
		a+="StartDate="+document.getElementById('datepicker_Start').value;
		a+="&EndDate="+document.getElementById('datepicker_End').value;
		a+="&StartTime="+document.getElementById('StartTime').value;//+"&EndTime="document.getElementById('EndTime').value;
		a+="&EndTime="+document.getElementById('EndTime').value;
		
		//alert(a);
  		$.ajax({url: a, 
			success: function(result){
				
				if(result=="not Found"){
					alert("not Found");
				}
				else{
					var contact = JSON.parse(result);
					var content = "計算結果";
					content += "開始時間: "+contact.StartTime+"<br>";
					content += "結束時間: "+contact.EndTime+"<br>";
					content += "預估人數: "+contact.PeopleNum+"<br>";
					content += "總臉數: "+contact.SumFace+"<br>";
					content += "總注視時間: "+contact.SumAttention+"<br>";
					content += "平均注視時間: "+contact.AverageAttention+"<br>";
				
					$("#div1").html(content);
					DrawFlot(contact.FPeopleStream);
				}

			},
			error:function(xhr, ajaxOptions, thrownError){ 
					alert(xhr.status); 
					alert(thrownError);  
					$("#div1").html(xhr.status+","+thrownError);
			}
		
		});
		
	});
  });
</script>
</head>
<body>

<div id="div1"><h2>Let jQuery AJAX Change This Text</h2></div>
<button>Get External Content</button>

<p>Start Date: <input type="text" id="datepicker_Start" name="StartDate"  size="30">
<label for="Time">Time</label>
<input id="StartTime" name="StartTime" title="Format: 00:00:00">
</p>

<p>End Date: <input type="text" id="datepicker_End" name="EndDate" size="30">
<label for="lastname">Time</label>
<input id="EndTime" name="EndTime" title="Format: 00:00:00">
</p>




<!--<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>-->

<script src="http://static.pureexample.com/js/flot/excanvas.min.js"></script>
<script src="http://static.pureexample.com/js/flot/jquery.flot.min.js"></script>

<!-- CSS -->
<style type="text/css">

</style>

<!-- Javascript -->
<script type="text/javascript">
function DrawFlot(stream) {
    
        
/*     var data1 = [
        [1, 1], [2, 0], [3, 1],
        [4, 1], [5, 1], [6, 1],
        [7, 1], [8, 1], [9, 1],
        [10, 1], [11, 0], [12, 1],
        [13, 1], [14, 1], [15, 0]
    ] */;
	var data1 = new Array();
	for(i=0;i<stream.length-1;i++){
		data1.push([i,stream[i]]);
	}
	
	//alert(data1);
    var data = [{
        label: "人數",
        data: data1,
        lines: {
            show: true
        },
        points:{
            show:true
        }
    }];

    var options = {
            xaxis: {
                mode: "time"
            },
            grid:{
                backgroundColor: { colors: ["#969696", "#5C5C5C"] }
            }
    };

    var plot = $.plot($("#example-section25 #flotcontainer"), data, options);  
};
</script>

<!-- HTML -->
<div id="example-section25">
    <div id="flotcontainer" style="width: 600px;height:200px;">
    </div>
</div>




 
</body>
</html>