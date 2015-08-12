/**
 * Created by Gasine on 2015/7/13.
 */
var i=0;
var len = 3;
var dec = true;
function moveimg(){
    if(i==0){dec=true;}
    if(i==(len-1)){dec=false;}
    if(dec){
        i+=1;
        var po=-i*200;
        $(move).animate({left:po+"px"});
    }else{
        i-=1;
        var po=-i*200;
        $(move).animate({left:po+"px"});
    }

}
$(document).ready(function() {
    time = setInterval("moveimg()", 2000);
    $("#show").mouseover(function () {
        window.clearInterval(time);
    });
    $("#show").mouseout(function () {
        time = setInterval("moveimg()", 2000);
    });
    var img;
    $(".img").dblclick(
        function(e){
            $(this).css('cursor','move');
            var offset=$(this).offset();
            var x= e.pageX-offset.left,y= e.pageY-offset.top;
            img = $(this);
            //alert(x);
            $(document).bind("mousemove",function(ev){
                img.stop();
                var _x = ev.pageX-x;
                var _y = ev.pageY-y;


                img.animate({left:_x+"px",top:_y+"px"},10);
            })
        }
    );
    $(document).mouseup(function(){
        if(img){
             img.css("cursor",'default');
        }

        $(this).unbind("mousemove");
    });
    $("#load a").click(function(){
        $(".back").css('display','block');
        $(".sc").css('display','block');
        return false;
    });
    $(".sc .sc_top div").hover(function () {
        $(this).css('cursor','pointer');
    }).click(function () {
        $(".back").css('display','none');
        $(".sc").css('display','none');
    });

    $("#loadimg").change(function(e){
        read = new FileReader();
        file= e.target.files[0];
        read.readAsDataURL(file);
        var re = /image/g;
        if(!re.test(file.type)){
            alert("请选择图片呀！");
        }else{
            read.onload= function () {
                $("#img").html("<img id='preview' src='"+read.result+"'>");
                $("#preview,#img").css({width:'200px',height:'200px',marginLeft:'-100px'});
                $("#height").val("200");
                $("#width").val("200");
            }
        }
    });
    $(".set input").change(function(e){
        var Ele=$(e.target);
        var num = Ele.val().replace(/ /,'');
        if(Number(num)) {
            var ele = Ele.attr("id");

            $("#preview,#img").css(ele,num+"px");
            if(ele=='width') {
                $("#preview,#img").css('margin-left','-'+num/2+"px");
            }
            $("#word").fadeIn().animate({marginTop:"-20px"},1000).fadeOut().css('margin-top', '25px');


        }else{
            alert("输数字啊笨蛋！");
        }
        });
    $("#an").hover(function() {
            $(this).css('cursor', 'pointer');
        }
    );
    $("#an").click(function(){

            if((typeof file)!='undefined'){
                var f = file.name;
                 var hz = f.substr(f.lastIndexOf('.')+1);
                 rea = read.result.substr(read.result.indexOf(',')+1);
                 $.ajax({
                 type: "POST",
                 url: "/getpic",
                 data: {data: rea,houzui:hz},
                 success: function (text) {

                 }}
                 )

            }else{
                 alert("快选图片呀！");
            }

        });

});