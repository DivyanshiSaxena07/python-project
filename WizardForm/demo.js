




// $.validator.addMethod("firstNameRegex",function(value , element){
//     return this.optional(element) || /^[a-zA-Z ]*$/i.test(value)
//   },"Please Enter Valid Name...");
//   $.validator.addMethod("lastNameRegex",function(value , element){
//     return this.optional(element) || /^[a-zA-Z ]*$/i.test(value)
//   },"Please Enter Valid Name...");
//   $.validator.addMethod("fatherNameRegex",function(value , element){
//     return this.optional(element) || /^[a-zA-Z ]*$/i.test(value)
//   },"Please Enter Valid Name...");
//   $.validator.addMethod("aadharRegex",function(value , element){
//     return this.optional(element) || /^\d{4}\d{4}\d{4}$/i.test(value)
//   },"Please Enter Valid Adhar Number...");
//   $.validator.addMethod("panRegex",function(value , element){
//     return this.optional(element) || /^([a-zA-Z]){5}([0-9]){4}([a-zA-Z]){1}?$/i.test(value)
//   },"Please Enter Valid Pan Number...");
//   $.validator.addMethod("emailRegex",function(value , element){
//     return this.optional(element) || /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/i.test(value)
//   },"Please Enter Valid Emai Id...");
//   $.validator.addMethod("contactRegex",function(value , element){
//     return this.optional(element) || /^\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$/i.test(value)
//   },"Please Enter Valid Mobile Number...");
//   $.validator.addMethod("alternetContactRegex",function(value , element){
//     return this.optional(element) || /^\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$/i.test(value)
//   },"Please Enter Valid Mobile Number...");
//   $.validator.addMethod("pinCodeRegex",function(value , element){
//     return this.optional(element) || /^\d{4}$|^\d{6}$/i.test(value)
//   },"Please Enter Valid Pin Code...");
//   $.validator.addMethod("ifscRegex",function(value , element){
//     return this.optional(element) || /^[A-Z]{4}0[A-Z0-9]{6}$/i.test(value)
//   },"Please Enter Valid IFSC Code...");








var x =$('#multi-step-form').validate({
      rules: {
        fname: {
          required: true,
          minlength: 2,
        },
        lname: {
          required: true,
          minlength: 2,
        },
        email: {
          required: true,
          email: true,//add an email rule that will ensure the value entered is valid email id.
          maxlength: 255,
        },
        number: {
          required: true,
          minlength: 10,
          maxlength: 10
        },
        gender: {
          required: true,
        },
        fathername: {
          required: true,
          minlength: 2,
        },
        smdId: {
          required: true,
          minlength: 8,
          maxlength: 8,
        },
        pan: {
          required: true,
        },
        date: {
          required: true,
        },
        adhar: {
          required: true,
        },
        nName: {
          required: true,
          minlength: 2,
        },
        age: {
          required: true,
        },
        relation: {
          required: true,
        },
        accNo: {
          required: true,
        },
        ifsc: {
          required: true,
        },
        hno: {
          required: true,
        },
        address: {
          required: true,
        },
        browser: {
          required: true,
        },
        city: {
          required: true,
        },
        landmark: {
          required: true,
        },
        hno1: {
          required: true,
        },
        address1: {
          required: true,
        },
        browser1: {
          required: true,
        },
        city1: {
          required: true,
        },
        landmark1: {
          required: true,
        },
      },
    //   messages: {
    //     fname: 'This field is required',
    //     lname: 'This field is required',
    //     email: 'Enter a valid email',
    //   },
    //   submitHandler: function (form) {
    //     form.submit();
    //   }
    });
    


    $(".step-next-1").click(function() {
        debugger
        if (x.form()) {
          $('#step-group-1').attr('style', 'display:none')
          $('#step-group-2').attr('style', 'display:block')
          $('#step2').addClass("active")
        }
      });   

      $(".step-next-2").click(function() {
        debugger
        if (x.form()) {
          $('#step-group-2').attr('style', 'display:none')
          $('#step-group-3').attr('style', 'display:block')
          $('#step3').addClass("active")
        }
      });   
      
      
      $(".step-next-3").click(function() {
        debugger
        if (x.form()) {
          $('#step-group-3').attr('style', 'display:none')
          $('#step-group-4').attr('style', 'display:block')
          $('#step4').addClass("active")
        }
      });   


      $(".step-next-4").click(function() {
        debugger
        if (x.form()) {
          $('#step-group-4').attr('style', 'display:none')
          $('#step-group-5').attr('style', 'display:block')
          $('#step5').addClass("active")
        }
      });   

// previous==================

$(".step-prev-1").click(function() {
    debugger
    if (x.form()) {
      $('#step-group-1').attr('style', 'display:block')
      $('#step-group-2').attr('style', 'display:none')
      $('#step2').removeClass("active")
    }
  });   

  $(".step-prev-2").click(function() {
    debugger
    if (x.form()) {
        $('#step-group-2').attr('style', 'display:block')
        $('#step-group-3').attr('style', 'display:none')
        $('#step3').removeClass("active")
    }
  });   


  $(".step-prev-3").click(function() {
    debugger
    if (x.form()) {
        $('#step-group-3').attr('style', 'display:block')
        $('#step-group-4').attr('style', 'display:none')
        $('#step4').removeClass("active")
    }
  });   

  $(".step-prev-4").click(function() {
    debugger
    if (x.form()) {
        $('#step-group-4').attr('style', 'display:block')
        $('#step-group-5').attr('style', 'display:none')
        $('#step5').removeClass("active")
    }
  });   


//   reset button

$(".reset-btn").click(function() {
    debugger
    if (x.form()) {
      $('#sucess-box').attr('style', 'display:none')
      $('form-container-box').attr('style', 'display:none')
      window.location.reload();
    }
  });   
$(".step-preview-1").click(function(){
    getCookie($(this).attr("name"));
    $('form-container-box').attr('style', 'display:none')
    $('#preview-page').attr('style', 'display:flex')
})


function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    let expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
  }
  
  
  function getCookie(cname) {
    let name = cname + "=";
    
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
    user = "";
    if (user != "") {
      alert("Welcome again " + user);
    } else {
      $('.form-field').each(function () {
        setCookie($(this).attr('name'), $(this).val(), 30)
  
      });
    }
  }