import signUpUser from './4-user-promise'; // Correct file path
import uploadPhoto from './5-photo-reject'; // Correct file path

function handleProfileSignup(firstName, lastName, fileName) {
  const promises = [signUpUser(firstName, lastName), uploadPhoto(fileName)];

  return Promise.allSettled(promises).then((results) => results.map((result) => {
    if (result.status === 'fulfilled') {
      return {
        status: 'fulfilled',
        value: result.value,
      };
    }
    return {
      status: 'rejected',
      value: result.reason.message,
    };
  }));
}

export default handleProfileSignup;
