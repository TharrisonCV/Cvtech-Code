const firstName = []


function validateInput() {
      // Get the input value
      var inputValue = document.getElementById('inputText').value;

      // Check if the input contains only alphabets using a regular expression
      if (/^[a-zA-Z]+$/.test(inputValue)) {
            /*
        // If true, display in an array
        var resultArray = inputValue.split('');
        document.getElementById('result').textContent = 'Result Array: [' + resultArray.join(', ') + ']';
        */

        firstName.push(inputValue);
        document.getElementById('result').innerHTML = "Result: "(firstName);
      } else {
        // If false, display "blank"
        document.getElementById('result').textContent = 'Result: blank';
      }
}