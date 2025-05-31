    const usernameInput = document.getElementById("username");
    const email = document.getElementById('password');
    const usernameMsg = document.getElementById('usernameMsg');
    const errbox = document.getElementById("errMsg");
    let username_bool = false;
    // نراقب التغيير على حقل اسم المستخدم
    usernameInput.addEventListener('input', () => {
        const username = usernameInput.value.trim();
        if (username.length === 0) {
            usernameMsg.textContent = '';
            return;
        }

        fetch('/check_username', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({username: username})
        })
        .then(response => response.json())
        .then(data => {
            if(data.exists){
                username_bool = true
                usernameMsg.textContent = data.message;
                console.log(data.message)
                usernameMsg.style.display = 'flex'
            } else {
                username_bool = false
                usernameMsg.textContent = '';

            }
        })
        .catch(err => {
            console.error('Error:', err);
        });
    });
    document.addEventListener('DOMContentLoaded', () => {
      const form = document.getElementById('registerForm');
      form.addEventListener('submit', function(event) {
      

        


        if (username.value.trim() === '' || email.value.trim() === '') {
            errbox.textContent = "Please fill all fields";
            errbox.style.display = "flex"
            event.preventDefault();
        }else if(username_bool){
            errbox.textContent = "User Name is already Exist";
            errbox.style.display = "flex"
            event.preventDefault();
        }

      });
    });
  