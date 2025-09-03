import jwt

class JWT_Manager:
  def __init__(self, private_key_path, public_key_path, algorithm="RS256"):
    self.algorithm = algorithm 

    with open(private_key_path, "rb") as file:
      self.private_key = file.read()

    with open(public_key_path, "rb") as file:
      self.public_key = file.read()


  def encode(self, data):
    try:
      token = jwt.encode(data, self.private_key, algorithm=self.algorithm)
      return token
    except Exception as e:
        print("Error generating token:", e)
        return None


  def decode(self, token):
    try:
      token = jwt.decode(token, self.public_key, algorithms=[self.algorithm])
      return token
    except Exception as e:
        print(type(token))
        print("Error decoding token:", e)
        return None