function myFunction(){
    var userInput = parseInt(document.getElementById("DataEntry").value);
    console.log(userInput);
    let radio1 = document.getElementById("fahrenheit");
    if (radio1.checked){
        let updatedF = (userInput*9/5)+32
        document.getElementById("result").value = updatedF + " °F";
        console.log(updatedF);
    }
    else{
        let updatedC = (userInput - 32)*5/9
        document.getElementById("result").value = updatedC + " °C";
        console.log(updatedC);
    }
}   