import React from 'react';
import Interactable from './_interactable'
import ColorPicker from 'react-color-picker'


const label = 'colorpicker';
const api = {
    route: '/reset',
    method: 'PUT'
};


class Picker extends Interactable {

    constructor(props) {
        super(props);
        this.label = label;
        this.api = api;
    }

    getInitialState() {
        return {
            color: 'blue'
        };
    }
//
    handleDrag(color) {
        console.log(color); // color is rgb(a) string
        this.setState({color});
    }
//
    //callAPI() {
    //    return fetch(this.api.route, {
    //        method: this.api.method
    //    })
    //}
    render() {

        return (
            <div>
                <h4>{ this.label }</h4>
                <ColorPicker value={this.state.color} onDrag={this.handleDrag.bind(this)} opacitySlider />
            </div>
        );
    }
}

export default Picker;
