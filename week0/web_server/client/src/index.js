import React from 'react';
import ReactDOM from 'react-dom';
// import App from './App/App';
// import LoginPage from './Login/LoginPage';
// import SignUpPage from './SignUp/SignUpPage';

import {Router, browserHistory} from 'react-router';
import routes from './routes';
import './index.css';

// ReactDOM.render(<App />, document.getElementById('root'));

ReactDOM.render(
    <Router history={browserHistory} routes={routes} />, 
    document.getElementById('root')
);
