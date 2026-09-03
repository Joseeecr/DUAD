const BASE_API_URL = "http://127.0.0.1:5000";

export const baseApiUrlInstance = axios.create({
  baseURL: BASE_API_URL
});

export { BASE_API_URL };