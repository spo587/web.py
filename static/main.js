
var cardsSelected = []

$(document).ready(function(){
    $('.set-reveal-bttn').on('click', function () {
        var hiddenMessage = $('#numsets').data('what-msg');
        $('#numsets').html(hiddenMessage);
    });

    $('#change-img-bttn').on('click', function () {
        var hidden = $('#change').data('img-path');
        $('#change').attr("src",hidden);
    });
    $('#change-img-bttn-2').on('click', function () {
        var hidden2 = $('#change2').data('img-path2');
        $('#change2').attr("src",hidden2);
    });
    $('#change-img-bttn-3').on('click', function () {
        var hidden3 = $('#change3').data('img-path3');
        $('#change3').attr("src",hidden3);
    });
    
    $('.settile').on('click', function(){
        this.addClass('selected');
        cardsSelected.push(this);
        if(cardsSelected.length == 3){
            $.get('./checkcards',
                cardsSelected,
                function(data){
                    if(data == 'true'){
                        alert('Congrats! You found a set!');
                    } else{
                        alert('That wasn\'t a set - try again!');
                    }
                },
                'text');
            cardsSelected = [];
        }
    });
});

function numberofsets()
{   
    console.log($numsetsonboard);
    document.getElementById("numsets").innerHTML=$numsetsonboard 
}

function displayfirstset(x)
{
    console.log(x)
    document.getElementById("change").src=x
}



