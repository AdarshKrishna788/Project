export interface User {
    _id: string;
    fullname: string;
    username: string;
    profilePic: string;
    token: string;
  }

  export interface signupData  {
    fullname: string,
    username:string ,
    password: string,
    confirmPassword: string,
    address: string,
    gender: string 
  };

  export interface loginData  {
    username: string,
    password: string
  };
  