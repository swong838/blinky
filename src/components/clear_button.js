import React from 'react';
import fetch from 'isomorphic-fetch';
require('es6-promise').polyfill();

class ClearButton extends React.Component {

    constructor(props) {
        super(props);
        this.api = {
            route: '/reset',
            method: 'HEAD'
        }
        this.state = {
            isFetching: false
        }
        this.onInteraction = this.onInteraction.bind(this);
    }

    onInteraction(event) {
        event.preventDefault()
        if (this.state.isFetching) {
            return;
        }
        this.setState({
            isFetching: true
        })

        fetch(this.api.route, {
            method: this.api.method
        })
        .then((response) => {
            console.log(this);
        });
    }

    render() {
        return (
            <button onClick={ this.onInteraction }>Clear</button>
        );
    }
};

export default ClearButton;
