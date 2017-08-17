import React from 'react';
import Interactable from './_interactable'
import ColorPicker from 'react-color-picker'
import { hexToRgb } from '../lib/utils'


const label = 'colorpicker';
const api = {
    route: '/setcolor',
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    }
};


class Picker extends Interactable {

    constructor(props) {
        super(props);
        this.label = label;
        this.api = api;
        this.state = {
            color: '#0000ff'
        }
        this.handleDrag = this.handleDrag.bind(this)

    }

    handleDrag(color) {
        this.setState({color});
        this._onInteraction();
    }

    callAPI() {
        return fetch(this.api.route, {
            method: this.api.method,
            headers: this.api.headers,
            body: JSON.stringify(hexToRgb(this.state.color))
        });
    }

    render() {
        //return <ColorPicker value={this.state.color} onDrag={this.handleDrag} onChange={this._onInteraction} />
        return <ColorPicker value={this.state.color} onDrag={this.handleDrag} />
    }
}

export default Picker;
