import axios from "axios";

export const api = axios.create({
  //baseURL: 'http://172.33.0.2:4000' <- not working, why?
  baseURL: 'http://127.0.0.1:5000'
})

export const fileSharing = async () => {
  let res = await api.post('/', { title: "NewUser", id: 100, username: "Andrey", password: "8282" })
  console.log(res);
}
