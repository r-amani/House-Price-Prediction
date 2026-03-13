async function predict(){

document.getElementById("loader").style.display="block";
document.getElementById("result").innerText="";

let button=document.querySelector("button");
button.disabled=true;

let features=[

parseFloat(document.getElementById("qual").value),
parseFloat(document.getElementById("area").value),
parseFloat(document.getElementById("garagecars").value),
parseFloat(document.getElementById("garagearea").value),
parseFloat(document.getElementById("bsmt").value),
parseFloat(document.getElementById("firstflr").value),
parseFloat(document.getElementById("bath").value),
parseFloat(document.getElementById("rooms").value),
parseFloat(document.getElementById("year").value),
parseFloat(document.getElementById("lotshape").value)

];

if(features.some(v => isNaN(v))){
document.getElementById("loader").style.display="none";
document.getElementById("result").innerText="Please fill all fields correctly.";
button.disabled=false;
return;
}

try{

let response=await fetch("https://house-price-prediction-8hdv.onrender.com/predict",{

method:"POST",
headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({features:features})

});

let data=await response.json();

document.getElementById("loader").style.display="none";

if(data.Predicted_Price){

document.getElementById("result").innerText =
"Estimated Price: $" + Math.round(data.Predicted_Price).toLocaleString();

}else{

document.getElementById("result").innerText = "Prediction failed.";

}

}catch(error){

document.getElementById("loader").style.display="none";
document.getElementById("result").innerText="Server error.";

}

button.disabled=false;

}