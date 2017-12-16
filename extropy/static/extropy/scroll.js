function  scrollFunctionhome(){
    vh = window.innerHeight/100;
    cur_pos = document.documentElement.scrollTop;
    time = Math.abs(cur_pos - (0*vh))*250/(100*vh);

    $("html, body").animate({ scrollTop: String(0*vh) + 'px'}, 2000, "easeOutExpo");

}

function scrollFunctionabout(){
    vh = window.innerHeight/100;
    cur_pos = document.documentElement.scrollTop;
    time = Math.abs(cur_pos - (200*vh))*500/(100*vh);

    $("html, body").animate({ scrollTop: String(200*vh) + 'px'}, 2000, "easeOutExpo");
}
function  scrollFunctionevents(){
    vh = window.innerHeight/100;
    cur_pos = document.documentElement.scrollTop;
    time = Math.abs(cur_pos - (400*vh))*300/(100*vh);

    $("html, body").animate({ scrollTop: String(310*vh) + 'px'}, time, "easeOutExpo");

}