window.onload = () => {
    myName = "NO_NAME"
    init();
}

function init() {
    $('.submit-radiogroup-button').each(handleRadiogroupAnswer);
    $('.submit-input-button').each(handleInputAnswer);
    $('#next-button-with-name').each(handleNextButtonWithName);
    
    this.log = "";

    createMouseEventHandlers();
    createKeyboardEventHandlers();
}

function handleNextButtonWithName(index, element) {
    $(element).click(function (event) {
        var parent = $(element).parent();
        var value = $(parent).find("#name-input")[0].value;
        if (value == "") {
            return;
        }
        myName = value;
        parent.next().show();
        parent.hide();
    });
}

function createKeyboardEventHandlers() {
    $(".text-input").keydown((event) => {
        this.log += "KEY_PRESS " + event.key + " " + Date.now() + '\n';
    });

    $(".text-input").keyup((event) => {
        this.log += "KEY_RELEASE " + event.key + " " + Date.now() + '\n';
    });
}

function getMousePosition(pointer) {
    this.log += "MOUSE_POSITION " + pointer.xCoord + " " + pointer.yCoord + " " + Date.now() + '\n';
}

function createMouseEventHandlers() {
    var pointer = Object({}, {
        xCoord:-1,
        yCoord:-1
    });

    setInterval(getMousePosition, 50, pointer);

    $(document).mousemove((event) => {
        pointer.xCoord = event.pageX;
        pointer.yCoord = event.pageY;
    });

    $(document).mousedown((event) => {
        this.log += "MOUSE_PRESS " + event.pageX + " " + event.pageY + " " + Date.now() + '\n';
    });
    $(document).mouseup((event) => {
        this.log += "MOUSE_RELEASE " + event.pageX + " " + event.pageY + " " + Date.now() + '\n';
    });

    $("#btnExport").click((event) => {
        newFile(this.log)
    });
}

function newFile(data) {
    data = myName + '\n' + data
    var blob = new Blob([data], {type: "octet/stream"});
    var url  = window.URL.createObjectURL(blob);
    window.location.assign(url);
}

function handleInputAnswer(index, element) {
    $(element).click(function (event) {
        var parent = $(element).parent();
        if ($(parent).find(".text-input")[0].value != $(parent).find(".answer").text()) {
            //return;
        }
        parent.next().show();
        parent.hide();
    });
}

function handleRadiogroupAnswer(index, element, count=0) {
    $(element).click(function (event) {
        var parent = $(element).parent();
        if ($(parent).has(":checked").length == count) {
            return;
        }
        parent.next().show();
        parent.hide();
    });
}
