    $(".delete_experience").on("click", function() {
     var experience_id = $(this).attr('experienceId');
     var doctor_id ={{doctor.id}}
     console.log("experience_id "+experience_id)
     console.log(doctor_id)


    swal.fire({
    title: 'هل  تريد ان تحذف الخبرة  ؟',
    type: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'نعم',
    closeOnConfirm: true,
    closeOnCancel: true
   }).then((result) => {
      if (result.value===true) {
$.ajax(
    {
      type: "GET",
      url: '{% url "dashboard_site:delete_doctor_experience" %}',
      data:{"doctor_id":doctor_id,"experience_id":experience_id, content:'mrcboy'},
      success: function () {
        console.log("is deleted deleted")
        location.reload();
      },
      error: function (xhr, statusText, err) {
        alert("error"+xhr.status);
      }
    });
      }
   })
})
