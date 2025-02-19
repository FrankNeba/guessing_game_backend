
const updateForm = document.getElementById('update')
if (updateForm){
    updateForm.addEventListener('submit', submitt)
}

async function submitt(e) {
    e.preventDefault()
    console.log(e.preventDefault())
    // console.log('clicked')

    const url = 'http://127.0.0.1:8000/api/play/'
    const score = document.getElementById('scorev').value
    const access = localStorage.getItem('access')
    // console.log(access)
     try{
        const response =  await fetch(url, {
            method: 'PUT',
            headers:{
                "Content-Type": "application/json",
                "Authorization": `Bearer ${access} `
            },
            body: JSON.stringify({
                score: score
            })
        } )

        // const data = await response.json()
        // alert(data.data)
        // console.log(data)
        // console.log('oksy')

        // document.getElementById('high').innerHTML = data.data.highestScore
        // console.log(data)
        // alert('okay')
        // document.getElementById('score').innerHTML = data.score
     }
     catch(error){
        console.log(`Error : ${error}`)
     }
    
}



const loginForm = document.getElementById('login')
if (loginForm){
    loginForm.addEventListener('submit', login)
}

async function login(e) {
    console.log('clicked')
    e.preventDefault()
    const url = 'http://127.0.0.1:8000/api/login/'
    const email = document.getElementById('email').value
    const password = document.getElementById('password').value
    // const access = localStorage.getItem('access')
     try{
        const response =  await fetch(url, {
            method: 'POST',
            headers:{
                "Content-Type": "application/json",
                // "Authorization": "Bearer "
            },
            body: JSON.stringify({
                email:email,
                password: password
            })
        } )

        const data = await response.json()
        localStorage.setItem('access',data.access)
        console.log(data)

        // document.getElementById('high').innerHTML = data.highestScore
        // document.getElementById('score').innerHTML = data.score
     }
     catch(error){
        console.log(`Error : ${error}`)
     }
    
}


