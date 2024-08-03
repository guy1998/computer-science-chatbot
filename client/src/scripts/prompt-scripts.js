const url = "http://localhost:1989";

const sendPrompt = async (prompt, notification)=>{
    const response = await fetch(`${url}/chat`, {
        method: "POST",
        headers: {
            "Content-type": 'application/json'
        },
        body: JSON.stringify({ prompt })
    });
    let answer = ""
    if(response.status === 200) {
        answer = response.json();
    } else {
        notification.add("Something went wrong!", { variant: 'error' });
    }
    return answer
}