import React, { useState } from 'react';
import { Jumbotron, Spinner} from 'reactstrap';
import PropTypes from 'prop-types';

function FunFact(props) {
    return <div>
                <Jumbotron>
                    <h2>Fun Fact</h2>
                    <p >{props.text}</p>
                    <Spinner color="grey" />
                </Jumbotron>
            </div>
}

export default FunFact;

FunFact.propTypes = {
    text: PropTypes.string
  };