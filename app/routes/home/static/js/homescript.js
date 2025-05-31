    const table = document.getElementById("taskTable")
    const tsk_show_btn = document.getElementById("show_btn")
    const add_task_form = document.getElementById("show_task")
    const close_btn  =  document.getElementById("btn-close")
    const submit_add_btn = document.getElementById("submit")
    const task_title = document.getElementById("task_title")
    const task_description = document.getElementById("task_description")
    const deadline = document.getElementById("deadline")
    const alert_err = document.getElementById("errMsg")
    tsk_show_btn.addEventListener("click" , function(){
      tsk_show_btn.style.display = "none"
      add_task_form.style.display = "block"
    });
    close_btn.addEventListener("click" ,function(){
      tsk_show_btn.style.display = "block"
      add_task_form.style.display = "none"
    });

    submit_add_btn.addEventListener("click", function(){
        if(task_title.value.trim() === "" || task_description.value.trim() === "" || deadline.value === null){
            alert_err.textContent = "Please Fill All The Fields"
        }else{

        post_data()
        }

    })   
    function post_data(){
          
                fetch("/addtask",{
            method : "POST",
                        headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({Task: {task_title:task_title.value , discrtiption:task_description.value , deadline:deadline.value}})
          })
          .then(response => response.json())
          .then(data =>{
            if(data.success){
                row = document.createElement("tr")
                table_task = document.getElementById("tasks")
                row.setAttribute("data-id" , data.id)
                title = document.createElement("th")
                discrtiption = document.createElement("th")
                due_time = document.createElement("th")
                created_time = document.createElement("th")
                time_remaming = document.createElement("th")
                edit = document.createElement("th")
                title.textContent = task_title.value
                discrtiption.textContent = task_description.value
                due_time.textContent = data.due_time
                created_time.textContent =data.created_at
                due_time.setAttribute("class" , "time-left")
                row.appendChild(title)
                row.appendChild(discrtiption)
                row.appendChild(due_time)
                row.appendChild(created_time)
                row.appendChild(time_remaming)
                row.appendChild(edit)
                table_task.appendChild(row)
                // creating the update button
              update_btn = document.createElement("button")
              update_btn.setAttribute("class" , "update_btn")
              update_btn.innerHTML = `
         <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pen-fill" viewBox="0 0 16 16">
        <path d="m13.498.795.149-.149a1.207 1.207 0 1 1 1.707 1.708l-.149.148a1.5 1.5 0 0 1-.059 2.059L4.854 14.854a.5.5 0 0 1-.233.131l-4 1a.5.5 0 0 1-.606-.606l1-4a.5.5 0 0 1 .131-.232l9.642-9.642a.5.5 0 0 0-.642.056L6.854 4.854a.5.5 0 1 1-.708-.708L9.44.854A1.5 1.5 0 0 1 11.5.796a1.5 1.5 0 0 1 1.998-.001"/>
        </svg>
              `;
              //createing the Don or Delete Button
              done_btn = document.createElement("button")
              done_btn.setAttribute("class" , "del_btn")
              done_btn.innerHTML = `
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check2-square" viewBox="0 0 16 16">
  <path d="M3 14.5A1.5 1.5 0 0 1 1.5 13V3A1.5 1.5 0 0 1 3 1.5h8a.5.5 0 0 1 0 1H3a.5.5 0 0 0-.5.5v10a.5.5 0 0 0 .5.5h10a.5.5 0 0 0 .5-.5V8a.5.5 0 0 1 1 0v5a1.5 1.5 0 0 1-1.5 1.5z"/>
  <path d="m8.354 10.354 7-7a.5.5 0 0 0-.708-.708L8 9.293 5.354 6.646a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0"/>
</svg>
              `;
                edit.appendChild(update_btn)
                edit.appendChild(done_btn)
                tsk_show_btn.style.display = "block"
                add_task_form.style.display = "none"
                task_title.value = ""
                task_description.value = ""
                deadline.value = ""
           
              calculate_time(time_remaming , data.created_at , data.due_time)
              }
            else{
              alert_err.textContent = "Error Adding Data Please try again later"
            }
          })
        }
function calculate_time(th, created_at ,due_time){
    const ct = parseCustomDate(created_at)
    const dt = parseCustomDate(due_time)
    console.log(ct)

    const diffMs = dt - ct; // الفرق بالمللي ثانية
    console.log(diffMs)
    if (diffMs <= 0) {
      th.textContent = "انتهى الوقت!";
      clearInterval(intervalId); // وقف التحديث لأنه انتهى الوقت
      return;
    }

    const hours = Math.floor(diffMs / 1000 / 60 / 60);
    const minutes = Math.floor((diffMs / 1000 / 60) % 60);
    const seconds = Math.floor((diffMs / 1000) % 60);

    th.textContent = 
      `الوقت المتبقي: ${hours} ساعة ${minutes} دقيقة ${seconds} ثانية`;
}
function parseCustomDate(dateStr) {
  dateStr = dateStr.replace(/:(AM|PM)$/i, ' $1');
  // الآن التاريخ بصيغة قابلة للقراءة
  return new Date(dateStr);
}

/*document.querySelectorAll('.del_btn').forEach(button =>{
  console.log("test")
  button.addEventListener("click", function(){
  var tr = button.closest("tr")
  const num_row = tr.rowIndex-1
  var em = tr.getAttribute("data-id")
    var table = document.getElementById("tasks")
      table.deleteRow(index=num_row)
  })
})
*/
const tables = document.getElementById('tasks')
tables.addEventListener("click", function(e) {
  // تحقق إذا العنصر المضغوط عليه زر عنده الكلاس del_btn
  if (e.target.classList.contains('del_btn')) {
    const tr = e.target.closest('tr');
    const id = tr.getAttribute('data-id');
    console.log("ID:", id);
    remove_task(id ,tr)
  }
});

function remove_task(id, tr) {
  const csrf = document.getElementById("csrf").value;
  fetch("/remove_task", {
    method: "DELETE",
    headers: {
      'Content-Type': 'application/json',
      "X-CSRFToken": csrf
    },
    body: JSON.stringify({ task_id: id })
  })
  .then(response => {
    if (!response.ok) throw new Error("CSRF verification failed or other error");
    return response.json();
  })
  .then(data => {
    if(data.success){

          tr.remove();
    console.log(data.id_task + " deleted");
    }
    else{
      if(data.redirect === null){
        console.log("data base error")
      }
      else{
        console.log("return to home")
      }
    }
  })
  .catch(error => console.error(error));
}

// logout btn
const log_out_btn = document.getElementById("btn2")
log_out_btn.addEventListener("click" , function(){
  const csrf = document.getElementById("csrf").value;
  fetch("/logout" , {
    method :"POST",
     credentials: 'include',
        headers: {
      'Content-Type': 'application/json',
      "X-CSRFToken": csrf
    },
  }).then(response => response.json())
  .then(data =>{
      if(data.success){
          console.log("done log out")
      }else{
          console.log("error happend")
      }
  })
})