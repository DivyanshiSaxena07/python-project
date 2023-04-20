
var obj = [{ entry: 'Fname', type: 'text' }, { entry: 'Lname', type: 'text' },
{ entry: 'Email', type: 'email' }, { entry: 'Number', type: 'number' }, { entry: 'Gender', type: 'radio' },
{ entry: 'FatherName', type: 'text' }, { entry: 'SMID', type: 'number' }, { entry: 'PanCard', type: 'text' },
{ entry: 'Date', type: 'date' }, { entry: 'AdharCard', type: 'text' }, { entry: 'NomineeName', type: 'text' },
{ entry: 'NomineeAge', type: 'number' }, { entry: 'NomineeAccNo', type: 'text' }, { entry: 'NomineeIFSC', typr: 'text' },
{ entry: 'Relation', type: 'text' }, { entry: 'HouseNo', type: 'number' }, { entry: 'Address', type: 'text' },
{ entry: 'State', type: 'select' }, { entry: 'City', type: 'text' }, { entry: 'Landmark', type: 'text' }
]




// var x =$('#multi-step-form').validate({
//   rules: {
//         fname:{
//                 required:true,
//                 minlength:2,
//               },
//         lname:{
//               required:true,
//               minlength:2,
//             },
//         email:{
//               required: true,
//               email: true,//add an email rule that will ensure the value entered is valid email id.
//               maxlength: 255,
//             },
//         number:{
//               required:true,
//               minlength:10,
//               maxlength:10
//         },
//         gender:{
//           required:true,
//         },
//         fathername:{
//           required:true,
//           minlength:2,
//         },
//         smdId:{
//           required:true,
//           minlength:8,
//           maxlength:8,
//         },
//         pan:{
//           required:true,
//         },
//         date:{
//           required:true,
//         },
//         adhar:{
//           required:true,
//         },
//         nName:{
//           required:true,
//           minlength:2,
//         },
//         age:{
//           required:true,
//         },
//         relation:{
//           required:true,
//         },
//         accNo:{
//           required:true,
//         },
//         ifsc:{
//           required:true,
//         },
//         hno:{
//           required:true,
//         },
//         address:{
//           required:true,
//         },
//         browser:{
//           required:true,
//         },
//         city:{
//           required:true,
//         },
//         landmark:{
//           required:true,
//         },
//         hno1:{
//           required:true,
//         },
//         address1:{
//           required:true,
//         },
//         browser1:{
//           required:true,
//         },
//         city1:{
//           required:true,
//         },
//         landmark1:{
//           required:true,
//         },
  
//       messages:{
//           fname: 'This field is required',
//           lname: 'This field is required',
//         email: 'Enter a valid email',
//        },  
// }
// });





