import React from 'react';
import Interactable from './_interactable'
import deepcopy from 'deepcopy';

const label = 'test';
const api = {
    route: '/effect',
    method: 'PUT'
};

class TriggerEffect extends Interactable {
    constructor(props) {
        super(props);
        this.label = props.label || label;
        this.api = deepcopy(api);
        this.api.route = [this.api.route, props.effect].join('/')
    }
};

export default TriggerEffect;
