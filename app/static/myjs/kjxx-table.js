$(function(){
    $('#uppage').bind({
        "mouseover":function(){
            var nowpage = $('#nowpage').val();
            if (nowpage > 1){
                $('#uppage').attr("href", "/get_kjxx?nowpage="+nowpage+"&action=uppage");
            }
        },
    });
    $('#nextpage').bind({
        "mouseover":function(){
            var nowpage = $('#nowpage').val();
            $('#nextpage').attr("href", "/get_kjxx?nowpage="+nowpage+"&action=nextpage")
            }
        },
    );
    $('#gopage').bind({
        "mouseover":function(){
            var nowpage = $('#nowpage').val()-1;
            var totalpage = $('#totalpage').html();
            $('#gopage').attr("href", "/get_kjxx?nowpage="+nowpage+"&action=nextpage");
        },
    });
    $('#searchkjrq').bind({
        "mouseover":function(){
            var inputkjrq = $('#inputkjrq').val();
            $('#searchkjrq').attr("href", "/so_kjxx?inputkjrq="+inputkjrq)
        },
    });

    $('#morePic').bind({
        "click":function(){
//            load loading movies
            $('#loadPicture')[0].style.display='block';
//            loading a html file
            $('#contentarea').load('/plot_bar', function(){
                $('#loadPicture')[0].style.display='none';
            })
        },
    });

    $('#morePic2').bind({
        "click":function(){
//            load loading movies
            $('#loadPicture')[0].style.display='block';
//            loading a html file
            $('#contentarea').load('/plot_weather', function(){
                $('#loadPicture')[0].style.display='none';
            })
        },
    });

    $('#blue_Pic_bar').bind({
        "click":function(){
//            load loading movies
            $('#loadPicture')[0].style.display='block';
//            loading a html file
            $('#contentarea').load('/blue_pic_bar', function(){
                $('#loadPicture')[0].style.display='none';
            })
        },
    });

    $('#blue_pic_scatter').bind({
        "click":function(){
//            load loading movies
            $('#loadPicture')[0].style.display='block';
//            loading a html file
            $('#contentarea').load('/blue_pic_scatter', function(){
                $('#loadPicture')[0].style.display='none';
            })
        },
    });

    $('#searchkjrq').bind({
        "click":function(){
            var ball_color = $("#select_ball_color").val();
            var select_condition = $("#select_condition").val();
            var ball = $("#inputkjrq").val();
            $.ajax({url:"/select_condition",
                data:{"ball_color":ball_color, "select_condition":select_condition, "ball":ball},
                dataType:"json",type:"POST",
                success: function(data){

                }})
        },
    });

});


