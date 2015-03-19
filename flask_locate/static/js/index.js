function handleFileSelect(evt) {
    var file = evt.target.files[0];

    Papa.parse(file, {
        //header: false,
        //dynamicTyping: true,
        complete: function(results) {
            //data = results;
            console.log("Finished:", results.data);
        }
    });
}

$(document).ready(function(){
    $("csv-file").change(handleFileSelect);
});
