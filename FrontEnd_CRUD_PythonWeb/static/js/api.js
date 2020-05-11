getUser();
async function getUser() {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/user/v01/get-all');
        console.log(response.data);
        let content = '';
        response.data.forEach(element => {
            content += `
            <tr>
                    <td>
                        <span class="custom-checkbox">
                            <input type="checkbox" id="checkbox1" name="options[]" value="1">
                            <label for="checkbox1"></label>
                        </span>
                    </td>
                    <td>${element.uid}</td>
                    <td>${element.uname}</td>
                    <td>${element.uemail}</td>
                    <td>${element.ucontact}</td>
                    <td>
                        <a href="#editEmployeeModal" onclick="getUserById(${element.id})" class="edit" data-toggle="modal"><i class="material-icons"
                                data-toggle="tooltip" title="Edit">&#xE254;</i></a>
                        <a href="#deleteEmployeeModal" onclick="deleteUserById(${element.id})" class="delete" data-toggle="modal"><i class="material-icons"
                                data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                    </td>
            </tr>
            
            
            
            `
        });
        document.getElementById('list_user').innerHTML = content;
    } catch (error) {
        console.error(error);
    }
}



async function addUser() {
    let uid = document.getElementById('uid').value;
    let uname = document.getElementById('uname').value;
    let uemail = document.getElementById('uemail').value;
    let ucontact = document.getElementById('ucontact').value;
    let upassword = document.getElementById('upassword').value;
    try {
        const response = await axios.post('http://127.0.0.1:8000/api/user/v01/add', {
            "uid": uid,
            "uname": uname,
            "uemail": uemail,
            "ucontact": ucontact,
            "upassword": upassword
        });
        console.log(response);
    } catch (error) {
        console.error(error);
    }

}


async function deleteUserById(id) {
    // let uid= document.getElementById('uid').value;
    // let uname= document.getElementById('uname').value;
    // let uemail= document.getElementById('uemail').value;
    // let ucontact= document.getElementById('ucontact').value;
    // let upassword= document.getElementById('upassword').value;
    try {
        const response = await axios.delete('http://127.0.0.1:8000/api/user/v01/delete/' + id);
        console.log(response);
        getUser();
    } catch (error) {
        console.error(error);
    }

}


async function getUserById(id) {
    // let uid= document.getElementById('uid').value;
    // let uname= document.getElementById('uname').value;
    // let uemail= document.getElementById('uemail').value;
    // let ucontact= document.getElementById('ucontact').value;
    // let upassword= document.getElementById('upassword').value;
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/user/v01/edit/' + id);
        console.log(response.data);
        let data = response.data
        document.getElementById('uid_edit').value = data.uid;
        document.getElementById('uname_edit').value = data.uname;
        document.getElementById('uemail_edit').value = data.uemail;
        document.getElementById('ucontact_edit').value = data.ucontact;
        document.getElementById('upassword_edit').value = data.upassword;
        document.getElementById('id_user_edit').value = data.id;
        id_user_edit
    } catch (error) {
        console.error(error);
    }

}




async function updateUser() {
    let id = document.getElementById('id_user_edit').value
    let uid = document.getElementById('uid_edit').value;
    let uname = document.getElementById('uname_edit').value;
    let uemail = document.getElementById('uemail_edit').value;
    let ucontact = document.getElementById('ucontact_edit').value;
    let upassword = document.getElementById('upassword_edit').value;
    try {
        const response = await axios.put('http://127.0.0.1:8000/api/user/v01/update/' + id, {
            "id": id,
            "uid": uid,
            "uname": uname,
            "uemail": uemail,
            "ucontact": ucontact,
            "upassword": upassword
        });
        console.log(response);
    } catch (error) {
        console.error(error);
    }

}