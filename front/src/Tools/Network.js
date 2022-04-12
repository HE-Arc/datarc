//export const url = "http://127.0.0.1:8000/api";
export const url = "https://datarc.srvz-webapp.he-arc.ch/api";

async function getData(page, headers = {}) {
    let request = await fetch(url + page + "/", { headers: headers })
    let data = await request.json()
    if (request.ok) {
        return data
    } else {
        throw (new Error());
    }
}

async function fileUpdate(action, headers = {}, u) {
    let request = await fetch(url + "/" + action + "/" + "?url=" + u, { headers: headers })
    let data = await request.json()
    if (request.ok) {
        return data
    } else {
        throw (new Error());
    }
}

async function sendData(page, params = {}, body = "") {
    let urlParams = Object.keys(params).length != 0 ? "?" + new URLSearchParams(params).toString() : "";
    let request = await fetch(url + page + urlParams + "/", {
        method: "post",
        body: JSON.stringify(body)
    })
    let result = await request.json()
    if (request.ok) {
        return result
    } else {
        throw (new Error());
    }
}

export {
    getData,
    sendData,
    fileUpdate
}