function btnclick() {
    var last = Date.now();
    var btn = document.querySelector('button');
    return function(){
        var now = Date.now();
        if((now - last)>1000){
            btn.innerHTML= '已点击';
        }
        last = now;
    }
}