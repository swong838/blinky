import React from 'react';
import ReactDOM from 'react-dom';
import Picker from './components/picker';
import TestButton from './components/test_button';
import ClearButton from './components/clear_button';


class Brazier extends React.Component {
    render() {
        return (
            <div>
                <ClearButton />
                <TestButton />
                <Picker initialColor="rgb(0,0,0,1)" />
            </div>
        )
    }
}

ReactDOM.render(<Brazier />, document.getElementById('app'));
