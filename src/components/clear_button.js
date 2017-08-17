import React from 'react';
import Interactable from './_interactable'

const label = 'clear all';
const api = {
    route: '/reset',
    method: 'PUT'
};

class ClearButton extends Interactable {

    constructor(props) {
        super(props);
        this.label = label;
        this.api = api;
    }

};

export default ClearButton;
