
const updateForm = document.getElementById('update')
if (updateForm){
    updateForm.addEventListener('submit', submitt)
}

async function submitt(e) {
    e.preventDefault()
    // console.log(e.preventDefault())
    // // console.log('clicked')

    const url = 'http://127.0.0.1:8000/api/play/'
    const score = document.getElementById('scorev').value
    const access = localStorage.getItem('access')
    console.log(access)
    //  try{
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

    //     const data = await response.json()
    //     // alert(data.data)
    //     // console.log(data)
    //     // console.log('oksy')

    //     document.getElementById('high').innerHTML = data.data.highestScore
    //     console.log(data)
    //     alert('okay')
        document.getElementById('score').innerHTML = 'okaty'
    //  }
    //  catch(error){
    //     console.log(`Error : ${error}`)
    //  }
    
}