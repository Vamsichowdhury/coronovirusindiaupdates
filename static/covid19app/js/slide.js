
var i=0;
var images=[];
var time =3000;
images[0]='/static/covid19app/images/1.png';
images[1]='/static/covid19app/images/2.png';
images[2]='/static/covid19app/images/3.png';
images[3]='/static/covid19app/images/4.png';
images[4]='/static/covid19app/images/5.png';
images[5]='/static/covid19app/images/6.png';
images[6]='/static/covid19app/images/7.png';
images[7]='/static/covid19app/images/8.png';

function changeImg(){

    document.slide.src =images[i];

    if(i<images.length-1){
        i++;
    }
    else{
        i=0;
    }
    setTimeout("changeImg()", time);
}

window.onload = changeImg;