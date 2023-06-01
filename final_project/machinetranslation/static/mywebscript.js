//This is a javascript code to be used in the HTML page through static rendering

let english_to_text = ()=>{
    bookname = document.getElementById(english_text).value;
    

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("updatemessage").innerHTML = xhttp.responseText;
            setTimeout(function(){ 
                document.getElementById("updatemessage").innerHTML = "<br/>"; 
            }, 1000);
            getBook();
        }
    };
    xhttp.open("GET", "english_text/", true);
    xhttp.send();
}

let english_to_fench = ()=>{
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let books = JSON.parse(xhttp.french_text);
            retstr = "<table class='table table-striped' style='width:100%;'><tr><th>English Text</th></tr>"
            books.forEach(element => {
                retstr+="<tr><td>"+element['english_text']+"<tr></tr>"
            }); 
            retstr+="</table>"

            
        }
    };
    xhttp.open("GET", print(french_text), true);
    xhttp.send();
}
