import { url } from './Network.js'


export async function uploadFile(file, token = "") {
    console.log("uploading...")
    token

    let response = await fetch(url + "/file/", {
        method: 'POST',
        headers: {
            Authentication: token
        },
        body: JSON.stringify({
            "name": file.name,
            "public": "True"
        })
    })
    let result = await response.json();
    console.log(result);
    if (response.ok) {
        if (result.status == "ok") {
            console.log(result)
            let data = await file.arrayBuffer();
            response = await fetch(url + "/upload/?url=" + result.url, {
                method: 'POST',
                body: data

            })
            result = await response.json();
            console.log(result);
        }
    } else {
        throw (new Error());
    }
}

export async function downloadFile(file_url, token = "", name = "myfile") {
    let response = await fetch(url + "/file/?url=" + file_url, {
        method: 'GET',
        headers: {
            Authentication: token
        }
    })
    let blob = await response.blob();
    const myurl = URL.createObjectURL(blob);
    download(myurl, name);
}

const download = (path, filename) => {
    const anchor = document.createElement('a');
    anchor.href = path;
    anchor.download = filename;
    document.body.appendChild(anchor);
    anchor.click();
    document.body.removeChild(anchor);
};