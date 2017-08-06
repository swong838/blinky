import React from 'react';
import Button from './_button'

const label = 'clear';
const api = {
    route: '/reset',
    method: 'PUT'
};

class ClearButton extends Button {

    constructor(props) {
        super(props);
        this.label = label;
        this.api = api;
    }

};

export default ClearButton;