export const formatResponse = (success, data, error) => {
  return {
    success,
    data,
    error
  };
};


export const formatLabel = (str) => {
  return str
    .replace(/([A-Z])/g, " $1")
    .replace(/^./, (char) => char.toUpperCase())
    .trim();
};