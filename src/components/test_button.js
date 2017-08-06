import React from 'react';
import Button from './_button'

const label = 'test';
const api = {
    route: '/test',
    method: 'PUT'
};

class TestButton extends Button {

    constructor(props) {
        super(props);
        this.label = label;
        this.api = api;
    }

};

export default TestButton;
