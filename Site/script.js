window.onload = () => {
    init();
}

function init() {
    $('.submit-checkbox-button').each(handleRadiogroupAnswer);
    $('.submit-input-button').each(handleInputAnswer);
    
    createMouseEventHandlers();
}

function getMousePosition(pointer) {
     //console.log("x: " + pointer.xCoord + "\ty: " + pointer.yCoord);
}

function createMouseEventHandlers() {
    var pointer = Object({}, {
        xCoord:-1,
        yCoord:-1
    });

    setInterval(getMousePosition, 100, pointer);

    $(document).mousemove((event) => {
        pointer.xCoord = event.pageX;
        pointer.yCoord = event.pageY;
    });
}

function handleInputAnswer(index, element) {
    $(element).click(function (event) {
        var parent = $(element).parent();
        if ($(parent).find(".text-input")[0].value != $(parent).find(".answer").text()) {
            return;
        }
        parent.next().show();
        parent.hide();
    });
}

function handleRadiogroupAnswer(index, element) {
    $(element).click(function (event) {
        var parent = $(element).parent();
        if ($(parent).has(":checked").length == 0) {
            return;
        }
        parent.next().show();
        parent.hide();
    });
}
