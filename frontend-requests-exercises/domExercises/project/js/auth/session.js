const storageKey = "session";


export const saveSession = (userId) => {
  localStorage.setItem(storageKey, JSON.stringify({userId: userId, loginAt: Date.now()}))
}


export const getSession = () => {
  const session = localStorage.getItem(storageKey);
  if(!session){
    return null;
  }
  return JSON.parse(session);
}


export const hasSessionExpired = (session) => {
  if((!session) || (!session.loginAt) || (Date.now() - session.loginAt > 300000)){
    return true;
  }

  return false;
}


export const clearSession = () => {
  localStorage.removeItem(storageKey);
}