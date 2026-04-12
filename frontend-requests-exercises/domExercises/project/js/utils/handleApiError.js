export const handleApiError = (error, formatResponse) => {
  if (error.response) {
    const details = error.response?.data?.error || error;
    return formatResponse(false, null, {
      type: "HTTP_ERROR",
      message: error.response.statusText,
      status: error.response.status,
      details: details
    });
  }

  return formatResponse(false, null, {
    type: "NETWORK_ERROR",
    message: error.message,
    status: null
  });
} 