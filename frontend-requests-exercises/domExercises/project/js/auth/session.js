const STORAGE_KEY = "loggedUserId";

export const saveLoggedUserId = (userId) => {
  localStorage.setItem(STORAGE_KEY, userId)
}


export const getLoggedUserId = () => {
  return localStorage.getItem(STORAGE_KEY);
}


export const removeLoggedUserId = () => {
  localStorage.removeItem(STORAGE_KEY);
}