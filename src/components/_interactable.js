import React from 'react';
import fetch from 'isomorphic-fetch';
import promise from 'es6-promise';

promise.polyfill();

const label = 'changeme';
const api = {
    route: '',
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
};


class Interactable extends React.Component {

    constructor(props) {
        super(props);
        this.label = label;
        this.api = api;
        this.state = {
            isFetching: false
        }
        this._onInteraction = this._onInteraction.bind(this);
        this.afterInteraction = this.afterInteraction.bind(this);
        this.callAPI = this.callAPI.bind(this);
    }

    _onInteraction(event) {
        event && event.preventDefault && event.preventDefault();
        if (this.state.isFetching) {
            return;
        }
        this.setState({
            isFetching: true
        })

        this.callAPI().then((response) => {
                this.afterInteraction(response);
            })
            .then(() => {
                this.setState({
                    isFetching: false
                })
            });
    }

    callAPI() {
        return fetch(this.api.route, {
            method: this.api.method,
            headers: this.api.headers
        })
    }

    afterInteraction(response) {}

    render() {
        return (
            <button onClick={ this._onInteraction }>{ this.label }</button>
        );
    }
};

export default Interactable;
