import React from 'react';
import ReactDOM from 'react-dom';
import TestButton from './components/test_button';
import ClearButton from './components/clear_button';

class Brazier extends React.Component {
    render() {
        return (
            <div>
                <ClearButton />
                <TestButton />
            </div>
        )
    }
}

ReactDOM.render(<Brazier />, document.getElementById('app'));
