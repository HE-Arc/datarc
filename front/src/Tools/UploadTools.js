import { url } from './Network.js'


export function getLink(u) {
    return url + "/file/?url=" + u;
}

export async function uploadFile(file, token = "") {
    console.log("uploading...")
    if (file.size > 2000000) {
        throw (new Error("error the file is too big"));
    }
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
    if (response.ok) {
        if (result.status == "ok") {
            let data = await file.arrayBuffer();
            response = await fetch(url + "/upload/?url=" + result.url, {
                method: 'POST',
                body: data

            })
            result = await response.json();
        }
    } else {
        throw (new Error("error while uploading"));
    }
}

export async function downloadFile(file_url, token = "", name = "myfile") {
    let response = await fetch(url + "/file/?url=" + file_url, {
        method: 'GET',
        headers: {
            Authentication: token
        }
    })
    if (await response.status == 403) {
        throw new Error();
    }
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