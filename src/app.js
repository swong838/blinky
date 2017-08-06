import React from 'react';
import ReactDOM from 'react-dom';
import ClearButton from './components/clear_button';

class Brazier extends React.Component {
    render() {
        return (
            <div>
                <ClearButton />
            </div>
        )
    }
}

ReactDOM.render(<Brazier />, document.getElementById('app'));
