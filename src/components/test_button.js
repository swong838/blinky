import React from 'react';
import Interactable from './_interactable'

const label = 'test';
const api = {
    route: '/test',
    method: 'PUT'
};

class TestButton extends Interactable {

    constructor(props) {
        super(props);
        this.label = label;
        this.api = api;
    }

};

export default TestButton;