window.addEventListener("load", () => {
  const form = document.getElementById("multi-step-form");
  const formcontainerbox = document.getElementById("form-container-box");
  const step2 = document.getElementById("step2");
  const step3 = document.getElementById("step3");
  const step4 = document.getElementById("step4");
  const step5 = document.getElementById("step5");

  const stepgroup1 = document.getElementById("step-group-1")
  const stepgroup2 = document.getElementById("step-group-2")
  const stepgroup3 = document.getElementById("step-group-3")
  const stepgroup4 = document.getElementById("step-group-4")
  const stepgroup5 = document.getElementById("step-group-5")

  const stepnext1 = document.getElementById("step-next-1")
  const stepnext2 = document.getElementById("step-next-2")
  const stepnext3 = document.getElementById("step-next-3")
  const stepnext4 = document.getElementById("step-next-4")

  const stepprev1 = document.getElementById("step-prev-1")
  const stepprev2 = document.getElementById("step-prev-2")
  const stepprev3 = document.getElementById("step-prev-3")
  const stepprev4 = document.getElementById("step-prev-4")

  const sucessbox = document.getElementById("sucess-box")
  const steppreview = document.getElementById("step-preview-1")
  const stepsubmit = document.getElementById("step-submit-1")
  const resetButton = document.getElementById("reset-btn")
  const prevbox = document.getElementById("preview-page")

  form.addEventListener("submit", (e) => {
    e.preventDefault()

  })

  stepnext1.addEventListener("click", function next1() {
    var fname = document.getElementsByName('fname')[0].value;
    var lname = document.getElementsByName('lname')[0].value;
    var email = document.getElementsByName('email')[0].value;
    var number = document.getElementsByName('number')[0].value;
    var gender = document.getElementsByName('gender')[0].value;
    var arr = [fname, lname, email, number, gender]
    var count = 0;


    for (let i = 0; i < arr.length; i++) {
      if (arr[i].length != 0)
        if (fname.match(/[a-zA-Z]+/) && lname.match(/[a-zA-Z]/))
          count++;
    }

    if (arr.length == count) {
      stepgroup1.style.display = "none";
      stepgroup2.style.display = "block";
      step2.classList.add("active")
    }
  })


  stepnext2.addEventListener("click", function next2() {
    var fathername = document.getElementsByName('fathername')[0].value;
    var smdId = document.getElementsByName('smdId')[0].value;
    var pan = document.getElementsByName('pan')[0].value;
    var date = document.getElementsByName('date')[0].value;
    var adhar = document.getElementsByName('adhar')[0].value;
    var count = 0;
    var arr = [fathername, smdId, pan, date, adhar]
    for (let i = 0; i < arr.length; i++) {

      if (arr[i].length != "")
        count++;
      if (arr.length == count) {
        stepgroup2.style.display = "none";
        stepgroup3.style.display = "block";
        step3.classList.add("active")
      }
    }
  })

  stepnext3.addEventListener("click", () => {
    var nName = document.getElementsByName('nName')[0].value;
    var age = document.getElementsByName('age')[0].value;
    var relation = document.getElementsByName('relation')[0].value;
    var accNo = document.getElementsByName('accNo')[0].value;
    var ifsc = document.getElementsByName('ifsc')[0].value;
    var count = 0;
    var arr = [nName, age, relation, accNo, ifsc]
    for (let i = 0; i < arr.length; i++) {

      if (arr[i].length != "")
        count++;
      if (arr.length == count) {
        stepgroup3.style.display = "none";
        stepgroup4.style.display = "block";
        step4.classList.add("active")
      }
    }
  })
  stepnext4.addEventListener("click", () => {
    var hno = document.getElementsByName('hno')[0].value;
    var address = document.getElementsByName('address')[0].value;
    var browser = document.getElementsByName('browser')[0].value;
    var city = document.getElementsByName('city')[0].value;
    var landmark = document.getElementsByName('landmark')[0].value;
    var count = 0;
    var arr = [hno, address, browser, city, landmark]
    for (let i = 0; i < arr.length; i++) {

      if (arr[i].length != "") {
        if (hno.match(/[a-zA-Z0-9]+/))
          count++;

      }
      if (arr.length == count) {
        stepgroup4.style.display = "none";
        stepgroup5.style.display = "block";
        step5.classList.add("active")
      }
    }
  })

  stepprev1.addEventListener("click", () => {
    stepgroup1.style.display = "block";
    stepgroup2.style.display = "none";
    step2.classList.remove("active");
  })

  stepprev2.addEventListener("click", () => {
    stepgroup2.style.display = "block";
    stepgroup3.style.display = "none";
    step3.classList.remove("active");
  })

  stepprev3.addEventListener("click", () => {
    stepgroup3.style.display = "block";
    stepgroup4.style.display = "none";
    step4.classList.remove("active");
  })

  stepprev4.addEventListener("click", () => {
    stepgroup4.style.display = "block";
    stepgroup5.style.display = "none";
    step5.classList.remove("active");
  })

  stepsubmit.addEventListener("click", () => {
    var hno = document.getElementsByName('hno1')[0].value;
    var address = document.getElementsByName('address1')[0].value;
    var browser = document.getElementsByName('browser1')[0].value;
    var city = document.getElementsByName('city1')[0].value;
    var landmark = document.getElementsByName('landmark1')[0].value;
    var count = 0;
    var arr = [hno, address, browser, city, landmark]
    for (let i = 0; i < arr.length; i++) {

      if (arr[i].length != "")
        count++;
      if (arr.length == count) {

        formcontainerbox.style.display = "none";
        sucessbox.style.display = "flex";
      }
    }
  })

  steppreview.addEventListener("click", () => {
    getCookie($(this).attr("name"));
    formcontainerbox.style.display = "none";
    prevbox.style.display = "flex";
    // document.getElementById('basic-detail').innerHTML = ''

  })

  resetButton.addEventListener("click", () => {
    sucessbox.style.display = "none";
    formcontainerbox.style.display = "none";
    window.location.reload();
  })

})

function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  let expires = "expires=" + d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}


function getCookie(cname) {
  let name = cname + "=";
  // console.log(name)
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
      console.log(c)
    }
    document.getElementById('preview-page').innerHTML += c;
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}




function saveData() {
  const form = document.getElementById('multi-step-form');
  const forData = new FormData(form)
  const data = [...forData.entries()]
  // console.log(data)
  // let user = getCookie($(this).attr("name"));
  user = "";
  if (user != "") {
    alert("Welcome again " + user);
  } else {
    $('.form-field').each(function () {
      setCookie($(this).attr('name'), $(this).val(), 30)

    });
  }
}

function next1(e) {

  e.preventDefault();

}


// Cookies=+++++++++++++++++++++++++++++++


