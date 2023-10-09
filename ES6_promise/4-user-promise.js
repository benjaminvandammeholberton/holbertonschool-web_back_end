function signUpUser(firstName, lastName) {
  return new Promise((resolve) => {
    resolve({ firstName: `${firstName}`, lastName: `${lastName}` });
  });
}
module.exports = signUpUser;
