import React from 'react';
import { Route,Redirect } from 'react-router-dom';
import PropTypes from 'prop-types';
import {connect} from 'react-redux';

const privateRoute = ({ component:Component,auth:{isAuthenticated, loading}, ...rest})=>(
    <Route
    {...rest}
    render={props => !isAuthenticated && !loading ? (<Redirect to='/login' />):(<Component{...props} />)} 
    />
);

privateRoute.protoTypes ={
    auth:PropTypes.object.isRequired
};
const mapStateToProps =state => ({
    auth: state.auth
});

export default connect(mapStateToProps)(privateRoute);
