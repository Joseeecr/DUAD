import { userInstance } from "../api/apiClient.js";
import { formatResponse } from "../utils/formatResponse.js";
import { handleApiError } from "../utils/handleApiError.js";

export const createUser = async (name, email, password, address) => {
  try {
    const response = await userInstance.post("collections/users/objects", {
        name: name,
        data: {
          email: email,
          password: password,
          address: address
        }
      });

    return formatResponse(true, response.data, null);

  } catch (error) {
    console.log(handleApiError(error, formatResponse));
    return handleApiError(error, formatResponse);
  };
};


export const getUserById = async (userId) => {
  try {
    const response = await userInstance.get(`collections/users/objects/${userId}`);
    
    return formatResponse(true, response.data, null);

  } catch (error) {
    console.log(handleApiError(error, formatResponse));
    return handleApiError(error, formatResponse);
  };
};


export const updateUserData = async (userId, data) => {
  try {
    const response = await userInstance.patch(`collections/users/objects/${userId}`, data);

    return formatResponse(true, response.data, null);

  } catch (error) {
    console.log(handleApiError(error, formatResponse));
    return handleApiError(error, formatResponse);
  }
}