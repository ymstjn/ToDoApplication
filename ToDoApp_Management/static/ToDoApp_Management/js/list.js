$(function(){
    $(".hd_inco").click(function(){
        var windowWidth = $(window).width();
        console.log(windowWidth);
        if(windowWidth < 900){
            $(".hd_inco").css("background-color", "cadetblue");
            $(".hd_init").css("background-color", "gray");
            $(".hd_comp").css("background-color", "gray");

            $(".tp_cont1:first-child").css("display", "block");
            $(".tp_cont1:nth-child(2)").css("display", "none");
            $(".tp_cont1:nth-child(3)").css("display", "none");
        }
    });

    $(".hd_init").click(function(){
        var windowWidth = $(window).width();
        
        if(windowWidth < 900){
            $(".hd_inco").css("background-color", "gray");
            $(".hd_init").css("background-color", "cadetblue");
            $(".hd_comp").css("background-color", "gray");

            $(".tp_cont1:first-child").css("display", "none");
            $(".tp_cont1:nth-child(2)").css("display", "block");
            $(".tp_cont1:nth-child(3)").css("display", "none");
        }
    });

    $(".hd_comp").click(function(){
        var windowWidth = $(window).width();
        if(windowWidth < 900){
            $(".hd_inco").css("background-color", "gray");
            $(".hd_init").css("background-color", "gray");
            $(".hd_comp").css("background-color", "cadetblue");
            
            $(".tp_cont1:first-child").css("display", "none");
            $(".tp_cont1:nth-child(2)").css("display", "none");
            $(".tp_cont1:nth-child(3)").css("display", "block");
        }
    });
});
