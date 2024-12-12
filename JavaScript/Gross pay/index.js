function calculate(){
    let work=document.getElementById("hoursWorked").value;
    let pay=document.getElementById("hourlyWage").value;
    console.log(work + " = Hours Worked");
    console.log(pay + " = Hourly Wage");
    let resultText;

    if(work > 40){
        let payWithOvertime = (pay * 40) + (pay * 1.5 *(work-40))
        //document.getElementById("results").innerHTML = payWithOvertime;
        console.log(payWithOvertime + " overtime");
        let overtimeHours = work - 40
        resultText = "Gross Pay (with overtime): $" + payWithOvertime.toFixed(2) + "<br> <br>" +"Amount of Overtime Worked: "+overtimeHours;
    }



    else if (work <= 40){
        let regularPay = (work * pay)
        console.log(regularPay + " Regular Pay");
        resultText = "Regular Gross Pay: $" + regularPay.toFixed(2);
    }
    
    
    document.getElementById("result").innerHTML = resultText ;

}