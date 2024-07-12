function inicia(){

  let user=document.getElementById('user').value;
  let pass=document.getElementById('pass').value;

  if(user== 'Alan' & pass== '1234'){

  window.location="mirasolapp/index";

  }

  else{
    if(user== 'Benja' & pass== '4321'){
    
    window.location="mirasolapp/seleccionVista";

    }

    else{

      document.getElementById('mensaje3').textContent = "Usuario o Contraseña incorrecta" ;
      document.getElementById('mensaje3').style.color='red';
      setTimeout(() => {
      document.getElementById('mensaje3').textContent = "" ;
      }, 2000);
      
      document.getElementById('user').value=''; 
      document.getElementById('pass').value='';

    }

    
  }

}

//-----------------------------------------------------------

const modalContainer = document.getElementById('contenedor-modal');
const closeButton = document.getElementById('cerrar-modal');


function abrirModal() {
modalContainer.style.display = 'block';
}


function cerrarModal() {
modalContainer.style.display = 'none';
}


const triggerElement = document.getElementById('boton-modal');
triggerElement.addEventListener('click', abrirModal);
closeButton.addEventListener('click', cerrarModal);

//---------------------------------------------------
function datos() {
let mail = document.getElementById('mail').value;
let fono = document.getElementById('fono').value;
let com = document.getElementById('mensaje').value;
let nombre = document.getElementById('nombre').value;

var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

if (!emailRegex.test(mail)) {
  document.getElementById('mensaje').textContent = "Por favor ingrese un correo electrónico válido.";
  document.getElementById('mensaje').style.color = 'red';
  setTimeout(() => {
    document.getElementById('mensaje').textContent = "";
  }, 3000);
  return false;
}

if (nombre !== '' && mail !== '' && fono !== '' && com !== '') {
  document.getElementById('mensaje2').textContent = "Enviado exitosamente";
  document.getElementById('mensaje2').style.color = "green";


  setTimeout(function() {
    document.getElementById('mail').value = '';
    document.getElementById('fono').value = '';
    document.getElementById('nombre').value = '';
    document.getElementById('mensaje').value = '';
  }, 1000);

  return false;
} else {
  document.getElementById('mensaje2').textContent = "Por favor rellene todos los campos";
  document.getElementById('mensaje2').style.color = "red";
  setTimeout(() => {
    document.getElementById('mensaje2').textContent = "";
  }, 5000);
  return false;
}
}

//---------------------------------------------------------------------------------

function iniciarMap(){
var coord = {lat:-41.4744082 ,lng: -72.9966483};
var map = new google.maps.Map(document.getElementById('map'),{
  zoom: 15,
  center: coord
});
var marker = new google.maps.Marker({
  position: coord,
  map: map
});
}

