async function predict(){

document.getElementById("loader").style.display="block";
document.getElementById("result").innerText="";

let features=[

parseFloat(document.getElementById("medinc").value),
parseFloat(document.getElementById("houseage").value),
parseFloat(document.getElementById("rooms").value),
parseFloat(document.getElementById("bedrooms").value),
parseFloat(document.getElementById("population").value),
parseFloat(document.getElementById("occup").value),
parseFloat(document.getElementById("lat").value),
parseFloat(document.getElementById("long").value)

];

let response=await fetch("https://house-price-prediction-8hdv.onrender.com/predict",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({features:features})

});

let data=await response.json();

document.getElementById("loader").style.display="none";

document.getElementById("result").innerText=
"Predicted Price: $" + Number(data.Predicted_Price).toFixed(2);

}
