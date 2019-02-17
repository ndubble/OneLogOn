import jwt_decode from 'jwt-decode';
import isValidJWT from 'utils/isValidJWT';

function me(url, options) {
  const jwt = localStorage.getItem('jwt');
  if (!jwt || !isValidJWT(jwt)) {
    return {};
  }
  try {
    const decodedJwt = jwt_decode(jwt);
    // console.log(decodedJwt);

    // TODO: change to real values
    return {
      name: decodedJwt.user_id,
      role: 'admin',
    };
  } catch (err) {
    console.error(err);
    return {};
  }
}

export default me;
